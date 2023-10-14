package com.example.bookshifter.projections;

public interface GameMinProjection {
    Long getId();
    String getTitle();
    Integer getGameYear();
    String getImageUrl();
    String getShortDescription();
    Integer getPosition();
}
