package com.example.bookshifter.projections;

import java.util.List;

public interface BookMinProjection {
    Long getId();
    String getTitle();
    String getPublisher();
    String getMediumCoverUrl();
}
