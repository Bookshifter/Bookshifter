package com.example.bookshifter.repositories;

import com.example.bookshifter.entities.User;
import com.example.bookshifter.entities.WishList;
import org.springframework.data.jpa.repository.JpaRepository;

public interface WishListRepository extends JpaRepository<WishList, Long> {

    WishList findByUser(User user);
}
