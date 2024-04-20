package com.example.bookshifter.controllers;

import com.example.bookshifter.dto.RegisterUserDTO;
import com.example.bookshifter.services.interfaces.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/createadmin")
public class AdminController {


    @Autowired
    private UserService userService;

    @PostMapping
    public ResponseEntity<String> createadmin(@RequestBody RegisterUserDTO requestDTO){
        if(userService.isAdminExists()){
            return ResponseEntity.badRequest().body("Admin ja existe");
        }

        userService.registerAdmin(requestDTO);

        return ResponseEntity.ok("Admin criado com sucesso");
    }
}
