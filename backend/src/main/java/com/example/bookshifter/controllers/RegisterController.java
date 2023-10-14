package com.example.bookshifter.controllers;

import com.example.bookshifter.dto.RegisterUserDTO;
import com.example.bookshifter.entities.User;
import com.example.bookshifter.entities.VerificationToken;
import com.example.bookshifter.events.RegistrationCompleteEvent;
import com.example.bookshifter.services.interfaces.UserService;
import com.example.bookshifter.services.interfaces.VerificationTokenService;
import com.example.bookshifter.utils.UrlUtil;
import jakarta.servlet.http.HttpServletRequest;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@Controller
@RequestMapping("/register")
public class RegisterController {
    @Autowired
    private UserService service;
    @Autowired
    private ApplicationEventPublisher publisher;
    @Autowired
    private VerificationTokenService tokenService;

    @GetMapping
    public String registrationForm(Model model){
        model.addAttribute("user", new RegisterUserDTO());
        return "registration";
    }

    @PostMapping
    public String registerUser(@ModelAttribute("user") RegisterUserDTO registerDTO, HttpServletRequest request){
        User user = service.registerUser(registerDTO);
        publisher.publishEvent(new RegistrationCompleteEvent(user, UrlUtil.getApplicationUrl(request)));
        return "redirect:/register?success";
    }

    @GetMapping("/enableAccount")
    public String enableAccount(@RequestParam("token") String token){
        Optional<VerificationToken> verificationToken = tokenService.findByToken(token);
        if(verificationToken.isPresent() && verificationToken.get().getUser().isEnabled()){
             return "redirect:/login?verified";
        }

        String validation = tokenService.validateToken(token);
        switch(validation.toLowerCase()){
            case "expired":
                return "redirect:/error?expired";
            case "valid":
                return "redirect:/login?valid";
            default:
                return "redirect:/error?invalid";
        }
    }
}
