BEGIN;
UPDATE Crew SET role = 'Banana' WHERE crew_id = 1;
-- לשמור את השינויים או לא
--COMMIT;
ROLLBACK;

-- לבדוק את המצב
SELECT * FROM Crew WHERE crew_id = 1;
