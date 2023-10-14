package com.example.bookshifter.dto;

import com.example.bookshifter.entities.Book;
import lombok.Data;

import java.util.ArrayList;
import java.util.List;

@Data
public class BookDTO{
    private Long id;
    private String title;
    private List<String> authors = new ArrayList<String>();
    private String description;
    private String publisher;
    private Integer publishYear;
    private Integer pageCount;
    private String largeCoverUrl;
    private String mediumCoverUrl;

    public BookDTO(){
    }

    public BookDTO(String title, List<String> authors, String description, String publisher,
                   Integer publishYear, Integer pageCount, String largeCoverUrl, String mediumCoverUrl) {
        this.title = title;
        this.authors = authors;
        this.description = description;
        this.publisher = publisher;
        this.publishYear = publishYear;
        this.pageCount = pageCount;
        this.largeCoverUrl = largeCoverUrl;
        this.mediumCoverUrl = mediumCoverUrl;
    }

    public BookDTO(Book book) {
        this.id = book.getId();
        this.title = book.getTitle();
        this.authors = book.getAuthors();
        this.description = book.getDescription();
        this.publisher = book.getPublisher();
        this.publishYear = book.getPublishYear();
        this.pageCount = book.getPageCount();
        this.largeCoverUrl = book.getLargeCoverUrl();
        this.mediumCoverUrl = book.getMediumCoverUrl();
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

    public String getPublisher(){
        return this.publisher;
    }

    public Integer getPublishYear(){
        return  this.publishYear;
    }

    public Integer getPageCount(){
        return this.pageCount;
    }

    public String getLargeCoverUrl(){
        return  this.largeCoverUrl;
    }

    public String getMediumCoverUrl(){
        return this.mediumCoverUrl;
    }
}
