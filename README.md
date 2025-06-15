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
  
	2.4 [צילום מסך של גיבוי](#צילום-מסך-גיבוי-הנתונים)
 
	2.5 [צילום מסך של שחזור](#צילום-מסך-של-שחזור-הנתונים-ממחשב-אחר)
 
3. [שלב 2 - שאילתות SQL](#שלב-2---שאילתות-sql)

	3.1 [שאילתות SELECT](#שאילתות-select)
  
	3.2 [שאילתות UPDATE](#שאילתות-update)
  
	3.3 [שאילתות DELETE](#שאילתות-delete)

   	3.4 [אילוצים](#אילוצים)

	3.5 [COMMIT](#COMMIT)

   	3.6 [ROLLBACK](#ROLLBACK)

4. [שלב 3 - אינטגרציה](#שלב-3---אינטגרציה)

5. [שלב 4 - פונקציות](#שלב-4---פונקציות)



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

---

## אילוצים

### 1. הוספת אילוץ CHECK לטבלת crew לוודא שתפקיד לא ריק

```sql
ALTER TABLE crew ADD CONSTRAINT chk_role_not_empty CHECK (role <> '');
```
![constraint-1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/constraint-1.jpg?raw=true) - *constraint 1*

### 2. הוספת DEFAULT לתאריך רכישה של ציוד

```sql
ALTER TABLE equipment ALTER COLUMN purchase_date SET DEFAULT CURRENT_DATE;
```
![constraint-2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/constraint-2.jpg?raw=true) - *constraint 2*

### 3. הוספת NOT NULL ל-capacity בתשתיות

```sql
ALTER TABLE infrastructure ALTER COLUMN capacity SET NOT NULL;
```
![constraint-3](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/constraint-3.jpg?raw=true) - *constraint 3*

---

## COMMIT

```sql
BEGIN;
UPDATE Crew SET role = 'Banana' WHERE crew_id = 1;
COMMIT;
```
![commit](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/commit.jpg?raw=true) - *after commit*

## ROLLBACK

```sql
BEGIN;
UPDATE Crew SET role = 'Banana' WHERE crew_id = 1;
ROLLBACK;
```
![rollback](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%91/screenshots/rollback.jpg?raw=true) - *after rollback*


---

# שלב 3 - אינטגרציה

את האינטגרציה ביצענו עם מאור וארי. בשלב הזה ביצענו אינטגרציה עם מערכת לניהול מסעדה. החלטנו לשלב את המערכות שלנו ע"י יצירת טבלה חדשה People בה כל חוקר הוא גם מלצר בשעות הערב במושבה בה הוא עובד. מכיוון שהחוקרים רוצים להפריד ביןחיי המחקר לחיי המלצרות שלהם הם נכנסו למערכת עם שם שונה בין כל עבודה ועם ת"ז שונה, אבל אנחנו מכירים אותם ורוצים לעזור להם לנהל את הזמן טוב יותר ולכן יש לנו טבלה בה שמור הת"ז של כל אחד בכל עבודה. התרשימים הבאים מציגים את המערכת שקיבלנו ואת המערכת המשולבת:

## תרשימים

### תרשים ה-ERD שקיבלנו
![theirERD](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%92/ERDAndDSTFiles/theirERD.jpg?raw=true)

### תרשים ה-DSD שקיבלנו
![theirDSD](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%92/ERDAndDSTFiles/theirDSD.jpg?raw=true)

### תרשים ה-ERD המשולב
![integratedERD](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%92/ERDAndDSTFiles/integratedERD.png?raw=true)

### תרשים ה-DSD המשולב
![integratedDSD](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%92/ERDAndDSTFiles/integratedDSD.png?raw=true)


## מבטים

### 1. מציג פרטי הזמנה במסעדה כולל שם הלקוח, סטטוס ההזמנה, מלצר, ושיטת תשלום

``` sql
CREATE OR REPLACE VIEW View_Restaurant_Orders AS
SELECT
    r."RestOrder_ID",
    r."RestOrder_DateTime",
    c."Full_Name" AS customer_name,
    w."Full_Name" AS waiter_name,
    r."Total_price",
    r."StatusO	" AS order_status,
    p."Payment_Method",
    p."Payment_Status"
FROM "RestOrder" r
JOIN "Customer" c ON r."Customer_ID" = c."Customer_ID"
LEFT JOIN "Waiter" w ON r."Waiter_ID" = w."Waiter_ID"
JOIN "Payment" p ON r."Payment_ID" = p."Payment_ID";
```

#### שאילתא 1 - כל ההזמנות ששולמו באשראי

```sql
SELECT * FROM View_Restaurant_Orders WHERE "Payment_Method" = 'CreditCard' LIMIT 10;
```
![query1.1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%92/screenshots/query1.1.jpg?raw=true)

#### שאילתא 2 - הזמנות מעל 100 ש"ח

```sql
SELECT * FROM View_Restaurant_Orders WHERE "Total_price" > 100 LIMIT 10;
```
![query1.2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%92/screenshots/query1.2.jpg?raw=true)


### 2. מציג חוקרים לפי מושבות, כולל תחום מחקר, צוות ושם מושבה.
```sql
CREATE OR REPLACE VIEW View_Colony_Researchers AS
SELECT
    r.researcher_id,
    r.name AS researcher_name,
    r.research_field,
    c.name AS crew_name,
    col.name AS colony_name,
    col.established_date
FROM researcher r
JOIN crew c ON r.crew_id = c.crew_id
JOIN colony col ON c.colony_id = col.colony_id;
```

#### שאילתא 1 - צוותים במושבות שהוקמו אחרי 2020

```sql
SELECT crew_name FROM View_Colony_Researchers WHERE established_date > '2020-01-01' LIMIT 10;
```
![query2.1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%92/screenshots/query2.1.jpg?raw=true)

#### שאילתא 2 - חוקרים במושבות שמתחילות ב-Ca

```sql
SELECT researcher_name FROM View_Colony_Researchers WHERE colony_name LIKE 'Ca%' LIMIT 10;
```
![query2.2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%92/screenshots/query2.2.jpg?raw=true)

---

# שלב 4 - פונקציות

## פונקציה 1 - מחשבת ממוצע מחירים של מנות
```sql
CREATE FUNCTION avg_dish_price() RETURNS REAL AS $$
DECLARE
    avg_price REAL;
BEGIN
    SELECT AVG(price) INTO avg_price FROM "Dish";
    RETURN avg_price;
END;
$$ LANGUAGE plpgsql;
```

## פונקציה 2 - מחזירה REF CURSOR של כל ההזמנות בסטטוס מסוים
```sql
CREATE FUNCTION get_orders_by_status(status_input order_status) RETURNS refcursor AS $$
DECLARE
    cur refcursor := 'get_orders_by_status';
BEGIN
    OPEN cur FOR SELECT * FROM "RestOrder" WHERE "StatusO	" = status_input;
    RETURN cur;
END;
$$ LANGUAGE plpgsql;
```

## פרוצדורה 1 - עדכון סטטוס הזמנה
```sql
CREATE PROCEDURE update_order_status(order_id INT, new_status order_status) AS $$
BEGIN
    UPDATE "RestOrder" SET "StatusO	" = new_status WHERE "RestOrder_ID" = order_id;
END;
$$ LANGUAGE plpgsql;
```

## פרוצדורה 2 - פרוצדורה עם CURSOR, לולאה ו-EXCEPTION
```sql
CREATE PROCEDURE update_all_orders_to_completed() AS $$
DECLARE
    r RECORD;
    cur CURSOR FOR SELECT "RestOrder_ID" FROM "RestOrder" WHERE "StatusO	" != 'Completed';
BEGIN
    OPEN cur;
    LOOP
        FETCH cur INTO r;
        EXIT WHEN NOT FOUND;
        BEGIN
            UPDATE "RestOrder" SET "StatusO	" = 'Completed' WHERE "RestOrder_ID" = r."RestOrder_ID";
        EXCEPTION WHEN OTHERS THEN
            RAISE NOTICE 'שגיאה בהזמנה %', r."RestOrder_ID";
        END;
    END LOOP;
    CLOSE cur;
END;
$$ LANGUAGE plpgsql;
```

## טריגר 1 - טריגר לעדכון תאריך ברכישה חדשה
```sql
CREATE OR REPLACE FUNCTION set_payment_date() RETURNS trigger AS $$
BEGIN
    NEW."Payment_Date" := CURRENT_DATE;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_set_payment_date
BEFORE INSERT ON "Payment"
FOR EACH ROW EXECUTE FUNCTION set_payment_date();
```

## טריגר 2 - טריגר לווידוא מחיר מנה חיובי
```sql
CREATE OR REPLACE FUNCTION check_dish_price() RETURNS trigger AS $$
BEGIN
    IF NEW.price <= 0 THEN
        RAISE EXCEPTION 'מחיר לא תקין!';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_check_dish_price
BEFORE INSERT OR UPDATE ON "Dish"
FOR EACH ROW EXECUTE FUNCTION check_dish_price();
```

## תוכנית 1 - מזמנת פונקציה ופרוצדורה - מחשבת ממוצע מחירים ומעדכנת סטטוס להזמנה

### מה התוכנית עושה?

התוכנית מחשבת את המחיר הממוצע של מנות (dishes) על ידי קריאה לפונקציה, ולאחר מכן מעדכנת את הסטטוס של הזמנה ספציפית (עם מזהה 1) ל'Confirmed' (אושר).

```sql
DO $$
DECLARE
    avg_price REAL;
BEGIN
    avg_price := avg_dish_price();
    CALL update_order_status(1, 'Confirmed');
END;
$$;
```

![run-main-1](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%93/screenshots/run-main1.jpg?raw=true)

## תוכנית 2 - מזמנת פונקציה עם REF CURSOR ופרוצדורה - מדפיסה מזהי הזמנות בסטטוס "Pending" ומעדכנת את כולן ל־Completed.

### מה התוכנית עושה?

התוכנית שולפת את כל ההזמנות מתוך טבלת "RestOrder" שנמצאות במצב 'Pending' (ממתין), מדפיסה את מזהה כל הזמנה שנמצאה, ולאחר מכן מעדכנת את כל ההזמנות בטבלה למצב 'Completed' (הושלם).

```sql
DO $$
DECLARE
    cur refcursor;
    row "RestOrder"%ROWTYPE;
BEGIN
    cur := get_orders_by_status('Pending');
    LOOP
        FETCH cur INTO row;
        EXIT WHEN NOT FOUND;
        RAISE NOTICE 'הזמנה: %', row."RestOrder_ID";
    END LOOP;
    CALL update_all_orders_to_completed();
END;
$$;

```

![run-main-2](https://github.com/H-Ariel/DBProject_0644_3156/blob/main/%D7%A9%D7%9C%D7%91%20%D7%93/screenshots/run-main2.jpg?raw=true)

