-- 1. טריגר לעדכון תאריך ברכישה חדשה
CREATE OR REPLACE FUNCTION set_payment_date() RETURNS trigger AS $$
BEGIN
    NEW."Payment_Date" := CURRENT_DATE;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trg_set_payment_date
BEFORE INSERT ON "Payment"
FOR EACH ROW EXECUTE FUNCTION set_payment_date();
