package com.example.bookshifter.repositories;

import com.example.bookshifter.entities.Role;
import com.example.bookshifter.entities.User;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.security.core.userdetails.UserDetails;

import java.util.Optional;

public interface UserRepository extends JpaRepository<User, Long> {
    Optional<User> findByEmail(String email);

    UserDetails findUserByEmail(String email);

    Optional<User> findByEmailAndRole(String email, Role role);
}
