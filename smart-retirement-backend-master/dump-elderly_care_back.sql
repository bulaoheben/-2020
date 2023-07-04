-- MySQL dump 10.13  Distrib 5.6.51, for Win32 (AMD64)
--
-- Host: localhost    Database: elderly_care_back
-- ------------------------------------------------------
-- Server version	5.6.51

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
-- Table structure for table `employee_info`
--
USE elderly_care_back;
DROP TABLE IF EXISTS `employee_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `employee_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `id_card` varchar(100) NOT NULL,
  `birthday` varchar(100) NOT NULL,
  `hire_date` varchar(100) NOT NULL,
  `resign_date` varchar(100) DEFAULT NULL,
  `imgset_dir` varchar(100) DEFAULT NULL,
  `profile_photo` varchar(100) NOT NULL,
  `CREATED` varchar(100) DEFAULT NULL,
  `UPDATED` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_info`
--

LOCK TABLES `employee_info` WRITE;
/*!40000 ALTER TABLE `employee_info` DISABLE KEYS */;
INSERT INTO `employee_info` VALUES (1,'worker','女','24242','323333','2018-07-09 00:00:00','2022-07-01 00:00:00','',NULL,'/','2022-07-02 13:35:11.103',NULL),(2,'worker3','男','46453','6666','2019-07-16 00:00:00','2022-07-06 00:00:00','2022-07-26 00:00:00',NULL,'/','2022-07-02 16:40:47.669',NULL);
/*!40000 ALTER TABLE `employee_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oldperson_info`
--

DROP TABLE IF EXISTS `oldperson_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oldperson_info` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `id_card` varchar(100) NOT NULL,
  `birthday` varchar(100) NOT NULL,
  `checkin_date` varchar(100) NOT NULL,
  `checkout_date` varchar(100) DEFAULT NULL,
  `imgset_dir` varchar(100) DEFAULT NULL,
  `profile_photo` varchar(100) NOT NULL,
  `room_number` varchar(100) NOT NULL,
  `CREATED` varchar(100) DEFAULT NULL,
  `UPDATED` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oldperson_info`
--

LOCK TABLES `oldperson_info` WRITE;
/*!40000 ALTER TABLE `oldperson_info` DISABLE KEYS */;
INSERT INTO `oldperson_info` VALUES (1,'圣诞老人','男','13984984829','220112303939393939','1991-11-04 00:00:00','2022-07-25 00:00:00','2022-07-28 00:00:00',NULL,'/','123','2022-07-02 09:27:22.868',NULL),(2,'42422','女','2222222222222','222222222222','2018-07-03 00:00:00','2022-07-12 00:00:00','2022-07-19 00:00:00',NULL,'/','222','2022-07-02 09:58:27.366',NULL),(3,'新老人','男','3333','33333','2020-06-30 00:00:00','2022-05-03 00:00:00','2022-07-12 00:00:00',NULL,'/','555','2022-07-02 12:38:37.496',NULL),(4,'66666','男','44','4444','2019-07-10 00:00:00','2022-07-05 00:00:00','',NULL,'/','455','2022-07-02 12:52:56.83',NULL),(5,'24242','女','333','2222','2017-07-04 00:00:00','2022-07-12 00:00:00','','https://lzh-pic.oss-cn-beijing.aliyuncs.com/images/oldpeople/5','https://lzh-pic.oss-cn-beijing.aliyuncs.com/images/oldpeople/5/smile_10.jpg','324','2022-07-02 17:22:26.351',NULL);
/*!40000 ALTER TABLE `oldperson_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sys_user`
--

DROP TABLE IF EXISTS `sys_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sys_user` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Username` varchar(100) NOT NULL,
  `Password` varchar(100) NOT NULL,
  `REAL_NAME` varchar(100) NOT NULL,
  `SEX` varchar(100) NOT NULL,
  `EMAIL` varchar(100) NOT NULL,
  `PHONE` varchar(100) NOT NULL,
  `MOBILE` varchar(100) NOT NULL,
  `CREATED` varchar(100) DEFAULT NULL,
  `UPDATED` varchar(100) DEFAULT NULL,
  `logoimage` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sys_user`
--

LOCK TABLES `sys_user` WRITE;
/*!40000 ALTER TABLE `sys_user` DISABLE KEYS */;
INSERT INTO `sys_user` VALUES (1,'finyle','123456789@','菲奈欧','男','33333333@11.com','73874884','13947093893','2022-07-01 19:50:11.522','2022-07-01 20:17:41.002','https://lzh-pic.oss-cn-beijing.aliyuncs.com/images/profile_photo/202206101195403.png');
/*!40000 ALTER TABLE `sys_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `volunteer_info`
--

DROP TABLE IF EXISTS `volunteer_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `volunteer_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `gender` varchar(100) NOT NULL,
  `phone` varchar(100) NOT NULL,
  `id_card` varchar(100) NOT NULL,
  `birthday` varchar(100) NOT NULL,
  `checkin_date` varchar(100) NOT NULL,
  `checkout_date` varchar(100) DEFAULT NULL,
  `imgset_dir` varchar(100) DEFAULT NULL,
  `profile_photo` varchar(100) NOT NULL,
  `CREATED` varchar(100) DEFAULT NULL,
  `UPDATED` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `volunteer_info`
--

LOCK TABLES `volunteer_info` WRITE;
/*!40000 ALTER TABLE `volunteer_info` DISABLE KEYS */;
INSERT INTO `volunteer_info` VALUES (1,'volunteer','男','435464','222222','2021-06-01 00:00:00','2022-07-18 00:00:00','',NULL,'/','2022-07-02 13:13:36.28',NULL),(2,'非官方','女','453534','323323','2018-07-02 00:00:00','2022-07-14 00:00:00','2022-07-14 00:00:00',NULL,'/','2022-07-02 16:34:35.972',NULL),(3,'5555','女','35353','2222','2022-07-04 00:00:00','2022-07-12 00:00:00','2022-07-26 00:00:00',NULL,'/','2022-07-02 16:43:04.073',NULL),(4,'544545','女','2222','222','2019-07-15 00:00:00','2022-07-11 00:00:00','','https://lzh-pic.oss-cn-beijing.aliyuncs.com/images/volunteer/4','https://lzh-pic.oss-cn-beijing.aliyuncs.com/images/volunteer/4/smile_10.jpg','2022-07-02 16:59:10.816',NULL);
/*!40000 ALTER TABLE `volunteer_info` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'elderly_care_back'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-02 21:44:23
