package com.demo.api.controller;

import com.demo.api.dto.MembersDTO;
import com.demo.api.dto.ResponseDTO;
import com.demo.api.security.util.JWTUtil;
import com.demo.api.service.MembersService;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.RequiredArgsConstructor;
import lombok.extern.java.Log;
import lombok.extern.log4j.Log4j2;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.logout.SecurityContextLogoutHandler;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

@Log4j2
@Validated
@RequiredArgsConstructor
@RestController
@RequestMapping("auth")
public class AuthController {

    private final MembersService membersService;
    private final JWTUtil jwtUtil;

    @PostMapping(value = "/join")
    public ResponseEntity<Long> register(@RequestBody MembersDTO membersDTO) {
        log.info("register..." + membersDTO);
    /*
    http://localhost:8089/server/members/join  (post)
    {
      "id":"user101@example.com",
      "password":"1",
      "name":"사용자101",
      "gender":"남",
      "email":"user101@example.com",
      "mobile":"010-1234-1234",
      "fromSocial":false,
      "roleSet":["ROLE_USER"]
    }
    */
        long num = membersService.registMembersDTO(membersDTO);
        return new ResponseEntity<>(num, HttpStatus.OK);
    }


    @PostMapping("/logout")
    public ResponseEntity<ResponseDTO> logout(HttpServletRequest request, HttpServletResponse response) {
        try {
            new SecurityContextLogoutHandler().logout(request, response, SecurityContextHolder.getContext().getAuthentication());
            return new ResponseEntity<>(new ResponseDTO("success", true), HttpStatus.OK);
        } catch (Exception e) {
            return new ResponseEntity<>(new ResponseDTO(e.getMessage(), false), HttpStatus.NOT_FOUND);
        }
    }

    @PostMapping(value = "/login", consumes = MediaType.ALL_VALUE,
            produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Map<String,String>> getToken(HttpServletResponse response,
                                           @RequestBody Map<String, Object> mapObj) {
        log.info("나와라");
        String email = mapObj.get("email").toString();
        String pass = mapObj.get("pass").toString();
        log.info(email + "/" + pass);
        String token = membersService.login(email, pass, jwtUtil);
        Map<String ,String> map = new HashMap<>();
        if (token != "" && token.length() > 1) {
            /*try {
                //response.setContentType("text/plain");
                //response.getOutputStream().write(token.getBytes());

            } catch (IOException e) {
                throw new RuntimeException(e);
            }*/
            map.put("token",token);
        }

        return new ResponseEntity<Map<String,String>>(map, HttpStatus.OK);
    }

}//end
