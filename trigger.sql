DELIMITER $$

CREATE TRIGGER UpdateAllAgesAfterInsert
AFTER INSERT ON Customer
FOR EACH ROW
BEGIN
    -- Updating age for all customers based on their DOB
    UPDATE Customer
    SET Age = TIMESTAMPDIFF(YEAR, DOB, CURDATE());
END$$

DELIMITER ;


 DELIMITER $$


-- trigger updates the quantity of the item 
CREATE TRIGGER AfterPurchaseUpdateQuantity
AFTER INSERT ON mydb.order_history
FOR EACH ROW
BEGIN
  UPDATE mydb.Product
  SET Quantity = Quantity - NEW.Quantity
  WHERE ID = NEW.Product_id;
END$$

DELIMITER ;

-- trigger checks the quantity available before placing order
DELIMITER $$

CREATE TRIGGER BeforeAddToCart
BEFORE INSERT ON mydb.order_history
FOR EACH ROW
BEGIN
  DECLARE available_quantity INT;
  SELECT Quantity INTO available_quantity FROM mydb.Product WHERE ID = NEW.Product_ID;
  IF available_quantity < NEW.Quantity THEN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Insufficient stock for the requested product.';
  END IF;
END$$

DELIMITER ;


-- trigger removes the data of a customer

DELIMITER $$

CREATE TRIGGER CleanupAfterCustomerDeletion
AFTER DELETE ON mydb.Customer
FOR EACH ROW
BEGIN
  DELETE FROM mydb.Cart WHERE Phone_Number = OLD.Phone_Number;
  DELETE FROM mydb.Address WHERE Customer_Phone_Number = OLD.Phone_Number;
  DELETE FROM mydb.Selects WHERE Customer_Phone_Number = OLD.Phone_Number;
END$$

DELIMITER ;
