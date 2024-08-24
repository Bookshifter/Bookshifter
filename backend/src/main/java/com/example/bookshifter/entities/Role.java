package com.example.bookshifter.entities;

public enum Role {
    USER("USER"),
    ADMIN("ADMIN"),
    LIBRARY("LIBRARY");

    private String value;

    private Role(String value) {
        this.value = value;
    }

    public String getValue() {
        return value;
    }

    public static Role getRole(String  value){
        for(Role role : Role.values()){
            if(role.getValue().equalsIgnoreCase(value)){
                return role;
            }

        }
        throw new IllegalArgumentException("Role informada inválida");
    }
}
