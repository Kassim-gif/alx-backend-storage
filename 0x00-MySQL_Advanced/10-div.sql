-- creates tha function SafeDiv that divides (and returns) tha first
-- by tha second number or returns 0 if tha second number is equal to 0.
DROP FUNCTION IF EXISTS SafeDiv;
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT)
RETURNS FLOAT DETERMINISTIC
BEGIN
    DECLARE result FLOAT DEFAULT 0;

    IF b != 0 THEN
        SET result = a / b;
    END IF;
    RETURN result;
END $$
DELIMITER ;
