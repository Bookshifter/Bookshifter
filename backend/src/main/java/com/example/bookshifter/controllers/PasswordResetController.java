package com.example.bookshifter.controllers;

import com.example.bookshifter.dto.NewPasswordDTO;
import com.example.bookshifter.dto.PasswordResetEmailRequest;
import com.example.bookshifter.entities.User;
import com.example.bookshifter.events.PasswordRecoveryEvent;
import com.example.bookshifter.services.PasswordResetTokenServiceImpl;
import com.example.bookshifter.services.UserServiceImpl;
import com.example.bookshifter.utils.UrlUtil;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;
@RestController
@RequestMapping("/forgot-password")
public class PasswordResetController {
    @Autowired
    private UserServiceImpl userService;

    @Autowired
    private ApplicationEventPublisher publisher;

    @Autowired
    private PasswordResetTokenServiceImpl service;

    @PostMapping
    public ResponseEntity<String> sendResetPasswordRequest(@RequestBody PasswordResetEmailRequest dto, HttpServletRequest request){
        Optional<User> user = userService.findByEmail(dto.email());

        if(user.isEmpty()){
            return ResponseEntity.status(404).body("Usuário não encontrado");
        }

        publisher.publishEvent(new PasswordRecoveryEvent(user.get(), UrlUtil.getApplicationUrl(request)));
        return  ResponseEntity.status(200).body("Email de mudança de senha enviado");
    }

    @PostMapping("/password-reset")
    public ResponseEntity<String> resetPassword(@RequestBody NewPasswordDTO request, @RequestParam("token") String requestToken){
        String validationTokenResult = service.validateToken(requestToken);
        if(validationTokenResult.equalsIgnoreCase("valid")){
            Optional<User> user = service.findUserByToken(requestToken);

            if(user.isPresent()){
                if (checkValidation(request.newPassword(), request.passwordConfirmation()).equalsIgnoreCase("valid")){
                    service.resetPassword(user.get(), request.newPassword());
                    service.deleteToken(requestToken);
                    return ResponseEntity.status(200).body("Senha alterada com sucesso");
                } else ResponseEntity.status(409).body("As senhas não coincidem");
            }
        } else if(validationTokenResult.equalsIgnoreCase("expired")) {
            return ResponseEntity.status(401).body("Token de recuperação de senha expirado, por favor gere outro token");
        }

        return ResponseEntity.status(406).body("Token não pertence a nenhum usuário");
    }

    private String checkValidation(String newPassword, String newPasswordConfirmation){
        if(newPassword.equalsIgnoreCase(newPasswordConfirmation)){
            return "VALID";
        }
        return "INVALID";
    }
}
