-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb`;
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET
utf8 ;
USE `mydb` ;
-- -----------------------------------------------------
-- Table `mydb`.`Subscription`
-- ---------------------------------------------------customeraddressaddress--
CREATE TABLE IF NOT EXISTS `mydb`.`Subscription` (
`ID` INT NOT NULL,
`Price` INT NOT NULL,
`Feature` VARCHAR(45) NULL,
`Name` VARCHAR(45) NOT NULL,
PRIMARY KEY (`ID`),
UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE,
UNIQUE INDEX `Name_UNIQUE` (`Name` ASC) VISIBLE)
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `mydb`.`Product Category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Product_Category` (
`id` INT NOT NULL AUTO_INCREMENT,
`Name` VARCHAR(45) NOT NULL,
PRIMARY KEY (`id`))
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `mydb`.`Product`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Product` (
`ID` INT NOT NULL,
`Quantity` INT NOT NULL,
`Name` VARCHAR(45) NOT NULL COMMENT '\n\n',
`Price` INT NOT NULL,
`Image` VARCHAR(45) NULL,
`Description` VARCHAR(45) NULL,
`Product_Category_id` INT NOT NULL,
PRIMARY KEY (`ID`, `Product_Category_id`),
INDEX `fk_Product_Product Category1_idx` (`Product_Category_id` ASC)
VISIBLE,
CONSTRAINT `fk_Product_Product Category1`
FOREIGN KEY (`Product_Category_id`)
REFERENCES `mydb`.`Product_Category` (`id`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `mydb`.`Customer`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Customer` (
`Phone_Number` VARCHAR(10) NOT NULL,
`User Password` VARCHAR(45) NOT NULL,
`Email` VARCHAR(45) NOT NULL,
`Sex` CHAR(1) BINARY NOT NULL,
`DOB` DATE NOT NULL,
`Name` VARCHAR(45),
`Subscription_ID` INT,
`Age` VARCHAR(45),
PRIMARY KEY (`Phone_Number`),
INDEX `fk_Customer_Subscription1_idx` (`Subscription_ID` ASC) VISIBLE,
CONSTRAINT `fk_Customer_Subscription1`
FOREIGN KEY (`Subscription_ID`)
REFERENCES `mydb`.`Subscription` (`ID`));
-- -----------------------------------------------------
-- Table `mydb`.`Cart`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Cart` (
`Cart_Id` INT NOT NULL AUTO_INCREMENT,
`Phone_Number` VARCHAR(10) NOT NULL,
`Quantity` INT UNSIGNED NOT NULL,
`Product_ID` INT NOT NULL,
PRIMARY KEY (`Cart_Id`),
INDEX `fk_Cart_Product1_idx` (`Product_ID` ASC) VISIBLE,
CONSTRAINT `fk_Cart_Product1`
    FOREIGN KEY (`Product_ID`)
    REFERENCES `mydb`.`Product` (`ID`),
CONSTRAINT `fk_Cart_Customer`
    FOREIGN KEY (`Phone_Number`)
    REFERENCES `mydb`.`Customer` (`Phone_Number`))
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `mydb`.`Address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Address` (
`House Number` INT NOT NULL,
`Street Name` VARCHAR(45) NULL,
`Pincode` VARCHAR(45) NULL,
`Country` VARCHAR(45) NULL,
`Customer_Phone_Number` VARCHAR(10) NOT NULL,
INDEX `fk_Address_Customer_idx` (`Customer_Phone_Number` ASC)
VISIBLE,
CONSTRAINT `fk_Address_Customer`
FOREIGN KEY (`Customer_Phone_Number`)
REFERENCES `mydb`.`Customer` (`Phone_Number`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `mydb`.`Selects`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Selects` (
`Customer_Phone_Number` VARCHAR(10) NOT NULL,
`Product_ID` INT NOT NULL,
PRIMARY KEY (`Customer_Phone_Number`, `Product_ID`),
INDEX `fk_Customer_has_Product_Product1_idx` (`Product_ID` ASC)
VISIBLE,
CONSTRAINT `fk_Customer_has_Product_Customer1`
FOREIGN KEY (`Customer_Phone_Number`)
REFERENCES `mydb`.`Customer` (`Phone_Number`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `fk_Customer_has_Product_Product1`
FOREIGN KEY (`Product_ID`)
REFERENCES `mydb`.`Product` (`ID`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `mydb`.`Brand`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `mydb`.`Brand` (
`ID` INT NOT NULL,
`Name` VARCHAR(45) NULL,
`Pincode` VARCHAR(45) NULL,
PRIMARY KEY (`ID`))
ENGINE = InnoDB;
-- -----------------------------------------------------
-- Table `mydb`.`Product Category_has_Brand`
-- -----------------------------------------------------
Create TABLE IF NOT EXISTS `mydb`.`trial_history`(
`ID` INT auto_increment,
`PHONE_NUMBER` VARCHAR(12) NOT NULL,
`Product_id` INT NOT NULL,
primary key(`ID`),
FOREIGN KEY (`Phone_Number`)
REFERENCES `mydb`.`Customer` (`Phone_Number`),
FOREIGN KEY (`Product_id`)
REFERENCES `mydb`.`Product` (`ID`))
engine=InnoDB;
Create TABLE IF NOT EXISTS `mydb`.`order_history`(
`ID` INT auto_increment,
`PHONE_NUMBER` VARCHAR(12) NOT NULL,
`Product_id` INT NOT NULL,
`Quantity` INT NOT NULL,
primary key(`ID`),
FOREIGN KEY (`Phone_Number`)
REFERENCES `mydb`.`Customer` (`Phone_Number`),
FOREIGN KEY (`Product_id`)
REFERENCES `mydb`.`Product` (`ID`))
engine=InnoDB;
CREATE TABLE IF NOT EXISTS `mydb`.`Product_Category_has_Brand` (
`Product_Category_id` INT NOT NULL,
`Brand_ID` INT NOT NULL,
PRIMARY KEY (`Product_Category_id`, `Brand_ID`),
INDEX `fk_Product_Category_has_Brand_Brand1_idx` (`Brand_ID` ASC)
VISIBLE,
INDEX `fk_Product_Category_has_Brand_Product Category1_idx`
(`Product_Category_id` ASC) VISIBLE,
CONSTRAINT `fk_Product_Category_has_Brand_Product Category1`
FOREIGN KEY (`Product_Category_id`)
REFERENCES `mydb`.`Product_Category` (`id`)
ON DELETE NO ACTION
ON UPDATE NO ACTION,
CONSTRAINT `fk_Product_Category_has_Brand_Brand1`
FOREIGN KEY (`Brand_ID`)
REFERENCES `mydb`.`Brand` (`ID`)
ON DELETE NO ACTION
ON UPDATE NO ACTION)
ENGINE = InnoDB;
