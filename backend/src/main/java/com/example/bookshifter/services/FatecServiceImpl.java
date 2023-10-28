package com.example.bookshifter.services;

import com.example.bookshifter.api.fatec.LocationInfo;
import com.example.bookshifter.dto.BookDTO;
import com.example.bookshifter.dto.FatecDTO;
import com.example.bookshifter.dto.ResponseFatecDTO;
import com.example.bookshifter.entities.Book;
import com.example.bookshifter.entities.Fatec;
import com.example.bookshifter.repositories.BookRepository;
import com.example.bookshifter.repositories.FatecRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.List;
import java.util.Optional;

@Service
public class FatecServiceImpl {
    @Autowired
    private FatecRepository repository;
    @Autowired
    private BookRepository bookRepository;
    @Autowired
    private RestTemplate template;

    public FatecDTO createFatec(FatecDTO dto){
        String url ="https://viacep.com.br/ws/" + dto.cep() + "/json/";

        ResponseEntity<LocationInfo> response = template.getForEntity(url, LocationInfo.class);
        Fatec newFatec = new Fatec(dto.name(), response.getBody().getRua(), response.getBody().getBairro(),
                response.getBody().getCidade());
        repository.save(newFatec);
        return dto;
    }

    public ResponseFatecDTO getAllFatecBooks(Long fatecId){
        Optional<Fatec> fatecOptional = repository.findById(fatecId);

        if(fatecOptional.isPresent()){
            Fatec fatec = fatecOptional.get();
            List<Book> book = bookRepository.findByFatecId(fatecId);
            var booksDTO = book.stream().map(BookDTO::new).toList();

            ResponseFatecDTO fatecDTO = new ResponseFatecDTO(fatec, booksDTO);
            return fatecDTO;
        }
        throw new RuntimeException("A Fatec desejada não é elegível");
    }
}
