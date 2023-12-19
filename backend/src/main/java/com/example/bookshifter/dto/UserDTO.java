package com.example.bookshifter.dto;

import com.example.bookshifter.entities.User;

public class UserDTO {
    private String firstName;
    private String lastName;
    private String email;


    public UserDTO(){

    }

    public UserDTO(User user){
        this.firstName = user.getFirstName();
        this.lastName = user.getLastName();
        this.email = user.getEmail();

    }

    public String getFirstName() {
        return firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public String getEmail() {
        return email;
    }

}
