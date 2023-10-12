-- Script that creates a trigger that resets the attribute
-- valid_email only when it has changed.
DELIMETER $$ ;
CREATE TRIGGER validate BEFORE UPDATE ON users 
FOR REACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;$$
DELIMETER;
