package com.example.bookshifter.dto;

import java.util.List;

public record WishlistDTO(Long id, List<BookDTO> books) {
}
