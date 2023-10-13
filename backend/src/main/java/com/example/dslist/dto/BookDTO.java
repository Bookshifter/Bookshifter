package com.example.dslist.dto;

import com.example.dslist.entities.Book;
import jakarta.persistence.ElementCollection;

import java.util.ArrayList;
import java.util.List;

public class BookDTO{
    private String title;
    private List<String> authors = new ArrayList<String>();
    private String description;
    private Integer pageCount;

    public BookDTO(){
    }

    public BookDTO(String title, List<String> authors, String description, Integer pageCount) {
        this.title = title;
        this.authors = authors;
        this.description = description;
        this.pageCount = pageCount;
    }

    public BookDTO(Book book) {
        this.title = book.getTitle();
        this.authors = book.getAuthors();
        this.description = book.getDescription();
        this.pageCount = book.getPageCount();
    }

    public String getTitle(){
        return this.title;
    }

    public List<String> getAuthors(){
        return this.authors;
    }

    public  String getDescription(){
        return  this.description;
    }

    public Integer getPageCount(){
        return this.pageCount;
    }
}
