package com.example.dslist.entities;


import jakarta.persistence.*;

import java.util.ArrayList;
import java.util.List;

@Entity(name = "tb_book")
public class Book {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    @ElementCollection
    private List<String> authors = new ArrayList<String>();

    @Column(columnDefinition = "TEXT")
    private String description;

    private String publisher;

    private Integer publishYear;

    private Integer pageCount;

    private String largeCoverUrl;

    @Column(name = "medium_cover_url")
    private String mediumCoverUrl;
    public Book(){
    }

    public Book(String title, List<String> authors, String description, String publisher, Integer publishYear,
                Integer pageCount, String largeCoverUrl, String mediumCoverUrl)
    {
        this.title = title;
        this.authors = authors;
        this.description = description;
        this.publisher = publisher;
        this.publishYear = publishYear;
        this.pageCount = pageCount;
        this.largeCoverUrl = largeCoverUrl;
        this.mediumCoverUrl = mediumCoverUrl;
    }

    public Long getId(){return this.id; }
    public String getTitle(){
        return this.title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<String> getAuthors(){
        return this.authors;
    }

    public void setAuthors(List<String> authors) {
        this.authors = authors;
    }

    public  String getDescription(){
        return  this.description;
    }
    public void setDescription(String description) {
        this.description = description;
    }

    public String getPublisher(){
        return this.publisher;
    }

    public Integer getPublishYear(){
        return this.publishYear;
    }
    public Integer getPageCount(){
        return this.pageCount;
    }
    public void setPageCount(Integer pageCount) {
        this.pageCount = pageCount;
    }

    public String getLargeCoverUrl(){
        return this.largeCoverUrl;
    }

    public void setLargeCoverUrl(String largeCoverUrl) {
        this.largeCoverUrl = largeCoverUrl;
    }

    public String getMediumCoverUrl(){
        return this.mediumCoverUrl;
    }

}
