-- MariaDB dump 10.19  Distrib 10.11.2-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: tooling
-- ------------------------------------------------------
-- Server version	10.11.2-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `cabinet_tooling`
--

DROP TABLE IF EXISTS `cabinet_tooling`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cabinet_tooling` (
  `category` varchar(250) NOT NULL,
  `category_url` varchar(50) DEFAULT NULL,
  `category_image` varchar(250) DEFAULT NULL,
  `sub_category` varchar(250) NOT NULL,
  `sub_category_url` varchar(50) DEFAULT NULL,
  `sub_category_image` varchar(250) DEFAULT NULL,
  `item` varchar(250) NOT NULL,
  `item_image` varchar(250) DEFAULT NULL,
  `descript` varchar(250) DEFAULT NULL,
  `location` smallint(6) NOT NULL,
  `quantity` smallint(6) NOT NULL,
  `minimum` smallint(6) NOT NULL,
  `manufacturer` varchar(250) NOT NULL,
  `edp` varchar(100) NOT NULL,
  `vendor` varchar(100) NOT NULL,
  `purchased` date NOT NULL,
  PRIMARY KEY (`edp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cabinet_tooling`
--

LOCK TABLES `cabinet_tooling` WRITE;
/*!40000 ALTER TABLE `cabinet_tooling` DISABLE KEYS */;
INSERT INTO `cabinet_tooling` VALUES
('Countersinks','countersinks','center_drills.jpg','Center Drills','center_drill','KEO_CENTERDRILL.jpg','#0 Center Drill','KEO_CENTERDRILL.jpg','Cobalt, Double End, 60 deg., Plain Finish',123,21,2,'KEO','10034','PT Solutions','2023-03-20'),
('Shop Supplies','supplies','collet.jpg','Tools','tools','tools.jpg','Allen Wrenches','allen_wrenches.jpg','22 Piece Standard/Metric Set',207,4,0,'Eklind','10222','PT Solutions','2023-03-20'),
('Countersinks','countersinks','center_drills.jpg','Center Drills','center_drill','KEO_CENTERDRILL.jpg','#2 Center Drill','KEO_CENTERDRILL.jpg','Cobalt, Double End, 60 deg., Plain Finish',123,10,2,'KEO','10242','PT Solutions','2023-03-20'),
('Taps','taps','taps.jpg','Spiral Point Taps','spiral_point','1230800.jpg','5/16-18 H3','1230800.jpg','Spiral Point, Bright Finish, 2 Flute, Material: Aluminum, Steel',112,3,1,'OSG','1230800','PT Solutions','2023-03-20'),
('Countersinks','countersinks','center_drills.jpg','Center Drills','center_drill','KEO_CENTERDRILL.jpg','#4 1/2 Center Drill','KEO_CENTERDRILL.jpg','Cobalt, Double End, 60 deg., Plain Finish',124,10,2,'KEO','14542','PT Solutions','2023-03-20'),
('Shop Supplies','supplies','collet.jpg','Collets','collets','collet.jpg','Emergency Collets','collet.jpg','1\" Extended, 5C E-Collet, 1/8 Pilot Hole',199,2,1,'Hardinge','148629','Hardinge','2023-03-20'),
('Countersinks','countersinks','center_drills.jpg','Countersinks','countersink','19071.jpg','5/16 X 82 deg','19071.jpg','Carbide, Double End, 4 flute, Plain Finish',134,4,1,'Melin','19071','McMaster-Carr','2023-03-20'),
('Internal Tools','carbide_id','carbide_id.jpg','ID Groove','grooving','20-1540.jpg','3/8 dia. X .062 Width','20-1530.jpg','Carbide, .500\" Max Depth, Plain Finish',130,0,0,'Internal Tool','20-1530','BlackHawk Industrial','2023-03-20'),
('Internal Tools','carbide_id','carbide_id.jpg','ID Groove','grooving','20-1540.jpg','3/8 dia. X .062 Width','20-1540.jpg','Carbide, 1.00\" Max Depth, Plain Finish',130,1,0,'Internal Tool','20-1540','BlackHawk Industrial','2023-03-20'),
('Milling','milling','endmills.jpg','Chamfer Mills','chamfer_mill','209-084250B.jpeg','1/4 X 82 deg','209-084250B.jpg','Carbide, Single End, 4 flute, AlTiN',103,4,1,'Monster Tool/GWS','209-084250B','BlackHawk Industrial','2023-03-20'),
('Internal Tools','carbide_id','carbide_id.jpg','Boring Bars','boring_bar','CARBIDE_BORING_BAR.jpg','B230-800A','CARBIDE_BORING_BAR.jpg','5/16 Shank, AlTiN coated',117,4,2,'Scientific','213195','BlackHawk Industrial','2023-03-20'),
('Internal Tools','carbide_id','carbide_id.jpg','Boring Bars','boring_bar','CARBIDE_BORING_BAR.jpg','B290-1000A','CARBIDE_BORING_BAR.jpg','5/16 Shank, AlTiN coated',118,6,2,'Scientific','213201','BlackHawk Industrial','2023-03-20'),
('Taps','taps','taps.jpg','Spiral Flute Taps','spiral_flute','2918801.jpg','10-32 H5','2918801.jpg','Spiral Flute Bottom, Steam Oxide Coating, 3 Flute, Material: Stainless Steel',111,4,1,'OSG','2918801','PT Solutions','2023-03-20'),
('Milling','milling','endmills.jpg','Endmills','endmill','31189.jpg','1/4 4 Flute','31184.jpg','Double End, Solid Carbide, AlTiN Coated',92,4,2,'SGS','31184','PT Solutions','2023-03-20'),
('Milling','milling','endmills.jpg','Endmills','endmill','31189.jpg','3/8 4 Flute','31187.jpg','Double End, Solid Carbide, AlTiN Coated',97,2,2,'SGS','31187','PT Solutions','2023-03-20'),
('Milling','milling','endmills.jpg','Endmills','endmill','31189.jpg','1/2 4 Flute','31189.jpg','Double End, Solid Carbide, AlTiN Coated',100,4,2,'SGS','31189','PT Solutions','2023-03-20'),
('Taps','taps','taps.jpg','STI Taps','sti','382728BR.jpg','10-24 STI H2','382728BR.jpg','STI, Spiral Point, Bright Finish, 2 Flute, Material: Aluminum, Steel',111,3,1,'YMW','382728BR','PT Solutions','2023-03-20'),
('Deburring/Grinding','deburring','deburring.jpg','Grinding','grinding','20316.jpg','Bench Wheel','38501.jpg','6\" X 1/2\" X 1\", Fine Green for Carbide Tools',220,4,0,'CGW Abrasives','38501','PT Solutions','2023-03-20'),
('Inserts','inserts','inserts.jpg','OD Threading','od_threading','51448.jpg','3ER 16UN VKX','51448.jpg','External Threading, Material: All',6,12,2,'Vargus','51448','PT Solutions','2023-03-20'),
('Inserts','inserts','inserts.jpg','ID Threading','id_threading','52553.jpg','3IR 16UN VKX','52553.jpg','Internal Threading, Material: All',6,3,2,'Vargus','52553','PT Solutions','2023-03-20'),
('Inserts','inserts','inserts.jpg','Boring','boring','5550211.jpg','CCMT 2-1-SM IC807','5550211.jpg','.0156 TNR. Boring, Material: Stainless, INCO, A286',27,10,2,'Iscar','5550211','BlackHawk Industrial','2023-03-20'),
('Inserts','inserts','inserts.jpg','Boring','boring','5599989.jpg','CCGT 2-1-AS IC20','5599989.jpg','.0156 TNR. Boring, Material: Aluminum, Titanium',28,3,2,'Iscar','5599989','BlackHawk Industrial','2023-03-20'),
('Inserts','inserts','inserts.jpg','Face Grooving','face_groove','6000018.jpg','GFF 3N IC20','6000018.jpg','.008 TNR. Face Grooving, Material: Aluminum, Titanium',35,9,4,'Iscar','6000018','BlackHawk Industrial','2023-03-20'),
('Inserts','inserts','inserts.jpg','OD Grooving','od_groove','6002547.jpg','GFN-2J IC354','6002547.jpg','.008 TNR. CUT OFF, Material: All',30,10,4,'Iscar','6002547','BlackHawk Industrial','2023-03-20'),
('Milling','milling','endmills.jpg','Chamfer Mills','chamfer_mill','209-084250B.jpeg','1/4 X 90 deg','64-1415C.jpg','Carbide, Double End, 4 flute, AlTiN',103,1,1,'Internal Tool','64-1415C','PT Solutions','2023-03-20'),
('Inserts','inserts','inserts.jpg','ID Grooving','id_groove','6402242.jpg','GIPI 2.50-0.20 IC20','6402242.jpg','.008 TNR. ID Grooving, Material: Aluminum, Titanium ',36,9,2,'Iscar','6402242','PT Solutions','2023-03-20'),
('Inserts','inserts','inserts.jpg','Turning/Boring','turning/boring','6802122.jpg','CNMG 432 TM AH120','6802122.jpg','.031 TNR. Turning/Boring, Material: Stainless, INCO, A286',23,20,4,'Tungaloy','6802122','PT Solutions','2023-03-10'),
('Inserts','inserts','inserts.jpg','Turning/Boring','turning/boring','6803421.jpg','DNMG 432 TM AH120','6803421.jpg','.031 TNR. Turning/Boring, Material: Stainless, INCO, A286',53,3,2,'Tungaloy','6803421','PT Solutions','2023-03-20'),
('Inserts','inserts','inserts.jpg','Turning/Boring','turning/boring','6811615.jpg','CNMG 431 TM AH120','6811615.jpg','.0156 TNR. Turning/Boring, Material: Stainless, INCO, A286',23,10,2,'Tungaloy','6811615','PT Solutions','2023-03-10'),
('Inserts','inserts','inserts.jpg','Turning','turning','6812134.jpg','VNMG 331 TM AH120','6812134.jpg','.0156 TNR. Turning, Material: Stainless, INCO, A286',50,9,2,'Tungaloy','6812134','PT Solutions','2023-03-10'),
('Inserts','inserts','inserts.jpg','Turning','turning','6812146.jpg','VNMG 332 TM AH120','6812146.jpg','.031 TNR. Turning, Material: Stainless, INCO, A286',50,19,4,'Tungaloy','6812146','PT Solutions','2023-03-10'),
('Taps','taps','taps.jpg','STI Taps','sti','382728BR.jpg','8-32 STI H2','8006900.jpg','STI, Spiral Flute Bottom, Bright Finish, 3 Flute, Material: Aluminum',111,3,1,'OSG','8006900','PT Solutions','2023-03-20'),
('Deburring/Grinding','deburring','deburring.jpg','Deburring','deburring','860708.jpg','Red Buffing Disc','860708.jpg','6\" OD X 1/2\" ID',219,49,5,'Standard Abrasives','860708','PT Solutions','2023-03-20'),
('Reamers','reamers','reamers.jpg','Carbide Reamers','carbide','CARBIDE_REAMER.jpg','.1645 Dia.','CARBIDE_REAMER.jpg','Carbide',167,3,0,'RapidKut','BG5011645','PT Solutions','2023-03-20'),
('Deburring/Grinding','deburring','deburring.jpg','Deburring','deburring','EO1000.jpg','Roto-Burr','EO1000.jpg','Disposable Hand Deburring Tool',171,8,1,'Noga','EO1000','PT Solutions','2023-03-20'),
('Drills','drills','drills.jpg','Performance Drills','performance','drills.jpg','MDW02188HGS3','MDW_S3_DRILL.jpg','.2188 Dia., Coolant Through, Carbide, 3X Length',141,1,1,'Sumitomo','MDW02188HGS3','PT Solutions','2023-03-20'),
('Drills','drills','drills.jpg','Performance Drills','performance','drills.jpg','MDW02344HGS3','MDW_S3_DRILL.jpg','.2344 Dia., Coolant Through, Carbide, 3X Length',143,2,1,'Sumitomo','MDW02344HGS3','PT Solutions','2023-03-20'),
('Drills','drills','drills.jpg','Performance Drills','performance','drills.jpg','MDW03125HGS3','MDW_S3_DRILL.jpg','.3125 Dia., Coolant Through, Carbide, 3X Length',149,2,1,'Sumitomo','MDW03125HGS3','PT Solutions','2023-03-20'),
('Drills','drills','drills.jpg','Performance Drills','performance','drills.jpg','MDW0710HGS3','MDW_S3_DRILL.jpg','.2795 Dia., Coolant Through, Carbide, 3X Length',146,2,1,'Sumitomo','MDW0710HGS3','PT Solutions','2023-03-20'),
('Drills','drills','drills.jpg','Performance Drills','performance','drills.jpg','MWS0130SB','MWS_DRILLS.jpg','.051 Dia., Coolant Through, Carbide, 3X Length',136,2,1,'Mitsubishi','MWS0130SB','PT Solutions','2023-03-20'),
('Drills','drills','drills.jpg','Performance Drills','performance','drills.jpg','MWS0380SB','MWS_DRILLS.jpg','.1496 Dia., Coolant Through, Carbide, 3X Length',137,2,1,'Mitsubishi','MWS0380SB','PT Solutions','2023-03-20'),
('Drills','drills','drills.jpg','Performance Drills','performance','drills.jpg','MWS0510SB','MWS_DRILLS.jpg','.2007 Dia., Coolant Through, Carbide, 3X Length',140,3,1,'Mitsubishi','MWS0510SB','PT Solutions','2023-03-20'),
('Reamers','reamers','reamers.jpg','HSS Reamers','hss','HSS_REAMER.jpg','.162 Dia.','HSS_REAMER.jpg','HSS',167,1,0,'Tri-Angle','R25382','PT Solutions','2023-03-20');
/*!40000 ALTER TABLE `cabinet_tooling` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-29 11:31:22
