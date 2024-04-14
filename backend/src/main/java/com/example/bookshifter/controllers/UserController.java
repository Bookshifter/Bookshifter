package com.example.bookshifter.controllers;

import com.example.bookshifter.dto.UserAndBookDTO;
import com.example.bookshifter.dto.UserDTO;
import com.example.bookshifter.exceptions.BookException;
import com.example.bookshifter.services.interfaces.BookService;
import com.example.bookshifter.services.interfaces.UserService;
import org.hibernate.annotations.NotFound;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequestMapping("/user")
public class UserController {
    @Autowired
    private UserService service;

    private BookService bookService;

    @Autowired
    public UserController(BookService bookService){
        this.bookService = bookService;
    }


    /*@GetMapping("/books")
    public ResponseEntity<UserAndBookDTO> getUserBooks(){
        try{
            return ResponseEntity.ok(bookService.getAuthenticatedUserBooks());
        } catch(BookException exception){
            return ResponseEntity.notFound().build();
        }
    }*/

}
