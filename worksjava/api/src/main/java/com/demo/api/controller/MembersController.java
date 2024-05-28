package com.demo.api.controller;

import com.demo.api.dto.MembersDTO;
import com.demo.api.service.MembersService;
import lombok.RequiredArgsConstructor;
import lombok.extern.log4j.Log4j2;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@Log4j2
@RequestMapping("/members/")
@RequiredArgsConstructor
public class MembersController {
  private final MembersService membersService;

//  @PostMapping(value = "/join")
//  public ResponseEntity<Long> register(@RequestBody MembersDTO membersDTO) {
//    log.info("register..."+membersDTO);
//    /*
//    http://localhost:8089/server/members/join  (post)
//    {
//      "id":"user101@example.com",
//      "password":"1",
//      "name":"사용자101",
//      "gender":"남",
//      "email":"user101@example.com",
//      "mobile":"010-1234-1234",
//      "fromSocial":false,
//      "roleSet":["ROLE_USER"]
//    }
//    */
//    long num = membersService.registMembersDTO(membersDTO);
//    return new ResponseEntity<>(num, HttpStatus.OK);
//  }
  @PutMapping(value = "/update", produces = MediaType.TEXT_PLAIN_VALUE)
  public ResponseEntity<String> update(@RequestBody MembersDTO membersDTO) {
    log.info("update..."+membersDTO);
    /*
    http://localhost:8089/server/members/update  (put)
    {
      "mno":"101",
      "id":"user101@example.com",
      "password":"1",
      "name":"사용자의101",
      "gender":"남",
      "email":"user101@example.com",
      "mobile":"010-1234-1234",
      "fromSocial":false,
      "roleSet":["ROLE_USER"]
    }
    */
    membersService.updateMembersDTO(membersDTO);
    return new ResponseEntity<>("modified", HttpStatus.OK);
  }

  @DeleteMapping(value = "/delete/{num}", produces = MediaType.TEXT_PLAIN_VALUE)
  public ResponseEntity<String> delete(@PathVariable("num") Long num) {
    log.info("delete.........");

    membersService.removeMembers(num);
    return new ResponseEntity<>("removed", HttpStatus.OK);
  }

  @GetMapping(value = "/get/{num}", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<MembersDTO> read(@PathVariable("num") Long num) {
    log.info("read......... "+num);

    return new ResponseEntity<>(membersService.get(num), HttpStatus.OK);
  }
  @GetMapping(value = "/get/all", produces = MediaType.APPLICATION_JSON_VALUE)
  public ResponseEntity<List<MembersDTO>> getAll() {
    log.info("getList......... ");

    return new ResponseEntity<>(membersService.getAll(), HttpStatus.OK);
  }
}
