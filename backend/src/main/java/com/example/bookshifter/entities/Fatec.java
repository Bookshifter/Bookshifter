package com.example.bookshifter.entities;

import com.example.bookshifter.api.fatec.LocationInfo;
import jakarta.persistence.*;

@Entity
@Table(name = "tb_fatec")
public class Fatec {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

     transient private LocationInfo info;

    public Fatec(){
    }

    public Fatec(String name){
        this.name = name;
    }

    public String getName() {
        return name;
    }

    public void setName(String name){
        this.name = name;
    }
}
