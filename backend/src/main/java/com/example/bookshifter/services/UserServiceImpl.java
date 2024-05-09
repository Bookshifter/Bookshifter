package com.example.bookshifter.services;

import com.example.bookshifter.dto.RegisterUserDTO;

import com.example.bookshifter.dto.UserDTO;
import com.example.bookshifter.entities.Role;
import com.example.bookshifter.entities.User;
import com.example.bookshifter.entities.WishList;
import com.example.bookshifter.exceptions.JWTExcepion;
import com.example.bookshifter.repositories.BookRepository;
import com.example.bookshifter.repositories.UserRepository;
import com.example.bookshifter.repositories.WishListRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.authentication.AnonymousAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.UsernameNotFoundException;

import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

@Service
public class UserServiceImpl implements com.example.bookshifter.services.interfaces.UserService {
    @Autowired
    private UserRepository repository;
    @Autowired
    private PasswordEncoder passwordEncoder;
    @Autowired
    private BookRepository bookRepository;
    @Autowired
    private WishListRepository wishListRepository;

    @Override
    public List<UserDTO> findAll() {
        var result = repository.findAll();

        List<UserDTO> users = result.stream().map(UserDTO::new).toList();
        return users;
    }

    @Override
    public User registerUser(RegisterUserDTO dto) {
        User newUser = new User(dto.getFirstName(), dto.getLastName(), dto.getEmail(),
                passwordEncoder.encode(dto.getPassword()), Role.USER);

        WishList userWishList = new WishList(0, newUser);

        repository.save(newUser);
        wishListRepository.save(userWishList);

        return newUser;
    }

    @Override
    public Optional<User> findByEmail(String email) {
        return Optional.ofNullable(repository.findByEmail(email)
                .orElseThrow(() -> new UsernameNotFoundException("Usuário não encontrado")));
    }

    @Override
    public User getAuthenticatedUserInfo(Authentication authentication) {
        if (!(authentication instanceof AnonymousAuthenticationToken)) {
            String getEmail = SecurityContextHolder.getContext().getAuthentication().getName();

            Optional<User> userOptional = repository.findByEmail(getEmail);
            if (userOptional.isPresent()) {
                return userOptional.get();
            }
        }
        throw new JWTExcepion("Token JWT expirado ou não informado, por favor tente novamente");
    }

    public User registerAdmin(RegisterUserDTO dto) {
        if (!isAdminExists(dto.getEmail())) {
            User newAdmin = new User(dto.getFirstName(), dto.getLastName(), dto.getEmail(), passwordEncoder.encode(dto.getPassword()), Role.ADMIN);
            newAdmin.setEnabled(true);
            repository.save(newAdmin);

        }
        else{
            throw new RuntimeException("Admin already exists");

        }
        return null;
    }

    public boolean isAdminExists(String email) {
        Optional<User> admin = repository.findByEmailAndRole(email, Role.ADMIN);
        return admin.isPresent();

    }
}
