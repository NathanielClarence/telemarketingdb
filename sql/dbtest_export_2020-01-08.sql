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
-- Dumping data for table `add_data`
--

LOCK TABLES `add_data` WRITE;
/*!40000 ALTER TABLE `add_data` DISABLE KEYS */;
INSERT INTO `add_data` VALUES ('nama_ibu');
/*!40000 ALTER TABLE `add_data` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admins`
--

LOCK TABLES `admins` WRITE;
/*!40000 ALTER TABLE `admins` DISABLE KEYS */;
INSERT INTO `admins` VALUES (1,'admin1','58b5444cf1b6253a4317fe12daff411a78bda0a95279b1d5768ebf5ca60829e78da944e8a9160a0b6d428cb213e813525a72650dac67b88879394ff624da482f','adm',1,'all','Testing Account 1'),(2,'telle1','59d8a5c23871a07d3857305ea046b63b7c76e957f42a9083216d58904b149c84547a67a83057a04ad50e7b64f1497966e5fb16419e22339ef8f54711629ccdc5','telle',1,'cc','Testing Account 2'),(4,'admin2','661bb43140229ad4dc3e762e7bdd68cc14bb9093c158c386bd989fea807acd9bd7f805ca4736b870b6571594d0d8fcfc57b98431143dfb770e083fa9be89bc72','adm',0,'all','Test Acc 2'),(5,'vnicholash','3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79','adm',1,'all','Nicholas Halim'),(6,'jakasembung','12b03226a6d8be9c6e8cd5e55dc6c7920caaa39df14aab92d5e3ea9340d1c8a4d3d0b8e4314f1f6ef131ba4bf1ceb9186ab87c801af0d5c95b1befb8cedae2b9','adm',1,'all','Jaka Sembung'),(7,'dmm','38416cab117b289fd11655dbc1ee533251f1d56084e8a4692e7bd37ee6ae8fbe17d8ebb033dfe573230db171cd430313be088ddeb0b1b973f2c2951fb15079e2','adm',0,'all','NN'),(8,'NAN','e1cb8b296cbea6b5af982f53b1a9abbed7d9bb571d4fb53f0c6a1dacc7c9e65f518017f5b128b9de0fe3f5ff9b21e15515080a9a34d5ce20218f1708e85d1c69','telle',0,'KNTL','NonusAnonimusNostradamus'),(12,'telle2','3041d35165ec6bcfc0e8274080ec6de336c6c97a691416a10ba1f92bdfc9c079a0ff18ed032b19592c034d3c4112f09fc815c0cb2e02b547dcf89a35742a3ae7','telle',1,'pl','Telle Testing 2');
/*!40000 ALTER TABLE `admins` ENABLE KEYS */;
UNLOCK TABLES;

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
  `assign_date` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assign_cc`
--

LOCK TABLES `assign_cc` WRITE;
/*!40000 ALTER TABLE `assign_cc` DISABLE KEYS */;
INSERT INTO `assign_cc` VALUES (1,'telle1',0,'2019-12-01 09:44:33'),(2,'telle1',0,'2019-12-01 09:44:33'),(3,'telle1',2,'2020-01-06 10:03:01'),(4,'telle1',2,'2019-12-01 09:44:33'),(5,'telle1',0,'2019-12-01 09:44:33'),(6,'telle1',0,'2020-01-06 09:41:59'),(7,'telle1',0,'2020-01-06 09:41:59'),(8,'telle1',0,'2020-01-06 09:41:59'),(9,'telle1',0,'2020-01-06 09:41:59'),(10,'telle1',0,'2020-01-06 09:41:59'),(11,'telle1',0,'2020-01-06 09:41:59'),(12,'telle1',0,'2020-01-06 09:41:59'),(13,'telle1',0,'2020-01-06 09:41:59'),(14,'telle1',0,'2020-01-06 09:41:59'),(15,'telle1',0,'2020-01-06 09:41:59'),(16,'telle1',0,'2020-01-06 09:41:59'),(17,'telle1',0,'2020-01-06 09:41:59'),(18,'telle1',0,'2020-01-06 09:41:59'),(19,'telle1',0,'2020-01-06 09:41:59'),(20,'telle1',0,'2020-01-06 09:41:59'),(21,' ',0,'2020-01-06 09:41:59');
/*!40000 ALTER TABLE `assign_cc` ENABLE KEYS */;
UNLOCK TABLES;

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
  `assign_date` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`cust_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `assign_pl`
--

LOCK TABLES `assign_pl` WRITE;
/*!40000 ALTER TABLE `assign_pl` DISABLE KEYS */;
INSERT INTO `assign_pl` VALUES (1,'telle2',0,'2020-01-06 09:44:33'),(2,'telle2',0,'2020-01-06 09:44:33'),(3,'telle2',0,'2020-01-06 09:44:33'),(4,'telle2',0,'2020-01-06 09:44:33'),(5,'telle2',0,'2020-01-06 09:44:33'),(6,'telle2',0,'2020-01-06 09:44:33'),(7,'telle2',0,'2020-01-06 09:44:33'),(8,'telle2',0,'2020-01-06 09:44:33'),(9,'telle2',0,'2020-01-06 09:44:33'),(10,'telle2',0,'2020-01-06 09:44:33'),(11,'telle2',0,'2020-01-06 09:44:33'),(12,'telle2',0,'2020-01-06 09:44:33'),(13,'telle2',0,'2020-01-06 09:44:33'),(14,'telle2',0,'2020-01-06 09:44:33'),(15,'telle2',0,'2020-01-06 09:44:33'),(16,'telle2',0,'2020-01-06 09:44:33'),(17,'telle2',0,'2020-01-06 09:44:33'),(18,'telle2',0,'2020-01-06 09:44:33'),(19,'telle2',0,'2020-01-06 09:44:33'),(20,'telle2',0,'2020-01-06 09:44:33'),(21,' ',0,'2020-01-06 09:44:33');
/*!40000 ALTER TABLE `assign_pl` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `bank_cc`
--

LOCK TABLES `bank_cc` WRITE;
/*!40000 ALTER TABLE `bank_cc` DISABLE KEYS */;
INSERT INTO `bank_cc` VALUES (8,'Bank 88'),(9,'Bank Indonesia'),(4,'BCA'),(3,'BNI'),(1,'BRI'),(2,'CIMB NIAGA'),(5,'MNC'),(6,'UOB');
/*!40000 ALTER TABLE `bank_cc` ENABLE KEYS */;
UNLOCK TABLES;

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
-- Dumping data for table `bank_pl`
--

LOCK TABLES `bank_pl` WRITE;
/*!40000 ALTER TABLE `bank_pl` DISABLE KEYS */;
INSERT INTO `bank_pl` VALUES (2,'Bank UKDW'),(1,'SAMPOERNA');
/*!40000 ALTER TABLE `bank_pl` ENABLE KEYS */;
UNLOCK TABLES;

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
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `customers`
--

LOCK TABLES `customers` WRITE;
/*!40000 ALTER TABLE `customers` DISABLE KEYS */;
INSERT INTO `customers` VALUES (1,NULL,'0888008080',NULL,'koran',0,NULL,'223322','1911/000000001',NULL,'2000-01-01',NULL,'2019-12-30 09:14:10'),(2,'nn','0808080','jalan siang','bank m',0,NULL,NULL,'1911/000000002',NULL,'2000-01-01',NULL,'2019-12-30 09:14:10'),(3,'n2','0888080080','jalan pagi','bank m',0,NULL,NULL,'1911/000000003',NULL,'2000-01-01',NULL,'2019-12-30 09:14:10'),(4,NULL,'088800808000088',NULL,'koran',0,NULL,NULL,'1911/000000004',NULL,'2000-01-01',NULL,'2019-12-30 09:14:10'),(5,'dabar','080808080080888','jalan 88 no 88','bank 88',0,'08888888','8888888888','1911/000000005','8888;8888;888','2000-01-01',NULL,'2019-12-30 09:14:10'),(6,'yanto','0899991919','jalan sd','BRI',0,'21221233123','2331131','1912/000000006','999;999;999','2000-01-01',NULL,'2019-12-30 09:14:10'),(7,'databaru','0888998989','jalan smp','BCA',0,'123123123','210000','1912/000000007','999;999;999','2000-01-01',NULL,'2019-12-30 09:14:10'),(8,'dalem','0898989',NULL,'BRI',0,'123123112','21131000','1912/000000008','999;999;999','2000-01-01',NULL,'2019-12-30 09:14:10'),(9,'DK','808080','jalan medog','koran',0,'99118811','21 digit','1912/000000009','999;99','1999-01-21',NULL,'2019-12-30 09:14:10'),(10,'DDK','90900','jln ln','BNI',0,'9911999','22 digit','1912/000000010','99999;9999','1999-01-22',NULL,'2019-12-30 09:14:10'),(11,'Brigitta Tifanny','081234567890','Jalan Kaliurang KM 9 Yogyakarta','handuajduukaj',0,'1234567890123456','100000000','1912/000000011','1234578909754323568','1998-12-31',NULL,'2019-12-30 09:14:10'),(12,'Lala','096472921','Suka suka','Surga',0,'12346940','100 digit','1912/000000012','99942399','1899-11-30',NULL,'2019-12-30 09:14:10'),(13,'Juju','09873456789','Ikeh','Kepo',0,'234567890876543','10 digit','1912/000000013','164894562834','1752-09-14',NULL,'2019-12-30 09:14:10'),(14,'sdfgkmnvcdrty','23456789098765','jalan jalan ke surabaya','Jakarta',0,'34567890987654345678','22 digit','1912/000000014','34567890678','2000-01-01',NULL,'2019-12-30 09:14:10'),(15,'Bujug','088818188181','jjkkll','bank hiyahiya',0,'12331991191','44 digit','1912/000000015','9910290','2000-01-01',NULL,'2019-12-30 09:14:10'),(16,'Dancho','0889199191','ssa','bank hayohayo',0,'199910012231','99 digit','1912/000000016','992211331;1123100192','2000-01-01',NULL,'2019-12-30 09:14:10'),(17,'DDSSA','081881991199',NULL,'bank helohelo',0,'99910011299123','9909','1912/000000017','999010011;09991001','2000-01-01',NULL,'2019-12-30 09:14:10'),(18,'Kalina','0888199191',NULL,'GK PMC',0,'9912399910123',NULL,'1912/000000018','9999999;9999999999;9999999','2000-01-01',NULL,'2019-12-30 09:14:10'),(19,'Tanaka','089199123199123',NULL,'Bank DMM',0,'99188231231123',NULL,'1912/000000019',NULL,'2000-01-01',NULL,'2019-12-30 09:14:10'),(20,'Gorbachev','0889919919191','edward','Sovetsky Soyuz',0,'kkttppp','???','1912/000000020',NULL,'2000-01-01',NULL,'2019-12-30 09:14:10'),(21,NULL,'0818181818181',NULL,'koran',0,NULL,NULL,NULL,NULL,'2000-01-01',NULL,'2020-01-06 05:59:37');
/*!40000 ALTER TABLE `customers` ENABLE KEYS */;
UNLOCK TABLES;

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
  PRIMARY KEY (`data_id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prod_cc`
--

LOCK TABLES `prod_cc` WRITE;
/*!40000 ALTER TABLE `prod_cc` DISABLE KEYS */;
INSERT INTO `prod_cc` VALUES (1,2,1,1,0,'Tidak',NULL,'2019-10-18','admin1',NULL,0,0,2,NULL,'2019-11-29 02:11:11',0,NULL),(2,3,0,0,0,'Tidak',NULL,'2019-10-09','admin1',NULL,0,0,2,NULL,NULL,0,NULL),(3,3,1,0,0,'Tidak',NULL,'2019-11-18','admin1',NULL,0,0,2,NULL,NULL,0,NULL),(12,2,1,0,0,'Tidak',NULL,'2019-10-27','admin1',NULL,0,0,2,NULL,NULL,0,NULL),(13,1,1,1,1,'Tertarik','1911/CC/000000001','2019-10-18','telle1','BCA',1,0,2,'2019-11-28',NULL,0,NULL),(14,1,1,1,1,'Tidak',NULL,'2019-09-18','telle1',NULL,0,0,2,NULL,NULL,0,NULL),(15,2,1,1,1,'Pikir-pikir',NULL,'2019-11-29','admin1',NULL,0,0,2,NULL,'2019-11-29 02:24:04',1,NULL),(16,2,1,1,1,'Tidak',NULL,'2019-11-29','admin1',NULL,0,0,2,NULL,NULL,0,NULL),(17,1,1,0,1,'Tidak',NULL,'2019-11-29','telle1',NULL,0,0,2,NULL,NULL,0,NULL),(18,3,1,1,0,'Tidak',NULL,'2019-11-29','admin1',NULL,0,0,2,NULL,NULL,0,NULL),(19,2,1,1,1,'Tidak',NULL,'2019-12-01','telle1','',0,0,2,NULL,NULL,0,NULL),(20,1,1,1,1,'Tidak',NULL,'2019-12-03','jakasembung','',1,1,0,'2019-12-16',NULL,0,'2019-12-16'),(21,1,1,1,1,'Tidak',NULL,'2019-12-03','admin1','',0,0,2,NULL,NULL,0,NULL),(22,5,1,1,1,'Pikir-pikir',NULL,'2019-12-16','telle1',NULL,0,0,2,NULL,NULL,1,NULL),(23,6,1,1,1,'Pikir-pikir',NULL,'2019-12-16','telle1',NULL,0,0,2,NULL,NULL,1,NULL),(24,6,1,1,1,'Pikir-pikir',NULL,'2019-12-16','jakasembung','',0,0,2,NULL,'2019-12-16 07:12:52',1,NULL),(25,6,1,1,1,'Tertarik','1912/CC/000000006','2019-12-16','telle1','Bank Indonesia',0,0,2,NULL,NULL,0,NULL),(26,8,1,1,1,'Pikir-pikir',NULL,'2019-12-16','telle1',NULL,0,0,2,NULL,NULL,1,NULL),(27,13,1,1,1,'Tertarik','1912/CC/000000013','2019-12-16','telle1','BCA',1,1,1,'2019-12-16',NULL,0,'2019-12-16'),(28,12,1,1,1,'Pikir-pikir',NULL,'2019-12-16','telle1',NULL,0,0,2,NULL,NULL,1,NULL),(29,12,1,1,1,'Tertarik','1912/CC/000000012','2019-12-16','telle1','BNI',0,0,2,NULL,NULL,0,NULL),(30,6,1,1,1,'Tidak',NULL,'2019-12-16','telle1','',0,0,2,NULL,NULL,0,NULL),(31,8,1,1,1,'Tidak',NULL,'2019-12-16','telle1','',0,0,2,NULL,NULL,0,NULL),(32,11,1,1,1,'Tidak',NULL,'2019-12-16','jakasembung',NULL,0,0,2,NULL,NULL,0,NULL),(33,9,1,1,1,'Pikir-pikir',NULL,'2019-12-16','jakasembung',NULL,0,0,2,NULL,NULL,0,NULL),(34,10,1,1,1,'Pikir-pikir',NULL,'2019-12-16','jakasembung',NULL,0,0,2,NULL,NULL,1,NULL),(35,14,1,1,1,'Tidak',NULL,'2019-12-16','jakasembung',NULL,0,0,2,NULL,NULL,0,NULL),(36,14,1,1,1,'Tidak',NULL,'2019-12-16','jakasembung','',0,0,2,NULL,NULL,0,NULL),(37,20,1,1,1,'Tertarik','1912/CC/000000020','2019-12-26','admin1','BRI',1,1,2,'2019-12-26',NULL,0,NULL);
/*!40000 ALTER TABLE `prod_cc` ENABLE KEYS */;
UNLOCK TABLES;

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
  PRIMARY KEY (`data_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `prod_pl`
--

LOCK TABLES `prod_pl` WRITE;
/*!40000 ALTER TABLE `prod_pl` DISABLE KEYS */;
INSERT INTO `prod_pl` VALUES (1,1,1,1,1,'Tertarik','1911/PL/000000001','2019-11-29','admin1','SAMPOERNA',1,1,'2019-11-29',NULL,0,1,0,1,0,2,0,2,0,NULL);
/*!40000 ALTER TABLE `prod_pl` ENABLE KEYS */;
UNLOCK TABLES;

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

--
-- Dumping data for table `products`
--

LOCK TABLES `products` WRITE;
/*!40000 ALTER TABLE `products` DISABLE KEYS */;
INSERT INTO `products` VALUES (1,'Kartu Kredit','CC'),(2,'Pinjaman Tunai','PL');
/*!40000 ALTER TABLE `products` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-08 16:23:08
