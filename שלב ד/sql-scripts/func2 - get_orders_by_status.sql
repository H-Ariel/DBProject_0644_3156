-- 2. מחזירה REF CURSOR של כל ההזמנות בסטטוס מסוים
CREATE FUNCTION get_orders_by_status(status_input order_status) RETURNS refcursor AS $$
DECLARE
    cur refcursor := 'get_orders_by_status';
BEGIN
    OPEN cur FOR SELECT * FROM "RestOrder" WHERE "StatusO	" = status_input;
    RETURN cur;
END;
$$ LANGUAGE plpgsql;