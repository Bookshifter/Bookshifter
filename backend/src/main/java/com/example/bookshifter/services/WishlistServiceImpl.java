package com.example.bookshifter.services;

import com.example.bookshifter.dto.BookDTO;
import com.example.bookshifter.dto.WishlistDTO;
import com.example.bookshifter.entities.Book;
import com.example.bookshifter.entities.User;
import com.example.bookshifter.entities.WishList;
import com.example.bookshifter.repositories.BookRepository;
import com.example.bookshifter.repositories.WishListRepository;
import com.example.bookshifter.services.interfaces.BookService;
import com.example.bookshifter.services.interfaces.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.Authentication;
import org.springframework.stereotype.Service;


@Service
public class WishlistServiceImpl {

    private UserService userService;
    private BookService bookService;
    private WishListRepository wishListRepository;
    private Authentication authentication;
    private BookRepository bookRepository;

    @Autowired
    public WishlistServiceImpl(UserService userService, BookService bookService, WishListRepository wishListRepository, BookRepository bookRepository){
        this.userService = userService;
        this.bookService = bookService;
        this.wishListRepository = wishListRepository;
        this.bookRepository = bookRepository;
    }

    public WishlistDTO addBookToWishList(Long id){
        User loggedUser = userService.getAuthenticatedUserInfo(authentication);

        WishList userWishList = wishListRepository.findByUser(loggedUser);
        Book book = bookRepository.findById(id).get();
        book.getWishList().add(userWishList);
        userWishList.getBooks().add(book);

        bookRepository.save(book);
        wishListRepository.save(userWishList);
        WishlistDTO dto = new WishlistDTO(userWishList.getId(), userWishList.getBooks().stream().map(BookDTO::new).toList());
        return dto;
    }
}
