package com.example.bookshifter.services;

import com.example.bookshifter.dto.FatecDTO;
import com.example.bookshifter.entities.Fatec;
import com.example.bookshifter.repositories.FatecRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

@Service
public class FatecServiceImpl {
    @Autowired
    private FatecRepository repository;
    @Autowired
    private RestTemplate template;

    public FatecDTO createFatec(FatecDTO dto){


        Fatec newFatec = new Fatec(dto.name());
        repository.save(newFatec);
        return dto;

    }
}
