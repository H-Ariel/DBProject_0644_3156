-- 1. עדכון תאריך הצטרפות של צוותים שהצטרפו לפני 2015
UPDATE CREW
SET JOINED_DATE = '2015-01-01'
WHERE JOINED_DATE < '2015-01-01';

-- 2. עדכון סטטוס של תשתיות למושבות שפרסמו משימות לאחר 2020
UPDATE INFRASTRUCTURE I
SET STATUS = 1
WHERE
	EXISTS (
		SELECT 1
		FROM COLONY C
			JOIN MISSION M ON C.COLONY_ID = M.COLONY_ID
		WHERE I.COLONY_ID = C.COLONY_ID
			AND M.START_DATE > '2020-01-01'
	);

-- 3. עדכון תפקידים של חוקרים לפי תחום מחקר
UPDATE CREW C
SET ROLE = 'Research Lead'
WHERE
	EXISTS (
		SELECT 1
		FROM RESEARCHER R
		WHERE R.CREW_ID = C.CREW_ID
			AND R.RESEARCH_FIELD = 'Elit LLC'
	);