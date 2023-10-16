package com.example.bookshifter.repositories;

import com.example.bookshifter.entities.Game;
import com.example.bookshifter.projections.GameMinProjection;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import java.util.List;

public interface GameRepository extends JpaRepository<Game, Long> {
	@Query(nativeQuery = true, value = """
		SELECT tb_game.id, tb_game.title, tb_game.game_year AS gameYear, tb_game.image_url AS imageUrl,
		tb_game.short_description AS shortDescription, tb_belonging.position
		FROM tb_game
		INNER JOIN tb_belonging ON tb_game.id = tb_belonging.game_id
		WHERE tb_belonging.game_list_id = :listId
		ORDER BY tb_belonging.position
			""")
	List<GameMinProjection> searchByList(Long listId);
}