package com.example.bookshifter.controllers;


import com.example.bookshifter.dto.FatecDTO;
import com.example.bookshifter.dto.ResponseFatecDTO;
import com.example.bookshifter.services.FatecServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RequestMapping("/fatec")
@RestController
public class FatecControllers {
    @Autowired
    private FatecServiceImpl service;


    @PostMapping
    public ResponseEntity<FatecDTO> getFatec(@RequestBody FatecDTO dto) {
        service.createFatec(dto);
        return  ResponseEntity.ok(dto);
    }
    @GetMapping("/books/")
    public ResponseEntity<ResponseFatecDTO> getInfo(@RequestParam("fatecID") Long id){
        return ResponseEntity.ok(service.getAllFatecBooks(id));
    }
}
