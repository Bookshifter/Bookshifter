package com.example.bookshifter.services.interfaces;

import com.example.bookshifter.dto.GameInfo;
import com.example.bookshifter.dto.MinimalGameInfo;
import org.springframework.http.ResponseEntity;

import java.util.List;

public interface GameService {
    ResponseEntity<GameInfo> findById(Long id);

    List<MinimalGameInfo> findAll();

    GameInfo addGame(GameInfo dto);

    ResponseEntity<GameInfo> deleteGame(Long id);


}
