package com.example.bookshifter.dto;

import java.util.List;

public record UserAndBookDTO(UserDTO owner, List<BookDTO> books) {

}
