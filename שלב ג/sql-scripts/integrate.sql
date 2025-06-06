CREATE TABLE People (
    researcher_id INT PRIMARY KEY,
    waiter_id INT UNIQUE,
    FOREIGN KEY (researcher_id) REFERENCES researcher(researcher_id),
    FOREIGN KEY (waiter_id) REFERENCES "Waiter"("Waiter_ID")
);

INSERT INTO People (researcher_id, waiter_id)
SELECT r.researcher_id, w."Waiter_ID"
FROM (
    SELECT researcher_id, ROW_NUMBER() OVER (ORDER BY researcher_id) AS rn FROM researcher
) r
JOIN (
    SELECT "Waiter"."Waiter_ID", ROW_NUMBER() OVER (ORDER BY "Waiter"."Waiter_ID") AS rn FROM "Waiter"
) w ON r.rn = w.rn
WHERE r.rn <= 300;