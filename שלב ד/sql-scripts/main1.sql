-- 1. מזמנת פונקציה ופרוצדורה
-- מחשבת ממוצע מחירים ומעדכנת סטטוס להזמנה
DO $$
DECLARE
    avg_price REAL;
BEGIN
    avg_price := avg_dish_price();
    CALL update_order_status(1, 'Confirmed');
END;
$$;

-- מה התוכנית עושה?
-- התוכנית מחשבת את המחיר הממוצע של מנות (dishes) על ידי קריאה לפונקציה, ולאחר מכן מעדכנת את הסטטוס של הזמנה ספציפית (עם מזהה 1) ל'Confirmed' (אושר).
