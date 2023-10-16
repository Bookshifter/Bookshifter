package com.example.bookshifter.repositories;

import com.example.bookshifter.entities.Book;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface BookRepository extends JpaRepository<Book,  Long> {
    @Query(nativeQuery = true, value = "SELECT * FROM tb_book book WHERE book.title LIKE CONCAT('%', :query, '%')" +
            "Or book.description LIKE CONCAT('%',:query, '%')" +
            "Or book.publisher LIKE CONCAT('%', :query, '%')"
        )
    List<Book> searchAllByQuery(String query);

}
