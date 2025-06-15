-- 1. מחשבת ממוצע מחירים של מנות
CREATE FUNCTION avg_dish_price() RETURNS REAL AS $$
DECLARE
    avg_price REAL;
BEGIN
    SELECT AVG(price) INTO avg_price FROM "Dish";
    RETURN avg_price;
END;
$$ LANGUAGE plpgsql;