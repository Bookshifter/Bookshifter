package com.example.bookshifter.services.interfaces;

import com.example.bookshifter.dto.RegisterUserDTO;
import com.example.bookshifter.dto.UserDTO;
import com.example.bookshifter.entities.User;
import org.springframework.boot.autoconfigure.kafka.KafkaProperties;
import org.springframework.security.core.Authentication;

import java.util.List;
import java.util.Optional;

public interface UserService {

    List<UserDTO> findAll();

    User registerUser(RegisterUserDTO dto);

    Optional<User> findByEmail(String email);

    boolean isAdminExists(String email);

    User getAuthenticatedUserInfo(Authentication authentication);

    void registerUser(String firstName, String lastName, String email, String password, String admin);

    User registerAdmin(RegisterUserDTO dto);
}
