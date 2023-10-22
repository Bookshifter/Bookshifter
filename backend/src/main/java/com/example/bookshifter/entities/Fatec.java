package com.example.bookshifter.entities;

import com.example.bookshifter.api.fatec.LocationInfo;
import jakarta.persistence.*;

import java.util.List;

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
    @OneToMany(mappedBy = "book")
    @JoinColumn(name = "book")
    transient private List<Book> book;

    public Fatec(){
    }

    public Fatec(String name, String street, String neighborhood, String city){
        this.name = name;
        this.street = street;
        this.neighborhood = neighborhood;
        this.city = city;

    }

    public String getName() {
        return name;
    }

    public void setName(String name){
        this.name = name;
    }

    public String getStreet(){
        return this.street;
    }

    public void setStreet(String street){
        this.street = street;
    }

    public String getNeighborhood(){
        return  this.neighborhood;
    }

    public String getCity(){
        return this.city;
    }

    public void setCity(String city){
        this.city = city;
    }

    public void setBook( List<Book> book) {
        this.book = book;
    }
}