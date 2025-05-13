-- 1. הוספת אילוץ CHECK לטבלת crew לוודא שתפקיד לא ריק
ALTER TABLE crew
ADD CONSTRAINT chk_role_not_empty CHECK (role <> '');

-- 2. הוספת DEFAULT לתאריך רכישה של ציוד
ALTER TABLE equipment
ALTER COLUMN purchase_date SET DEFAULT CURRENT_DATE;

-- 3. הוספת NOT NULL ל-capacity בתשתיות
ALTER TABLE infrastructure
ALTER COLUMN capacity SET NOT NULL;
