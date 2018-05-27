-- MySQL dump 10.13  Distrib 5.7.17, for Win64 (x86_64)
--
-- Host: 169.254.10.1    Database: piWeather
-- ------------------------------------------------------
-- Server version	5.5.54-0+deb8u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cameraTriggers`
--

DROP TABLE IF EXISTS `cameraTriggers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cameraTriggers` (
  `triggerID` int(11) NOT NULL AUTO_INCREMENT,
  `sensorName` varchar(45) DEFAULT NULL,
  `triggerValue` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`triggerID`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1 COMMENT='	';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `eenheid`
--

DROP TABLE IF EXISTS `eenheid`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `eenheid` (
  `eenheidID` int(11) NOT NULL,
  `eenheid` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`eenheidID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `meting`
--

DROP TABLE IF EXISTS `meting`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `meting` (
  `metingID` int(11) NOT NULL AUTO_INCREMENT,
  `sensorID` int(11) DEFAULT NULL,
  `tijdstip` datetime DEFAULT NULL,
  `waarde` int(11) DEFAULT NULL,
  `eenheidID` int(11) DEFAULT NULL,
  PRIMARY KEY (`metingID`),
  KEY `fk_meting_sensoren_idx` (`sensorID`),
  KEY `fk_meting_eenheid1_idx` (`eenheidID`),
  CONSTRAINT `fk_meting_eenheid1` FOREIGN KEY (`eenheidID`) REFERENCES `eenheid` (`eenheidID`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_meting_sensoren` FOREIGN KEY (`sensorID`) REFERENCES `sensoren` (`sensorID`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=14246 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `sensoren`
--

DROP TABLE IF EXISTS `sensoren`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sensoren` (
  `sensorID` int(11) NOT NULL,
  `sensorName` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`sensorID`),
  KEY `fk_sensoren_settings1_idx` (`sensorName`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `settings`
--

DROP TABLE IF EXISTS `settings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `settings` (
  `settingsID` int(11) NOT NULL AUTO_INCREMENT,
  `sensorName` varchar(45) DEFAULT NULL,
  `minimumValue` int(11) DEFAULT NULL,
  `maximumValue` int(11) DEFAULT NULL,
  PRIMARY KEY (`settingsID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping events for database 'piWeather'
--

--
-- Dumping routines for database 'piWeather'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-06-19 13:32:45
