package com.example.dslist.repositories;

import com.example.dslist.entities.Book;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface BookRepository extends JpaRepository<Book,  Long> {

}
