-- 2. פרוצדורה עם CURSOR, לולאה ו-EXCEPTION
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