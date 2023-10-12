-- Script that creates a stored procedure call
-- that computes and stores students' average score
DROP procedure IF EXISTS ComputerAverageScoreForUser;
DELIMETER $$;
CREATE PROCEDURE ComputerAverageScoreForUser(
    IN user_id INT
)
BEGIN
    UPDATE users
    SET average_score=(SELECT AVG(score) FR0M corrections
        WHERE corrections.user_id=user_id)
    WHERE id=user_id;
END; $$
DELIMETER ;
