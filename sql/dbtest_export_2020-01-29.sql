-- MySQL dump 10.13  Distrib 8.0.17, for Win64 (x86_64)
--
-- Host: localhost    Database: dbtest
-- ------------------------------------------------------
-- Server version	8.0.17

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
-- Table structure for table `add_data`
--

DROP TABLE IF EXISTS `add_data`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_data` (
  `col` varchar(32) NOT NULL,
  UNIQUE KEY `col` (`col`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `admins`
--

DROP TABLE IF EXISTS `admins`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admins` (
  `id` int(15) NOT NULL AUTO_INCREMENT,
  `username` varchar(32) NOT NULL,
  `password` varchar(1000) NOT NULL,
  `privilege` varchar(5) NOT NULL,
  `active_status` tinyint(1) NOT NULL DEFAULT '1',
  `product` varchar(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`,`username`),
  UNIQUE KEY `username` (`username`),
  UNIQUE KEY `username_2` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `assign_cc`
--

DROP TABLE IF EXISTS `assign_cc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assign_cc` (
  `cust_id` int(20) NOT NULL,
  `assigned_telle` varchar(32) NOT NULL DEFAULT ' ',
  `times_assigned` int(1) NOT NULL DEFAULT '0',
  `assign_date` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `assign_pl`
--

DROP TABLE IF EXISTS `assign_pl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `assign_pl` (
  `cust_id` int(20) NOT NULL,
  `assigned_telle` varchar(32) NOT NULL DEFAULT ' ',
  `times_assigned` int(1) NOT NULL DEFAULT '0',
  `assign_date` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bank_cc`
--

DROP TABLE IF EXISTS `bank_cc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank_cc` (
  `id_bank` int(32) NOT NULL AUTO_INCREMENT,
  `nama_bank` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id_bank`),
  UNIQUE KEY `nama_bank` (`nama_bank`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `bank_pl`
--

DROP TABLE IF EXISTS `bank_pl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `bank_pl` (
  `id_bank` int(32) NOT NULL AUTO_INCREMENT,
  `nama_bank` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`id_bank`),
  UNIQUE KEY `nama_bank` (`nama_bank`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `customers`
--

DROP TABLE IF EXISTS `customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `customers` (
  `id` int(20) NOT NULL AUTO_INCREMENT,
  `nama` varchar(255) DEFAULT NULL,
  `telp` varchar(20) NOT NULL,
  `alamat` varchar(255) DEFAULT NULL,
  `asal_data` varchar(30) NOT NULL,
  `fetched` tinyint(1) NOT NULL DEFAULT '0',
  `no_ktp` varchar(32) DEFAULT NULL,
  `penghasilan` varchar(32) DEFAULT NULL,
  `unique_code` varchar(32) DEFAULT NULL,
  `cc` varchar(500) DEFAULT NULL,
  `date_of_birth` date DEFAULT NULL,
  `nama_ibu` varchar(100) DEFAULT NULL,
  `date_added` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `params`
--

DROP TABLE IF EXISTS `params`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `params` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `value` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `prod_cc`
--

DROP TABLE IF EXISTS `prod_cc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prod_cc` (
  `data_id` int(20) NOT NULL AUTO_INCREMENT,
  `cust_id` int(20) NOT NULL,
  `connected` tinyint(1) NOT NULL,
  `received` tinyint(1) NOT NULL,
  `explained` tinyint(1) NOT NULL,
  `note` varchar(15) NOT NULL DEFAULT 'Tidak',
  `unique_code` varchar(255) DEFAULT NULL,
  `updated` date NOT NULL,
  `updater` varchar(32) NOT NULL,
  `bank` varchar(32) DEFAULT NULL,
  `berkas` tinyint(1) NOT NULL DEFAULT '0',
  `data_masuk` tinyint(1) NOT NULL DEFAULT '0',
  `approval` int(2) NOT NULL DEFAULT '2',
  `followup_date` date DEFAULT NULL,
  `recontact` timestamp NULL DEFAULT NULL,
  `recontact_status` tinyint(1) NOT NULL DEFAULT '0',
  `approval_date` date DEFAULT NULL,
  `prospect` int(2) DEFAULT '0',
  `app_type` varchar(10) DEFAULT NULL,
  `comment` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`data_id`)
) ENGINE=InnoDB AUTO_INCREMENT=43 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `prod_pl`
--

DROP TABLE IF EXISTS `prod_pl`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `prod_pl` (
  `data_id` int(20) NOT NULL AUTO_INCREMENT,
  `cust_id` int(20) NOT NULL,
  `connected` tinyint(1) NOT NULL,
  `received` tinyint(1) NOT NULL,
  `explained` tinyint(1) NOT NULL,
  `note` varchar(15) NOT NULL DEFAULT 'Tidak',
  `unique_code` varchar(255) DEFAULT NULL,
  `updated` date NOT NULL,
  `updater` varchar(32) NOT NULL,
  `bank` varchar(32) DEFAULT NULL,
  `berkas` tinyint(1) NOT NULL DEFAULT '0',
  `data_masuk` tinyint(1) NOT NULL DEFAULT '0',
  `followup_date` date DEFAULT NULL,
  `recontact` timestamp NULL DEFAULT NULL,
  `recontact_status` tinyint(1) NOT NULL DEFAULT '0',
  `agent` tinyint(1) NOT NULL DEFAULT '0',
  `owner` tinyint(1) NOT NULL DEFAULT '0',
  `setuju` int(2) NOT NULL DEFAULT '2',
  `ondesk_keluar` tinyint(1) NOT NULL DEFAULT '0',
  `cst_approve` int(2) NOT NULL DEFAULT '2',
  `visit` tinyint(1) NOT NULL DEFAULT '0',
  `vis_approval` int(2) NOT NULL DEFAULT '2',
  `akad` tinyint(1) NOT NULL DEFAULT '0',
  `akad_date` date DEFAULT NULL,
  `prospect` int(2) DEFAULT '0',
  `app_type` varchar(10) DEFAULT NULL,
  `comment` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`data_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Table structure for table `products`
--

DROP TABLE IF EXISTS `products`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `products` (
  `id` int(5) NOT NULL AUTO_INCREMENT,
  `nama_produk` varchar(32) NOT NULL,
  `kode_produk` varchar(5) NOT NULL,
  PRIMARY KEY (`id`,`kode_produk`),
  UNIQUE KEY `kode_produk` (`kode_produk`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-29 17:38:55
