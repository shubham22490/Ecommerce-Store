-- code for product category
-- Populate `Product Category` table
INSERT INTO `mydb`.`Product_Category` (`Name`)
VALUES
('Electronics'),
('Clothing'),
('Books'),
('Furniture'),
('Toys'),
('Home Appliances'),
('Beauty'),
('Sports'),
('Jewelry'),
('Accessories');

-- code for product
INSERT INTO `mydb`.`Product` (`ID`, `Quantity`, `Name`,
`Price`, `Product_Category_id`) VALUES
(1, 100, 'Smartphone', 500, 1),
(2, 50, 'T-shirt', 20, 2),
(3, 20, 'Novel', 10, 3),
(4, 30, 'Sofa', 800, 4),
(5, 40, 'Action Figure', 15, 5),
(6, 60, 'Refrigerator', 12, 6),
(7, 25, 'Lipstick', 30, 7),
(8, 15, 'Football', 400, 8),
(9, 35, 'Necklace', 50, 9),
(10, 10, 'Watch', 100, 10);


-- code for brand
INSERT INTO `mydb`.`Brand` (`ID`, `Name`, `Pincode`)
VALUES
(1, 'Brand A', '11111'),
(2, 'Brand B', '22222'),
(3, 'Brand C', '33333'),
(4, 'Brand D', '44444'),
(5, 'Brand E', '55555'),
(6, 'Brand F', '66666'),
(7, 'Brand G', '77777'),
(8, 'Brand H', '88888'),
(9, 'Brand I', '99999'),
(10, 'Brand J', '00000');

-- code for subscription
INSERT INTO `mydb`.`Subscription` (`ID`, `Price`,
`Feature`, `Name`) VALUES
(1, 10, 'Basic', 'Basic Subscription'),
(2, 20, 'Premium', 'Premium Subscription'),
(3, 30, 'Pro', 'Pro Subscription'),
(4, 15, 'Standard', 'Standard Subscription'),
(5, 25, 'Gold', 'Gold Subscription'),
(6, 35, 'Enterprise', 'Enterprise Subscription'),
(7, 12, 'Starter', 'Starter Subscription'),
(8, 22, 'Silver', 'Silver Subscription'),
(9, 40, 'Ultimate', 'Ultimate Subscription'),
(10, 18, 'Plus', 'Plus Subscription');



-- Populate `Customer` table
INSERT INTO `mydb`.`Customer` (`Phone_Number`,`User Password`,`Email`, `Sex`, `DOB`, `Name`, `Subscription_ID`, `Age`) VALUES
('1234567890','haha1' ,'customer1@example.com', 'M',
'1990-01-01', 'John Doe', 1, '31'),
('9876543210', 'haha2','customer2@example.com', 'F',
'1995-05-05', 'Jane Smith', 2, '26'),
('1112223334', 'haha3','customer3@example.com', 'M',
'1985-12-12', 'Chris Johnson', 3, '36'),
('4445556667', 'haha4','customer4@example.com', 'F',
'1988-08-08', 'Emma Brown', 4, '33'),
('7778889991', 'haha5','customer5@example.com', 'M',
'1992-02-02', 'Michael Wilson', 5, '29'),
('2345678901', 'haha6','customer6@example.com', 'F',
'1993-03-03', 'Emily Taylor', 6, '28'),
('8901234567', 'haha7','customer7@example.com', 'M',
'1980-04-04', 'David Martinez', 7, '41'),
('3456789012', 'haha8','customer8@example.com', 'F',
'1975-07-07', 'Jessica Anderson', 8, '46'),
('9012345678', 'haha9','customer9@example.com', 'M',
'1970-06-06', 'Daniel Garcia', 9, '51'),
('4567890123', 'haha10','customer10@example.com', 'F',
'1965-09-09', 'Sophia Brown', 10, '56');






-- code for product category has brand
-- Populate `Product Category_has_Brand` table
INSERT INTO `mydb`.`Product_Category_has_Brand`
(`Product_Category_id`, `Brand_ID`) VALUES
(1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 1);

-- code for selects
INSERT INTO `mydb`.`Selects` (`Customer_Phone_Number`, `Product_ID`) VALUES
(1234567890, 1),
(9876543210, 2),
(1112223334, 3),
(4445556667, 4),
(7778889991, 5),
(2345678901, 6),
(8901234567, 7),
(3456789012, 8),
(9012345678, 9),
(4567890123, 10);

