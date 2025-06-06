-- מציג פרטי הזמנה במסעדה כולל שם הלקוח, סטטוס ההזמנה, מלצר, ושיטת תשלום
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


-- כל ההזמנות ששולמו באשראי
SELECT * FROM View_Restaurant_Orders WHERE "Payment_Method" = 'CreditCard' LIMIT 10;

-- הזמנות מעל 100 ש"ח
SELECT * FROM View_Restaurant_Orders WHERE "Total_price" > 100 LIMIT 10;


-- מציג חוקרים לפי מושבות, כולל תחום מחקר, צוות ושם מושבה.
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

-- צוותים במושבות שהוקמו אחרי 2020
SELECT crew_name FROM View_Colony_Researchers WHERE established_date > '2020-01-01' LIMIT 10;

-- חוקרים במושבות שמתחילות ב-Ca
SELECT researcher_name FROM View_Colony_Researchers WHERE colony_name LIKE 'Ca%' LIMIT 10;
