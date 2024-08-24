package com.example.bookshifter.entities;


import jakarta.persistence.*;

import java.util.ArrayList;
import java.util.List;
import java.util.Set;

@Entity
@Table(name = "tb_fatec")
public class Fatec {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;






    private String name;

    private String street;
    private String neighborhood;
    private String city;



    @OneToMany

    private List<Book> books = new ArrayList<>();



    public Fatec() {
    }

    public Fatec(String name, String street, String neighborhood, String city) {
        this.name = name;
        this.street = street;
        this.neighborhood = neighborhood;
        this.city = city;

    }

    public Long getId() {
        return this.id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getStreet() {
        return this.street;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public String getNeighborhood() {
        return this.neighborhood;
    }

    public String getCity() {
        return this.city;
    }

    public List<Book> getBooks(){
        return this.books;
    }




    public void setCity(String city) {
        this.city = city;
    }
}
