-- 1. עדכון סטטוס הזמנה
CREATE PROCEDURE update_order_status(order_id INT, new_status order_status) AS $$
BEGIN
    UPDATE "RestOrder" SET "StatusO	" = new_status WHERE "RestOrder_ID" = order_id;
END;
$$ LANGUAGE plpgsql;
