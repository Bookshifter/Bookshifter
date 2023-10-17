package com.example.bookshifter.services.interfaces;

import com.example.bookshifter.dto.BookDTO;
import com.example.bookshifter.dto.MinimalBookDTO;

import java.util.List;

public interface BookService {
    BookDTO saveBookByIsbn(Long isbn);

    List<MinimalBookDTO> findAllBooks();

    BookDTO findById(Long id);

    void deleteBook(Long id);

    List<BookDTO> searchProducts(String query);
}
