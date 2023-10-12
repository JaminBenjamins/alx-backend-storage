-- Script that creates an index on the 
-- table names and first letter of name and score.
CREATE INDEX idx_name_first_score on names(name(1), score)
