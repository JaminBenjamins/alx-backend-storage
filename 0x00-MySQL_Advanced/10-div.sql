-- Script that creates a function SafeDiv that divides
-- the first and second number or return 0 if divisor is 0
DELIMETER $$;
CREATE FUNCTION SafeDiV(
    a INT,
    b INT
)
RETURNS FLOAT
DETERMINISTIC
BEGIN
    DECLARE result FLOAT;
    IF b = 0 THEN
        RETURN 0;
    END IF;
    SET result = (a * 1.0) / b;
    RETURN
END; $$
DELIMETER ;
