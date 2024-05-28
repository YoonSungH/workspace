package com.demo.api.security.handler;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import lombok.extern.log4j.Log4j2;
import org.json.JSONObject;
import org.springframework.security.authentication.*;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.web.authentication.AuthenticationFailureHandler;

import java.io.IOException;
import java.io.PrintWriter;

@Log4j2
public class ApiLoginFailHandler implements AuthenticationFailureHandler {
  @Override
  public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
    exception.printStackTrace();
    writePrintErrorResponse(response, exception);
  }

  private void writePrintErrorResponse(HttpServletResponse response, AuthenticationException exception) {
    try {
      response.setContentType("application/json;charset=utf-8");
      JSONObject jsonObject = new JSONObject();
      String message = exception.getMessage();
      jsonObject.put("code", "401");
      jsonObject.put("message", message);
      PrintWriter printWriter = response.getWriter();
      printWriter.print(jsonObject);
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  private String getExceptionMessage(AuthenticationException exception) {
    if (exception instanceof BadCredentialsException) {
      return "비밀번호 불일치";
    } else if (exception instanceof UsernameNotFoundException) {
      return "계정없음";
    } else if (exception instanceof AccountExpiredException) {
      return "계정만료";
    } else if (exception instanceof CredentialsExpiredException) {
      return "비밀번호 만료";
    } else if (exception instanceof DisabledException) {
      return "계정 비활성화";
    } else if (exception instanceof LockedException) {
      return "계정잠김";
    } else {
      return "확인된 에러가 없습니다.";
    }
  }


//  @Override
//  public void onAuthenticationFailure(HttpServletRequest request, HttpServletResponse response, AuthenticationException exception) throws IOException, ServletException {
//    log.info("login fail hanlder.... exception.getMessage() : " + exception.getMessage());
//    response.setStatus(HttpServletResponse.SC_UNAUTHORIZED);
//    response.setContentType("application/json;charset=utf-8");
//    JSONObject jsonObject = new JSONObject();
//    String message = exception.getMessage();
//    jsonObject.put("code","401");
//    jsonObject.put("message",message);
//    PrintWriter printWriter = response.getWriter();
//    printWriter.print(jsonObject);
//
//  }


}//end
