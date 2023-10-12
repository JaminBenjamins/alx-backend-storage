-- SQL scripts that create a stored procedure ComputeAverageWeightedScoreForUser
-- That computes and stores the average weighted score for a student

DROP procedure IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMETER | 
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (
    IN user_id INT
)
BEGIN
    UPDATE users
    SET average_score=(SELECT AVG(score) FROM corrections
                        WHERE corrections.user_id=user_id)
    WHERE id=user_id;
END;
|
