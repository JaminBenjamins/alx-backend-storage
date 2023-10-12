-- Script that creates a view that lists all students
-- that have a score under 80 and no last_meeting more than a month
CREATE VIEW need_meeting AS SELECT name FROM students WHERE score < 80
AND (last_meeting IS NULL OR last_meeting < DATE(CURDATE() - INTERVAL 1 MONTH));
