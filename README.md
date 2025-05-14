# DBProject_0644_3156
## מערכת ניהול מושבות בחלל

**שמות המגישים:** אריאל חלילי וארבל פאר  
**יחידה נבחרת:** אנשי צוות  

---
## תוכן עניינים
1. [מבוא](#מבוא)
3. [תרשים ERD](#תרשים-erd)
4. [תרשים DSD](#תרשים-dsd)
5. [שיטות להכנסת הנתונים](#שיטות-להכנסת-הנתונים)
6. [צילום מסך גיבוי הנתונים](#צילום-מסך-גיבוי-הנתונים)
7. [צילום מסך של שחזור הנתונים ממחשב אחר](#צילום-מסך-של-שחזור-הנתונים-ממחשב-אחר)

---
## מבוא

המערכת מיועדת לניהול מידע אודות מושבות חלליות. הנתונים הנשמרים כוללים מידע על כל חללית, המשימות שלה, הציוד בו נעשה שימוש במשימה, ואנשי הצוות המאכלסים את החללית. הפונקציונליות המרכזית מאפשרת הוספת חללית חדשה, בניית צוות מסודר עם תפקידים מוגדרים לכל איש צוות.

---
# שלב 1 - עיצוב ובניית בסיס הנתונים

## תרשים ERD
![image](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%90/ERDAndDSTFiles/ERD.png?raw=true)

---
## תרשים DSD
![image](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%90/ERDAndDSTFiles/DSD.png?raw=true)

---
## שיטות להכנסת הנתונים

### יצירת נתונים באופן אוטומטי
![generatedata](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%90/screenshots/generatedata.jpg?raw=true)

### ייבוא נתונים מקובץ CSV
![import-from-csv](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%90/screenshots/import-from-csv.jpg?raw=true)

### הכנסת נתונים באמצעות סקריפט פייתון
📜 **[python script](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%90/programing/init-script.py)**

### הכנסת נתונים באמצעות סקריפט SQL
📜 **[sql script](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%90/DataImportFiles/insert_Crew.sql)**

---
## צילום מסך גיבוי הנתונים
![backup](https://github.com/user-attachments/assets/f35b84fc-30e0-47f5-a0c6-b001a4fcc011)

---
## צילום מסך של שחזור הנתונים ממחשב אחר
![restore](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%90/screenshots/restore.jpg?raw=true)

---

# שלב 2 - שאילתות SQL

## 1. שמות החוקרים, תחום מחקר, ותאריך הצטרפות של הצוותים המתאימים להם
```sql
SELECT
	R.NAME,
	R.RESEARCH_FIELD,
	C.NAME AS CREW_NAME,
	C.JOINED_DATE
FROM
	RESEARCHER R
	JOIN CREW C ON R.CREW_ID = C.CREW_ID;
```

![select 1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/select-1.jpg?raw=true)

## 2. שמות הצוותים, מספר המיכשור ששויך לכל צוות
```sql
SELECT
	C.NAME AS CREW_NAME,
	COUNT(U.EQUIPMENT_ID) AS EQUIPMENT_COUNT
FROM
	CREW C
	LEFT JOIN USES U ON C.CREW_ID = U.MISSION_ID
GROUP BY
	C.NAME;
```

![select 2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/select-2.jpg?raw=true)

## 3. ציוד שמולא ביותר מ-3 משימות
```sql
SELECT
	E.NAME AS EQUIPMENT_NAME,
	COUNT(U.MISSION_ID) AS MISSION_COUNT
FROM
	EQUIPMENT E
	JOIN USES U ON E.EQUIPMENT_ID = U.EQUIPMENT_ID
GROUP BY
	E.NAME
HAVING
	COUNT(U.MISSION_ID) > 3;
```

![select 3](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/select-3.jpg?raw=true)

## 4. שמות המושבות שהוקמו לפני 2010 ושטח הציוד שנרכש לכל אחת
```sql
SELECT
	COL.NAME,
	SUM(CURRENT_DATE - E.PURCHASE_DATE) AS TOTAL_EQUIPMENT_AGE -- מחשב את ההפרש בימים בין תאריך רכישת הציוד לתאריך הנוכחי
FROM
	COLONY COL
	JOIN MISSION M ON COL.COLONY_ID = M.COLONY_ID
	JOIN USES U ON M.MISSION_ID = U.MISSION_ID
	JOIN EQUIPMENT E ON U.EQUIPMENT_ID = E.EQUIPMENT_ID
WHERE
	COL.ESTABLISHED_DATE < '2010-01-01'
GROUP BY
	COL.NAME;
```
![select 4](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/select-4.jpg?raw=true)

## 5. חוקרים בתפקיד ספציפי וצוותים שצורפו אליהם

```sql
SELECT
	R.NAME AS RESEARCHER_NAME,
	C.NAME AS CREW_NAME,
	C.ROLE
FROM
	RESEARCHER R
	JOIN CREW C ON R.CREW_ID = C.CREW_ID
WHERE
	C.ROLE = 'Engineer';
```

![select 5](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/select-5.jpg?raw=true)

## 6. מספר חוקרים שנמצאים בכל צוות
```sql
SELECT
	C.NAME AS CREW_NAME,
	COUNT(R.RESEARCHER_ID) AS RESEARCHER_COUNT
FROM
	CREW C
	LEFT JOIN RESEARCHER R ON C.CREW_ID = R.CREW_ID
GROUP BY
	C.NAME;
```

![select 6](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/select-6.jpg?raw=true)

## 7. פרטי המיכשור שנרכש לאחר 2015
```sql
SELECT
	E.NAME,
	E.PURCHASE_DATE
FROM
	EQUIPMENT E
WHERE
	E.PURCHASE_DATE > '2015-01-01';
```

![select 7](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/select-7.jpg?raw=true)

## 8. מידע על הצוותים והמשימות שלהם ב-2019

```sql
SELECT
	C.NAME AS CREW_NAME,
	M.NAME AS MISSION_NAME,
	M.START_DATE
FROM
	CREW C
	JOIN MISSION M ON C.COLONY_ID = M.COLONY_ID
WHERE
	EXTRACT(
		YEAR
		FROM
			M.START_DATE
	) = 2019;
```

![select 8](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/select-8.jpg?raw=true)
