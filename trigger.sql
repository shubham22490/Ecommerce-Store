DELIMITER $$

CREATE TRIGGER after_product_update
AFTER UPDATE ON product
FOR EACH ROW
BEGIN
    IF NEW.Quantity = 0 THEN
        DELETE FROM product WHERE ID = NEW.ID;
    END IF;
END$$

DELIMITER ;

DELIMITER $$

CREATE TRIGGER increment_cart_quantity
AFTER INSERT ON Cart
FOR EACH ROW
BEGIN
    UPDATE Customer
    SET Cart_quantity = Cart_quantity + NEW.Quantity
    WHERE Cart_Id = NEW.Cart_Id;
END$$

DELIMITER ;


DELIMITER $$

CREATE TRIGGER decrement_cart_quantity
AFTER DELETE ON Cart
FOR EACH ROW
BEGIN
    UPDATE Customer
    SET Cart_quantity = Cart_quantity - OLD.Quantity
    WHERE Cart_Id = OLD.Cart_Id;
END$$

DELIMITER ;



