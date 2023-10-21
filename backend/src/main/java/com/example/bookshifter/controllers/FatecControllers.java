package com.example.bookshifter.controllers;

import com.example.bookshifter.api.book.google.VolumeInfo;
import com.example.bookshifter.api.fatec.LocationInfo;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.client.RestTemplate;

@RequestMapping("/fatec")
@RestController
public class FatecControllers {
    Logger logger = LoggerFactory.getLogger(FatecControllers.class);
    @Autowired
    private RestTemplate template;
    @GetMapping("/{cep}")
    public ResponseEntity getFatec(@PathVariable String cep){
        String url = "https://viacep.com.br/ws/" + cep + "/json";
        ResponseEntity<LocationInfo> response = template.getForEntity(url, LocationInfo.class);

        logger.info("Response", response.getBody());

        return  ResponseEntity.ok(response.getBody());
    }
}
