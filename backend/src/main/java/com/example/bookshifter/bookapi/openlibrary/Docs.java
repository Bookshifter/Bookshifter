package com.example.bookshifter.bookapi.openlibrary;

import com.fasterxml.jackson.annotation.JsonIgnoreProperties;
import com.fasterxml.jackson.annotation.JsonProperty;

import java.util.ArrayList;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Docs {
    @JsonProperty("publish_year")
    private ArrayList<Integer> publishYear = new ArrayList<>();

    public ArrayList<String> publisher = new ArrayList<>();

    public ArrayList<Integer> getPublishYear(){
        return  this.publishYear;
    }

    public void setPublishYear(ArrayList<Integer> publishYear) {
        this.publishYear = publishYear;
    }

    public ArrayList<String> getPublisher(){
        return this.publisher;
    }
    public void setPublisher(ArrayList<String> publisher) {
        this.publisher = publisher;
    }
}
