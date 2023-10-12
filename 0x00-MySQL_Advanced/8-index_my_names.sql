-- Script that createss an index 
-- on a table nme and finds first letter of name
CREATE INDEX idx_name_first ON names(name(1))
