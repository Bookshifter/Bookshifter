package com.example.bookshifter.controllers;


import com.example.bookshifter.dto.FatecDTO;
import com.example.bookshifter.dto.FatecInfoDTO;
import com.example.bookshifter.dto.ResponseFatecDTO;
import com.example.bookshifter.exceptions.FatecException;
import com.example.bookshifter.services.FatecServiceImpl;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequestMapping("/fatecs")
@RestController
public class FatecController {
    @Autowired
    private FatecServiceImpl service;


    @PostMapping
    public ResponseEntity<?> createFatec(@RequestBody FatecDTO dto) {
        try {
            service.createFatec(dto);
            return  ResponseEntity.ok(dto);
        } catch(FatecException exception){
            return ResponseEntity.status(409).body(exception.getStatusText());
        }

    }
    @GetMapping("/books")
    public ResponseEntity<ResponseFatecDTO> getFatecBooks(@RequestParam("fatecID") Long id){
        return ResponseEntity.ok(service.getAllFatecBooks(id));
    }

    @GetMapping
    public ResponseEntity<List<FatecInfoDTO>> getAll(){
        return ResponseEntity.ok(service.getAll());
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getFatecById(@PathVariable Long id){
        try{
            return ResponseEntity.ok(service.getFatecById(id));
        } catch(FatecException exception){
            return ResponseEntity.status(404).body(exception.getStatusText());
        }

    }
}
