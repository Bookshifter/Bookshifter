package com.example.bookshifter.entities;

import jakarta.persistence.*;

import java.util.ArrayList;
import java.util.List;

@Entity
@Table(name = "tb_wishlist")
public class WishList {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private Integer quantity;

    @OneToOne
    public User user;

    @ManyToMany
    @JoinTable(name = "tb_wishlist_books",
    joinColumns = @JoinColumn(name = "wishlist_id"),
    inverseJoinColumns = @JoinColumn(name = "book_id"))
    public List<Book> books = new ArrayList<>();


    public WishList(){

    }

    public WishList(Integer quantity, User user) {
        this.quantity = quantity;
        this.user = user;
    }

    public Long getId() {
        return id;
    }
    public Integer getQuantity() {
        return this.getBooks().size();
    }

    public void setQuantity(Integer quantity) {
        this.quantity = quantity;
    }

    public User getUser() {
        return user;
    }

    public List<Book> getBooks() {
        return books;
    }


}
