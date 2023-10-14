package com.example.bookshifter.controllers;

import com.example.bookshifter.dto.BookDTO;
import com.example.bookshifter.services.interfaces.BookService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

import java.util.List;

@RestController
@RequestMapping("/books")
public class BookController {
    @Autowired
    private RestTemplate template;

    @Autowired
    private BookService service;
    public static Logger logger = LoggerFactory.getLogger(BookController.class);

    @GetMapping("/isbn:{isbn}")
    public String getBook(@PathVariable Long isbn){
        service.saveBookByIsbn(isbn);
        return "Livro adicionado!";
    }

    @GetMapping("/all")
    public ResponseEntity<List<BookDTO>> findAll(){
        return ResponseEntity.ok(service.findAllBooks());
    }

    @GetMapping("/{id}")
    public ResponseEntity<BookDTO> getById(@PathVariable Long id){
        return ResponseEntity.ok(service.findById(id));
    }


    @DeleteMapping("/{id}")
    public String deleteBook(@PathVariable Long id){
        service.deleteBook(id);
        return "Livro deletado com sucesso!";
    }

}
