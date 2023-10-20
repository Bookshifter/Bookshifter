package com.example.bookshifter.controllers;

import com.example.bookshifter.api.book.google.VolumeInfo;
import com.example.bookshifter.api.fatec.LocationInfo;
import com.example.bookshifter.dto.FatecDTO;
import com.example.bookshifter.services.FatecServiceImpl;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

@RequestMapping("/fatec")
@RestController
public class FatecControllers {
    @Autowired
    private FatecServiceImpl service;
    Logger logger = LoggerFactory.getLogger(FatecControllers.class);
    @Autowired
    private RestTemplate template;
    @PostMapping
    public ResponseEntity getFatec(@RequestBody FatecDTO dto) {
        service.createFatec(dto);

        return  ResponseEntity.ok(dto);
    }
}
