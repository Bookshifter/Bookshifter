package com.example.bookshifter.repositories;

import com.example.bookshifter.entities.Book;
import org.springframework.data.jpa.repository.JpaRepository;

public interface BookRepository extends JpaRepository<Book,  Long> {

}
