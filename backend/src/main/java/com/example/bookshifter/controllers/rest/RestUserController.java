package com.example.bookshifter.controllers.rest;

import com.example.bookshifter.services.interfaces.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/rest-users")
public class RestUserController {
    @Autowired
    private UserService service;

    @GetMapping
    public ResponseEntity findAll(){
        return ResponseEntity.ok(service.findAll());
    }
}
