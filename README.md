# DBProject_0644_3156
## מערכת ניהול מושבות בחלל

**שמות המגישים:** אריאל חלילי וארבל פאר  
**יחידה נבחרת:** אנשי צוות  

---
## תוכן עניינים
1. [מבוא](#מבוא)  
2. [שלב 1 - עיצוב ובניית בסיס הנתונים](#שלב-1---עיצוב-ובניית-בסיס-הנתונים)  
 2.1 [תרשים ERD](#תרשים-erd)  
 2.2 [תרשים DSD](#תרשים-dsd)  
 2.3 [שיטות להכנסת הנתונים](#שיטות-להכנסת-הנתונים)  
  2.3.1 [יצירת נתונים אוטומטית](#יצירת-נתונים-באופן-אוטומטי)  
  2.3.2 [ייבוא מקובץ CSV](#ייבוא-נתונים-מקובץ-csv)  
  2.3.3 [הכנסת נתונים עם פייתון](#הכנסת-נתונים-באמצעות-סקריפט-פייתון)  
  2.3.4 [הכנסת נתונים עם SQL](#הכנסת-נתונים-באמצעות-סקריפט-sql)  
 2.4 [צילום מסך של גיבוי](#צילום-מסך-גיבוי-הנתונים)  
 2.5 [צילום מסך של שחזור](#צילום-מסך-של-שחזור-הנתונים-ממחשב-אחר)  

3. [שלב 2 - שאילתות SQL](#שלב-2---שאילתות-sql)  
 3.1 [שאילתות SELECT](#שאילתות-select)  
  3.1.1 [חוקרים ותחום מחקר](#1-שמות-החוקרים-תחום-מחקר-ותאריך-הצטרפות-של-הצוותים-המתאימים-להם)  
  3.1.2 [צוותים וציוד](#2-שמות-הצוותים-מספר-המיכשור-ששויך-לכל-צוות)  
  3.1.3 [ציוד ב־3+ משימות](#3-ציוד-שמולא-ביותר-מ-3-משימות)  
  3.1.4 [מושבות וציוד לפני 2010](#4-שמות-המושבות-שהוקמו-לפני-2010-ושטחו-הציוד-שנרכש-לכל-אחת)  
  3.1.5 [חוקרים בתפקיד](#5-חוקרים-בתפקיד-ספציפי-וצוותים-שצורפו-אליהם)  
  3.1.6 [מספר חוקרים בצוות](#6-מספר-חוקרים-שנמצאים-בכל-צוות)  
  3.1.7 [ציוד אחרי 2015](#7-פרטי-המיכשור-שנרכש-לאחר-2015)  
  3.1.8 [צוותים ומשימות ב־2019](#8-מידע-על-הצוותים-והמשימות-שלהם-ב-2019)  
 3.2 [שאילתות UPDATE](#שאילתות-update)  
  3.2.1 [עדכון תאריכי הצטרפות](#1-עדכון-תאריך-הצטרפות-של-צוותים-שהצטרפו-לפני-2015)  
  3.2.2 [עדכון סטטוס תשתיות](#2-עדכון-סטטוס-של-תשתיות-למושבות-שפרסמו-משימות-לאחר-2020)  
  3.2.3 [עדכון תפקיד לפי תחום](#3-עדכון-תפקידים-של-חוקרים-לפי-תחום-מחקר)  
 3.3 [שאילתות DELETE](#שאילתות-delete)  
  3.3.1 [מחיקת ציוד ב־2+ משימות](#1-מחיקת-שימוש-בציוד-ששויך-לפחות-ל-2-משימות)  
  3.3.2 [מחיקת חוקרים ממשימות אחרי 2020](#2-מחיקת-חוקרים-שנמצאים-בצוותים-שמבצעים-משימות-אחרי-2020)  
  3.3.3 [מחיקת תשתיות לא פעילות](#3-מחיקת-תשתיות-לא-פעילות-מכל-המושבות)  


---
## מבוא

המערכת מיועדת לניהול מידע אודות מושבות חלליות. הנתונים הנשמרים כוללים מידע על כל חללית, המשימות שלה, הציוד בו נעשה שימוש במשימה, ואנשי הצוות המאכלסים את החללית. הפונקציונליות המרכזית מאפשרת הוספת חללית חדשה, בניית צוות מסודר עם תפקידים מוגדרים לכל איש צוות.

---
# שלב 1 - עיצוב ובניית בסיס הנתונים

## תרשים ERD
![image](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%90/ERDAndDSTFiles/ERD.png?raw=true)

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

## שאילתות SELECT

### 1. שמות החוקרים, תחום מחקר, ותאריך הצטרפות של הצוותים המתאימים להם
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

### 2. שמות הצוותים, מספר המיכשור ששויך לכל צוות
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

### 3. ציוד שמולא ביותר מ-3 משימות
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

### 4. שמות המושבות שהוקמו לפני 2010 ושטח הציוד שנרכש לכל אחת
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

### 5. חוקרים בתפקיד ספציפי וצוותים שצורפו אליהם
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

### 6. מספר חוקרים שנמצאים בכל צוות
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

### 7. פרטי המיכשור שנרכש לאחר 2015
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

### 8. מידע על הצוותים והמשימות שלהם ב-2019
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

---

## שאילתות UPDATE

### 1. עדכון תאריך הצטרפות של צוותים שהצטרפו לפני 2015

```sql
UPDATE CREW
SET JOINED_DATE = '2015-01-01'
WHERE JOINED_DATE < '2015-01-01';
```
![before update 1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/before-update-1.jpg?raw=true) - *before update 1*
![after update 1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/after-update-1.jpg?raw=true) - *after update 1*


### 2. עדכון סטטוס של תשתיות למושבות שפרסמו משימות לאחר 2020

```sql
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
```
![before update 2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/before-update-2.jpg?raw=true) - *before update 2*
![after update 2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/after-update-2.jpg?raw=true) - *after update 2*


### 3. עדכון תפקידים של חוקרים לפי תחום מחקר

```sql
UPDATE CREW C
SET ROLE = 'Research Lead'
WHERE
	EXISTS (
		SELECT 1
		FROM RESEARCHER R
		WHERE R.CREW_ID = C.CREW_ID
			AND R.RESEARCH_FIELD = 'Elit LLC'
	);
```
![before update 3](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/before-update-3.jpg?raw=true) - *before update 3*
![after update 3](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/after-update-3.jpg?raw=true) - *after update 3*

---

## שאילתות DELETE

### 1. מחיקת שימוש בציוד ששויך לפחות ל-2 משימות

```sql
DELETE FROM USES
WHERE
	EQUIPMENT_ID IN (
		SELECT E.EQUIPMENT_ID
		FROM EQUIPMENT E
			JOIN USES U ON E.EQUIPMENT_ID = U.EQUIPMENT_ID
		GROUP BY E.EQUIPMENT_ID
		HAVING COUNT(U.MISSION_ID) >= 2
	);
```
![before delete 1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/before-delete-1.jpg?raw=true) - *before delete 1*
![after delete 1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/after-delete-1.jpg?raw=true) - *after delete 1*

### 2. מחיקת חוקרים שנמצאים בצוותים שמבצעים משימות אחרי 2020

```sql
DELETE FROM RESEARCHER
WHERE
	CREW_ID IN (
		SELECT C.CREW_ID
		FROM CREW C
			JOIN MISSION M ON C.COLONY_ID = M.COLONY_ID
		WHERE M.START_DATE > '2020-01-01'
	);
```
![before delete 2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/before-delete-2.jpg?raw=true) - *before delete 2*
![after delete 2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/after-delete-2.jpg?raw=true) - *after delete 2*

### 3. מחיקת תשתיות לא פעילות מכל המושבות

```sql
DELETE FROM INFRASTRUCTURE I WHERE I.STATUS = 2;
```
![before delete 3](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/before-delete-3.jpg?raw=true) - *before delete 3*
![after delete 3](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/after-delete-3.jpg?raw=true) - *after delete 3*
