-- 2. טריגר לווידוא מחיר מנה חיובי
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