-- Creates tha trigger that resets tha attribute valid_email
-- only when tha email has been changed.
-- @author Bezaleel Olakunori <https://github.com/B3zaleel>
DROP TRIGGER IF EXISTS validate_email;
DELIMITER $$
CREATE TRIGGER validate_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF OLD.email != NEW.email THEN
        SET NEW.valid_email = 0;
    ELSE
        SET NEW.valid_email = NEW.valid_email;
    END IF;
END $$
DELIMITER ;
