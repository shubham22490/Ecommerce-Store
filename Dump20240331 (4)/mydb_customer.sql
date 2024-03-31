-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: mydb
-- ------------------------------------------------------
-- Server version	8.0.36

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `customer`
--

DROP TABLE IF EXISTS `customer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customer` (
  `Phone_Number` varchar(10) NOT NULL,
  `User Password` varchar(45) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Sex` char(1) CHARACTER SET utf8mb3 COLLATE utf8mb3_bin NOT NULL,
  `DOB` date NOT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Subscription_ID` int NOT NULL,
  `Age` varchar(45) DEFAULT NULL,
  `Cart_quantity` int NOT NULL,
  `Cart_Id` int NOT NULL,
  PRIMARY KEY (`Phone_Number`,`Cart_Id`),
  KEY `fk_Customer_Subscription1_idx` (`Subscription_ID`),
  KEY `fk_Customer_Cart1_idx` (`Cart_Id`),
  CONSTRAINT `fk_Customer_Cart1` FOREIGN KEY (`Cart_Id`) REFERENCES `cart` (`Cart_Id`),
  CONSTRAINT `fk_Customer_Subscription1` FOREIGN KEY (`Subscription_ID`) REFERENCES `subscription` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customer`
--

LOCK TABLES `customer` WRITE;
/*!40000 ALTER TABLE `customer` DISABLE KEYS */;
INSERT INTO `customer` VALUES ('1112223334','haha3','customer3@example.com','M','1985-12-12','Chris Johnson',3,'36',1,3),('1234567890','haha1','customer1@example.com','M','1990-01-01','John Doe',1,'31',2,1),('2345678901','haha6','customer6@example.com','F','1993-03-03','Emily Taylor',6,'28',2,6),('3456789012','haha8','customer8@example.com','F','1975-07-07','Jessica Anderson',8,'46',1,8),('4445556667','haha4','customer4@example.com','F','1988-08-08','Emma Brown',4,'33',4,4),('4567890123','haha10','customer10@example.com','F','1965-09-09','Sophia Brown',10,'56',2,10),('7778889991','haha5','customer5@example.com','M','1992-02-02','Michael Wilson',5,'29',5,5),('8901234567','haha7','customer7@example.com','M','1980-04-04','David Martinez',7,'41',3,7),('9012345678','haha9','customer9@example.com','M','1970-06-06','Daniel Garcia',9,'51',4,9),('9876543210','haha2','customer2@example.com','F','1995-05-05','Jane Smith',2,'26',3,2);
/*!40000 ALTER TABLE `customer` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-03-31 18:36:27
