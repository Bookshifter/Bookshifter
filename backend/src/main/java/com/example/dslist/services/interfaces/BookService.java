package com.example.dslist.services.interfaces;

import com.example.dslist.dto.BookDTO;

import java.util.List;

public interface BookService {
    BookDTO saveBookByIsbn(Long isbn);

    List<BookDTO> findAllBooks();

    BookDTO findById(Long id);

    void deleteBook(Long id);
}
