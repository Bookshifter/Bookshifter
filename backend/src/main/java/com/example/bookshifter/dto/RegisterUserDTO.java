package com.example.bookshifter.dto;

import lombok.Data;

import java.util.List;

@Data
public class RegisterUserDTO {
    private String firstName;
    private String lastName;
    private String email;
    private String password;
}

