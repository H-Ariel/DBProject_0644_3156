-- 2. מזמנת פונקציה עם REF CURSOR ופרוצדורה
-- מדפיסה מזהי הזמנות בסטטוס "Pending" ומעדכנת את כולן ל־Completed.
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

-- מה התוכנית עושה?
-- התוכנית שולפת את כל ההזמנות מתוך טבלת "RestOrder" שנמצאות במצב 'Pending' (ממתין), מדפיסה את מזהה כל הזמנה שנמצאה, ולאחר מכן מעדכנת את כל ההזמנות בטבלה למצב 'Completed' (הושלם).
