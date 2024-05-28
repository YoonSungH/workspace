package com.demo.api.config;

import com.demo.api.security.filter.ApiCheckFilter;
import com.demo.api.security.filter.ApiLoginFilter;
import com.demo.api.security.handler.ApiLoginFailHandler;
import com.demo.api.security.util.JWTUtil;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.method.configuration.EnableMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityCustomizer;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.security.web.savedrequest.HttpSessionRequestCache;

@Log4j2
@Configuration
@EnableWebSecurity
@EnableMethodSecurity
//@RequiredArgsConstructor
public class SecurityConfig {
//  private final CorsConfig corsConfig;
  private static final String[] PERMIT_ALL_LIST = {
      //"/members/join", "/members/login",
    "/auth/join", "/auth/login",  "/error/**", "/",
    "/members/get/**", "/members/delete/**", "/members/update"
};
  private static final String[] AUTHENTICATED_LIST = {
      "/follow/**",
      "/image/**",
      "/like/board"
  };
  private static final String[] ADMIN_LIST = {
      "/admin/**",
      "/report/**", "/users/approve/**", "/users/filter-find/**"
  };

  @Bean
  public WebSecurityCustomizer webSecurityCustomizer(){
    return web ->{
      web.ignoring().requestMatchers("/favicon.ico", "/error");
    };
  }

  @Bean
  protected SecurityFilterChain config(HttpSecurity httpSecurity,AuthenticationManager am) throws Exception {
    httpSecurity.csrf(AbstractHttpConfigurer::disable);
    //httpSecurity.cors(corsConfigurer -> corsConfigurer.configurationSource(corsConfig.corsConfigurationSource()));
    httpSecurity.authorizeHttpRequests(authorizationManagerRequestMatcherRegistry -> {
      authorizationManagerRequestMatcherRegistry.requestMatchers(PERMIT_ALL_LIST).permitAll();
      authorizationManagerRequestMatcherRegistry.requestMatchers(AUTHENTICATED_LIST).authenticated();
      authorizationManagerRequestMatcherRegistry.requestMatchers(ADMIN_LIST).hasAuthority("[ADMIN]");
      authorizationManagerRequestMatcherRegistry.anyRequest().denyAll();
    });

    // UsernamePasswordAuthenticationFilter 이전에 동작하도록 filter chain 에 지정
    httpSecurity.addFilterBefore(apiCheckFilter(), UsernamePasswordAuthenticationFilter.class);

//  httpSecurity.addFilterBefore(apiLoginFilter(am), UsernamePasswordAuthenticationFilter.class);
//
    //cors settings
    //httpSecurity.cors(corsConfigurer -> corsConfigurer.corsConfigurationSource());

    httpSecurity.csrf(AbstractHttpConfigurer::disable);


    //cache 없게 하기
    HttpSessionRequestCache requestCache = new HttpSessionRequestCache();
    requestCache.setMatchingRequestParameterName(null);
    httpSecurity.requestCache(cache -> cache.requestCache(requestCache));

    //session stateless
    httpSecurity.sessionManagement(sessionManagemnetConfigurer ->
        sessionManagemnetConfigurer.sessionCreationPolicy(SessionCreationPolicy.STATELESS));
    return httpSecurity.build();
  }

  @Bean
  PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
  }

  @Bean
  public JWTUtil jwtUtil() {
    return new JWTUtil();
  }

  @Bean // 클라이언트로부터 요청된 주소에 권한이 있는지 없는지 확인
  public ApiCheckFilter apiCheckFilter() {
    String[] pattern = {"/members/**"}; // AntPathMatcher의 패턴 표기법
    return new ApiCheckFilter(pattern, jwtUtil());
  }

//  @Bean
//  public ApiLoginFilter apiLoginFilter(AuthenticationManager am) throws Exception{
//    ApiLoginFilter apiLoginFilter = new ApiLoginFilter("/auth/login",jwtUtil());
//    apiLoginFilter.setAuthenticationManager(am);
//    apiLoginFilter.setAuthenticationFailureHandler(new ApiLoginFailHandler());
//    return apiLoginFilter;
//  }


  @Bean
  // authentication bean
  public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration) throws Exception {
    return authenticationConfiguration.getAuthenticationManager();
  }
}




