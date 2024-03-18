package com.example.bookshifter.controllers;

import com.example.bookshifter.dto.BookDTO;
import com.example.bookshifter.dto.BookRequestDTO;

import com.example.bookshifter.exceptions.ApiException;
import com.example.bookshifter.exceptions.BookException;
import com.example.bookshifter.exceptions.FatecException;
import com.example.bookshifter.services.interfaces.BookService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.util.UriComponentsBuilder;

import java.net.URI;
import java.util.List;

@RestController
@RequestMapping("/books")
public class BookController {

    @Autowired
    private BookService service;

    @CrossOrigin("*")
    @PostMapping
    public ResponseEntity<?> createBook(@RequestParam(name = "isbn") Long isbn, @RequestParam(name = "fatecId") Long fatecId, @RequestBody BookRequestDTO dto, UriComponentsBuilder ucb){
        try {
            BookDTO createdBook = service.saveBookByIsbn(isbn, fatecId, dto);
            URI createdBookURI = ucb.path("/books/{id}").buildAndExpand(createdBook.getId()).toUri();
            return ResponseEntity.created(createdBookURI).build();
        } catch (ApiException | FatecException exception ){
            return ResponseEntity.status(404).body(exception.getStatusText());
        }

    }

    @GetMapping
    public ResponseEntity<List<BookDTO>> findAll(){
        return ResponseEntity.ok(service.findAllBooks());
    }

    @GetMapping("/search")
    public ResponseEntity<List<BookDTO>> searchBook(@RequestParam String query){
        return ResponseEntity.ok(service.searchProducts(query));
    }

    @GetMapping("/{id}")
    public ResponseEntity<?> getById(@PathVariable Long id){
        try {
            BookDTO book = service.findById(id);
            return ResponseEntity.ok(book);
        } catch (BookException exception){
            return ResponseEntity.status(404).body(exception.getStatusText());
        }
    }


    @CrossOrigin(origins="*")
    @DeleteMapping("/{id}")
    public ResponseEntity<String> deleteBook(@PathVariable Long id){

        try {
            service.deleteBook(id);
            return ResponseEntity.noContent().build();
        } catch(BookException error){
            return ResponseEntity.status(404).body("Livro não encontrado");
        }
    }
}
