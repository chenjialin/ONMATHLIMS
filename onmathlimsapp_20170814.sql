-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: localhost    Database: SEQ_SA_INFO
-- ------------------------------------------------------
-- Server version	5.7.19-0ubuntu0.16.04.1

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
-- Table structure for table `analysis_master`
--

DROP TABLE IF EXISTS `analysis_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `analysis_master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `reference_genome` varchar(45) DEFAULT '',
  `compare_method` varchar(45) DEFAULT '',
  `create_time` datetime DEFAULT NULL,
  `created_by` varchar(45) DEFAULT '',
  `update_time` datetime DEFAULT NULL,
  `updated_by` varchar(45) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `analysis_master`
--

LOCK TABLES `analysis_master` WRITE;
/*!40000 ALTER TABLE `analysis_master` DISABLE KEYS */;
INSERT INTO `analysis_master` VALUES (1,1,'Ensemble','两两全比较','2016-04-10 23:05:00','test','2017-06-07 04:46:18','test');
/*!40000 ALTER TABLE `analysis_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `attachment`
--

DROP TABLE IF EXISTS `attachment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `attachment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `upload_user_id` int(11) NOT NULL,
  `operate_user_id` int(11) DEFAULT '0',
  `file_type` varchar(45) DEFAULT NULL,
  `filename` varchar(200) NOT NULL,
  `file_path` varchar(200) DEFAULT NULL,
  `status` varchar(45) DEFAULT NULL,
  `upload_time` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attachment`
--

LOCK TABLES `attachment` WRITE;
/*!40000 ALTER TABLE `attachment` DISABLE KEYS */;
INSERT INTO `attachment` VALUES (4,21,5,5,'send_sample','send_sample.xlsx','lims_app/static/attachment/21/send_sample/send_sample.xlsx','new','2017-08-02 00:01:21'),(5,21,5,5,'quality_check','ONMATH-900送样结果.xls','lims_app/static/attachment/21/quality_check/ONMATH-900送样结果.xls','new','2017-08-02 19:14:42'),(6,12,5,5,'quality_check','ONMATH-900送样结果.xls','lims_app/static/attachment/12/quality_check/ONMATH-900送样结果.xls','new','2017-08-03 17:41:36');
/*!40000 ALTER TABLE `attachment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add rna sample sequencing type',1,'add_rnasamplesequencingtype'),(2,'Can change rna sample sequencing type',1,'change_rnasamplesequencingtype'),(3,'Can delete rna sample sequencing type',1,'delete_rnasamplesequencingtype'),(4,'Can add sample info detail',2,'add_sampleinfodetail'),(5,'Can change sample info detail',2,'change_sampleinfodetail'),(6,'Can delete sample info detail',2,'delete_sampleinfodetail'),(7,'Can add dna sample sequencing type',3,'add_dnasamplesequencingtype'),(8,'Can change dna sample sequencing type',3,'change_dnasamplesequencingtype'),(9,'Can delete dna sample sequencing type',3,'delete_dnasamplesequencingtype'),(10,'Can add compare table',4,'add_comparetable'),(11,'Can change compare table',4,'change_comparetable'),(12,'Can delete compare table',4,'delete_comparetable'),(13,'Can add sample species',5,'add_samplespecies'),(14,'Can change sample species',5,'change_samplespecies'),(15,'Can delete sample species',5,'delete_samplespecies'),(16,'Can add sample other',6,'add_sampleother'),(17,'Can change sample other',6,'change_sampleother'),(18,'Can delete sample other',6,'delete_sampleother'),(19,'Can add analysis master',7,'add_analysismaster'),(20,'Can change analysis master',7,'change_analysismaster'),(21,'Can delete analysis master',7,'delete_analysismaster'),(22,'Can add sample type',8,'add_sampletype'),(23,'Can change sample type',8,'change_sampletype'),(24,'Can delete sample type',8,'delete_sampletype'),(25,'Can add user info',9,'add_userinfo'),(26,'Can change user info',9,'change_userinfo'),(27,'Can delete user info',9,'delete_userinfo'),(28,'Can add sample project master',10,'add_sampleprojectmaster'),(29,'Can change sample project master',10,'change_sampleprojectmaster'),(30,'Can delete sample project master',10,'delete_sampleprojectmaster'),(31,'Can add sample packet information',11,'add_samplepacketinformation'),(32,'Can change sample packet information',11,'change_samplepacketinformation'),(33,'Can delete sample packet information',11,'delete_samplepacketinformation'),(34,'Can add sample table',12,'add_sampletable'),(35,'Can change sample table',12,'change_sampletable'),(36,'Can delete sample table',12,'delete_sampletable'),(37,'Can add log entry',13,'add_logentry'),(38,'Can change log entry',13,'change_logentry'),(39,'Can delete log entry',13,'delete_logentry'),(40,'Can add group',14,'add_group'),(41,'Can change group',14,'change_group'),(42,'Can delete group',14,'delete_group'),(43,'Can add permission',15,'add_permission'),(44,'Can change permission',15,'change_permission'),(45,'Can delete permission',15,'delete_permission'),(46,'Can add user',16,'add_user'),(47,'Can change user',16,'change_user'),(48,'Can delete user',16,'delete_user'),(49,'Can add content type',17,'add_contenttype'),(50,'Can change content type',17,'change_contenttype'),(51,'Can delete content type',17,'delete_contenttype'),(52,'Can add session',18,'add_session'),(53,'Can change session',18,'change_session'),(54,'Can delete session',18,'delete_session'),(58,'Can add attachment',20,'add_attachment'),(59,'Can change attachment',20,'change_attachment'),(60,'Can delete attachment',20,'delete_attachment'),(61,'Can add build lib',21,'add_buildlib'),(62,'Can change build lib',21,'change_buildlib'),(63,'Can delete build lib',21,'delete_buildlib'),(64,'Can add down machine',22,'add_downmachine'),(65,'Can change down machine',22,'change_downmachine'),(66,'Can delete down machine',22,'delete_downmachine'),(67,'Can add quality check',23,'add_qualitycheck'),(68,'Can change quality check',23,'change_qualitycheck'),(69,'Can delete quality check',23,'delete_qualitycheck'),(70,'Can add send sample',24,'add_sendsample'),(71,'Can change send sample',24,'change_sendsample'),(72,'Can delete send sample',24,'delete_sendsample'),(73,'Can add up machine',25,'add_upmachine'),(74,'Can change up machine',25,'change_upmachine'),(75,'Can delete up machine',25,'delete_upmachine');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `build_lib`
--

DROP TABLE IF EXISTS `build_lib`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `build_lib` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `project_number` varchar(45) DEFAULT NULL,
  `sample_name` varchar(45) DEFAULT NULL,
  `sample_id` varchar(45) DEFAULT NULL,
  `lib_id` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample_id_UNIQUE` (`sample_name`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `build_lib`
--

LOCK TABLES `build_lib` WRITE;
/*!40000 ALTER TABLE `build_lib` DISABLE KEYS */;
INSERT INTO `build_lib` VALUES (1,12,'ONMATH-900','sample_name_1','10-A','lib_id_1','2017/6/29',''),(2,12,'ONMATH-900','sample_name_2','10-B','lib_id_2','2017/6/29',''),(3,12,'ONMATH-900','sample_name_3','11-A','lib_id_3','2017/6/29',''),(4,12,'ONMATH-900','sample_name_4','11-B','','2017/6/29',''),(5,12,'ONMATH-900','sample_name_5','12-A','lib_id_5','2017/6/29',''),(6,12,'ONMATH-900','sample_name_6','12-B','lib_id_6','2017/6/29',''),(7,12,'ONMATH-900','sample_name_7','13-A','','2017/6/29',''),(8,12,'ONMATH-900','sample_name_8','13-B','lib_id_8','2017/6/29',''),(9,12,'ONMATH-900','sample_name_9','14-A','lib_id_9','2017/6/29','haha'),(10,12,'ONMATH-900','sample_name_10','14-B','lib_id_10','2017/6/29',''),(11,14,'ONMATH-903','test_1','15-A','','2017/7/3',''),(12,14,'ONMATH-903','test_2','15-B','lib_id_12','2017/7/3',''),(13,14,'ONMATH-903','test_3','16-A','lib_id_13','2017/7/3',''),(14,14,'ONMATH-903','test_4','16-B','lib_id_14','2017/7/3',''),(15,14,'ONMATH-903','test_5','17-A','lib_id_15','2017/7/3',''),(16,14,'ONMATH-903','test_6','17-B','lib_id_16','2017/7/3',''),(17,14,'ONMATH-903','test_7','18-A','lib_id_17','2017/7/3',''),(18,14,'ONMATH-903','test_8','18-B','lib_id_18','2017/7/3',''),(19,14,'ONMATH-903','test_9','19-A','lib_id_19','2017/7/3','haha'),(20,14,'ONMATH-903','test_10','19-B','','2017/7/23',''),(21,21,'ONMATH-909','haha_1','20-A','lib_id_21','2017/7/23',''),(22,21,'ONMATH-909','haha_2','20-B','lib_id_22','2017/7/23',''),(23,21,'ONMATH-909','haha_3','21-A','lib_id_23','2017/7/23',''),(24,21,'ONMATH-909','haha_4','21-B','lib_id_24','2017/7/23',''),(25,21,'ONMATH-909','haha_5','22-A','lib_id_25','2017/7/23',''),(26,21,'ONMATH-909','haha_6','22-B','lib_id_26','2017/7/23',''),(27,21,'ONMATH-909','haha_7','123-A','lib_id_27','2017/7/23',''),(28,21,'ONMATH-909','haha_8','123-B','','2017/7/23','haha'),(29,21,'ONMATH-909','haha_9','131-A','lib_id_29','2017/7/23',''),(30,21,'ONMATH-909','haha_10','131-B','lib_id_30','2017/7/23','');
/*!40000 ALTER TABLE `build_lib` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `compare_table`
--

DROP TABLE IF EXISTS `compare_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `compare_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `master_id` int(11) DEFAULT NULL,
  `number` varchar(45) DEFAULT '',
  `comparison_name` varchar(45) DEFAULT '',
  `sample_group1` varchar(45) DEFAULT '',
  `sample_group2` varchar(45) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=116 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `compare_table`
--

LOCK TABLES `compare_table` WRITE;
/*!40000 ALTER TABLE `compare_table` DISABLE KEYS */;
INSERT INTO `compare_table` VALUES (4,2,'1','a vs b','',''),(5,2,'2','a vs c','',''),(6,2,'3','b vs c','',''),(99,1,'1','a vs c','a','c'),(100,1,'2','a vs d','a','d'),(101,1,'3','a vs f','a','f'),(102,1,'4','a vs g','a','g'),(103,1,'5','a vs t','a','t'),(104,1,'6','a vs u','a','u'),(105,1,'8','c vs f','c','f'),(106,1,'9','c vs g','c','g'),(107,1,'10','c vs t','c','t'),(108,1,'11','c vs u','c','u'),(109,1,'12','d vs f','d','f'),(110,1,'15','d vs u','d','u'),(111,1,'17','f vs t','f','t'),(112,1,'18','f vs u','f','u'),(113,1,'19','g vs t','g','t'),(114,1,'20','g vs u','g','u'),(115,1,'21','t vs u','t','u');
/*!40000 ALTER TABLE `compare_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (13,'admin','logentry'),(14,'auth','group'),(15,'auth','permission'),(16,'auth','user'),(17,'contenttypes','contenttype'),(7,'lims_app','analysismaster'),(20,'lims_app','attachment'),(21,'lims_app','buildlib'),(4,'lims_app','comparetable'),(3,'lims_app','dnasamplesequencingtype'),(22,'lims_app','downmachine'),(23,'lims_app','qualitycheck'),(1,'lims_app','rnasamplesequencingtype'),(2,'lims_app','sampleinfodetail'),(6,'lims_app','sampleother'),(11,'lims_app','samplepacketinformation'),(10,'lims_app','sampleprojectmaster'),(5,'lims_app','samplespecies'),(12,'lims_app','sampletable'),(8,'lims_app','sampletype'),(24,'lims_app','sendsample'),(25,'lims_app','upmachine'),(9,'lims_app','userinfo'),(18,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2017-07-12 03:30:40.600684'),(2,'auth','0001_initial','2017-07-12 03:30:40.965202'),(3,'admin','0001_initial','2017-07-12 03:30:41.058305'),(4,'admin','0002_logentry_remove_auto_add','2017-07-12 03:30:41.097611'),(5,'contenttypes','0002_remove_content_type_name','2017-07-12 03:30:41.208266'),(6,'auth','0002_alter_permission_name_max_length','2017-07-12 03:30:41.226065'),(7,'auth','0003_alter_user_email_max_length','2017-07-12 03:30:41.260247'),(8,'auth','0004_alter_user_username_opts','2017-07-12 03:30:41.295657'),(9,'auth','0005_alter_user_last_login_null','2017-07-12 03:30:41.357521'),(10,'auth','0006_require_contenttypes_0002','2017-07-12 03:30:41.360852'),(11,'auth','0007_alter_validators_add_error_messages','2017-07-12 03:30:41.395658'),(12,'auth','0008_alter_user_username_max_length','2017-07-12 03:30:41.452646'),(13,'lims_app','0001_initial','2017-07-12 03:30:41.554545'),(14,'sessions','0001_initial','2017-07-12 03:30:41.582778'),(15,'lims_app','0002_auto_20170719_0313','2017-07-19 03:14:03.448549'),(16,'lims_app','0003_auto_20170719_0315','2017-07-19 03:18:25.153565'),(17,'lims_app','0004_auto_20170719_0318','2017-07-19 03:18:25.186579'),(18,'lims_app','0005_auto_20170719_0706','2017-07-19 07:06:53.628195'),(19,'lims_app','0006_projectfile','2017-07-28 07:01:43.409207'),(20,'lims_app','0006_attachment_buildlib_downmachine_qualitycheck_sendsample_upmachine','2017-08-02 07:34:22.838108');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('hmwj1gg2dly5ouswz7hamagw3cxlyh2z','YjRiNzk3YzU5ZmUyNzBiOGU0Y2QzYTU1ZDdmN2NhMTkyYzlmMDZiYTp7InVzZXJuYW1lIjoibXl0ZXN0In0=','2017-08-24 09:24:43.112568'),('pqt3hmpvztgig93do4l1nprly8inu9pd','YjRiNzk3YzU5ZmUyNzBiOGU0Y2QzYTU1ZDdmN2NhMTkyYzlmMDZiYTp7InVzZXJuYW1lIjoibXl0ZXN0In0=','2017-08-28 01:21:46.440402');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dna_sample_sequencing_type`
--

DROP TABLE IF EXISTS `dna_sample_sequencing_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dna_sample_sequencing_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `resequencing` varchar(1) DEFAULT 'Y',
  `de_novo_sequencing` varchar(1) DEFAULT 'Y',
  `mate_pair` varchar(1) DEFAULT 'Y',
  `low_initial_weight_sequencing` varchar(1) DEFAULT 'Y',
  `exome` varchar(1) DEFAULT 'Y',
  `target_area_capture` varchar(1) DEFAULT 'Y',
  `purified` varchar(1) DEFAULT 'Y',
  `unpurified` varchar(1) DEFAULT 'Y',
  `d16s_rdna` varchar(1) DEFAULT 'Y',
  `rad` varchar(1) DEFAULT 'Y',
  `metagenome` varchar(1) DEFAULT 'Y',
  `chip_seq` varchar(1) DEFAULT 'Y',
  `dna_methylation_sequencing` varchar(1) DEFAULT 'Y',
  `rrbs` varchar(1) DEFAULT 'Y',
  `medip_seq` varchar(1) DEFAULT 'Y',
  `mitochondrial_dna_sequencing` varchar(1) DEFAULT 'Y',
  `dna_sample_sequencing_type_other` varchar(45) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dna_sample_sequencing_type`
--

LOCK TABLES `dna_sample_sequencing_type` WRITE;
/*!40000 ALTER TABLE `dna_sample_sequencing_type` DISABLE KEYS */;
INSERT INTO `dna_sample_sequencing_type` VALUES (1,1,'N','Y','N','N','N','N','N','N','N','N','N','N','N','N','N','Y',''),(2,2,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(3,3,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(4,4,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(5,5,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(6,6,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(7,7,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(8,8,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(9,10,'N','N','N','N','N','N','N','N','Y','N','N','N','N','N','N','N',''),(10,12,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(11,13,'Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','Y','1'),(12,14,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(13,17,'N','N','N','N','N','Y','N','N','N','N','N','N','N','N','N','N',''),(14,18,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(15,19,'N','N','N','N','N','Y','N','N','N','N','N','N','N','N','N','N',''),(16,20,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N',''),(17,21,'N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','N','');
/*!40000 ALTER TABLE `dna_sample_sequencing_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `downmachine`
--

DROP TABLE IF EXISTS `downmachine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `downmachine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` varchar(45) DEFAULT NULL,
  `project_number` varchar(45) DEFAULT NULL,
  `sample_name` varchar(45) DEFAULT NULL,
  `sample_id` varchar(45) DEFAULT NULL,
  `data_count` varchar(45) DEFAULT NULL,
  `q20` varchar(45) DEFAULT NULL,
  `q30` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample_id_UNIQUE` (`sample_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `downmachine`
--

LOCK TABLES `downmachine` WRITE;
/*!40000 ALTER TABLE `downmachine` DISABLE KEYS */;
INSERT INTO `downmachine` VALUES (1,'12','ONMATH-900','sample_name_1','10-A','4','23','23','2017/7/2',''),(2,'12','ONMATH-900','sample_name_2','10-B','3','22','','2017/7/2',''),(3,'12','ONMATH-900','sample_name_3','11-A','4','22','','2017/7/2',''),(4,'12','ONMATH-900','sample_name_4','11-B','3','32','32','2017/7/2','test'),(5,'12','ONMATH-900','sample_name_5','12-A','3','22','','2017/7/2',''),(6,'12','ONMATH-900','sample_name_6','12-B','','','','2017/7/2',''),(7,'12','ONMATH-900','sample_name_7','13-A','4','32','','2017/7/2',''),(8,'12','ONMATH-900','sample_name_8','13-B','','','','2017/7/2',''),(9,'12','ONMATH-900','sample_name_9','14-A','2','32','','2017/7/2',''),(10,'12','ONMATH-900','sample_name_10','14-B','','','','2017/7/2','test'),(11,'14','ONMATH-903','test_1','15-A','2','','','2017/7/8',''),(12,'14','ONMATH-903','test_2','15-B','2','','2','2017/7/8',''),(13,'14','ONMATH-903','test_3','16-A','2','','','2017/7/8',''),(14,'14','ONMATH-903','test_4','16-B','2','','','2017/7/8',''),(15,'14','ONMATH-903','test_5','17-A','2','','','2017/7/8',''),(16,'14','ONMATH-903','test_6','17-B','2','','32','2017/7/8',''),(17,'14','ONMATH-903','test_7','18-A','2','','','2017/7/8',''),(18,'14','ONMATH-903','test_8','18-B','2','','','2017/7/8',''),(19,'14','ONMATH-903','test_9','19-A','2','','','2017/7/8',''),(20,'14','ONMATH-903','test_10','19-B','2','','','2017/7/30',''),(21,'21','ONMATH-909','haha_1','20-A','','','32','2017/7/30',''),(22,'21','ONMATH-909','haha_2','20-B','','','','2017/7/30','test'),(23,'21','ONMATH-909','haha_3','21-A','','','','2017/7/30',''),(24,'21','ONMATH-909','haha_4','21-B','6','','','2017/7/30',''),(25,'21','ONMATH-909','haha_5','22-A','','','32','2017/7/30',''),(26,'21','ONMATH-909','haha_6','22-B','','','32','2017/7/30',''),(27,'21','ONMATH-909','haha_7','123-A','4','','','2017/7/30',''),(28,'21','ONMATH-909','haha_8','123-B','','','','2017/7/30',''),(29,'21','ONMATH-909','haha_9','131-A','','','','2017/7/30',''),(30,'21','ONMATH-909','haha_10','131-B','','','','2017/7/30','');
/*!40000 ALTER TABLE `downmachine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_file`
--

DROP TABLE IF EXISTS `project_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_number` varchar(45) NOT NULL,
  `receive_sample` varchar(100) NOT NULL,
  `quality_check` varchar(100) NOT NULL,
  `build_lib` varchar(100) NOT NULL,
  `upmachine` varchar(100) NOT NULL,
  `downmachine` varchar(100) NOT NULL,
  `receive_sample_name` varchar(45) NOT NULL,
  `quality_check_name` varchar(45) NOT NULL,
  `build_lib_name` varchar(45) NOT NULL,
  `upmachine_name` varchar(45) NOT NULL,
  `downmachine_name` varchar(45) NOT NULL,
  `receive_sample_time` varchar(45) NOT NULL,
  `quality_check_time` varchar(45) NOT NULL,
  `build_lib_time` varchar(45) NOT NULL,
  `upmachine_time` varchar(45) NOT NULL,
  `downmachine_time` varchar(45) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_file`
--

LOCK TABLES `project_file` WRITE;
/*!40000 ALTER TABLE `project_file` DISABLE KEYS */;
/*!40000 ALTER TABLE `project_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `project_log_table`
--

DROP TABLE IF EXISTS `project_log_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `project_log_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `action` varchar(45) DEFAULT NULL,
  `time` varchar(45) NOT NULL DEFAULT '',
  `manager` varchar(45) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `id_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `project_log_table`
--

LOCK TABLES `project_log_table` WRITE;
/*!40000 ALTER TABLE `project_log_table` DISABLE KEYS */;
INSERT INTO `project_log_table` VALUES (1,17,'create new project','2017-06-23 19:30:30.894540','test'),(2,1,'update this project','2017-06-23 19:51:38.088722','chencheng'),(3,2,'update this project','2017-06-23 19:51:58.351498','chencheng'),(4,3,'update this project','2017-06-23 19:53:47.993243','chencheng'),(6,17,'update this project','2017-06-23 19:55:54.008688','chencheng'),(7,12,'update this project','2017-06-23 20:00:26.456569','chencheng'),(8,10,'update this project','2017-06-23 20:15:52.566531','chencheng'),(9,17,'update this project','2017-06-23 20:17:03.770256','chencheng'),(10,18,'create new project','2017-07-14 11:29:39.204416','haha'),(11,2,'update this project','2017-07-17 10:08:05.323935','chencheng'),(12,19,'create new project','2017-07-17 11:11:43.202612','haha'),(13,20,'create new project','2017-07-17 15:28:01.674630','haha'),(14,20,'update this project','2017-07-17 15:43:37.633050','chencheng'),(15,10,'update sample table','2017-07-17 16:26:16.997284','chencheng'),(16,19,'update sample table','2017-07-17 16:34:34.168200','haha'),(17,10,'update this project','2017-07-17 16:51:06.519168','chencheng'),(18,20,'update sample table','2017-07-17 17:06:01.451036','chencheng'),(19,21,'create new project','2017-07-20 18:58:41.178126','haha'),(20,21,'create sample table','2017-07-20 18:58:53.787388','haha');
/*!40000 ALTER TABLE `project_log_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `quality_check`
--

DROP TABLE IF EXISTS `quality_check`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `quality_check` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `project_number` varchar(45) DEFAULT NULL,
  `sample_name` varchar(45) DEFAULT NULL,
  `sample_id` varchar(45) DEFAULT NULL,
  `concentration` varchar(45) DEFAULT NULL,
  `volume` varchar(45) DEFAULT NULL,
  `rin` varchar(45) DEFAULT NULL,
  `results` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample_id_UNIQUE` (`sample_id`)
) ENGINE=InnoDB AUTO_INCREMENT=41 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `quality_check`
--

LOCK TABLES `quality_check` WRITE;
/*!40000 ALTER TABLE `quality_check` DISABLE KEYS */;
INSERT INTO `quality_check` VALUES (1,12,'ONMATH-900','sample_name_1','10-A','11','3','','A','2017/6/28',''),(2,12,'ONMATH-900','sample_name_2','10-B','','','','A','2017/6/28',''),(3,12,'ONMATH-900','sample_name_3','11-A','3','','43','A','2017/6/28',''),(4,12,'ONMATH-900','sample_name_4','11-B','','','','A','2017/6/28',''),(5,12,'ONMATH-900','sample_name_5','12-A','','','','A','2017/6/28',''),(6,12,'ONMATH-900','sample_name_6','12-B','','3','','B','2017/6/28','haha'),(7,12,'ONMATH-900','sample_name_7','13-A','','','','A','2017/6/28',''),(8,12,'ONMATH-900','sample_name_8','13-B','','','23','A','2017/6/28',''),(9,12,'ONMATH-900','sample_name_9','14-A','','','','A','2017/6/28',''),(10,12,'ONMATH-900','sample_name_10','14-B','','','','A','2017/6/28',''),(11,14,'ONMATH-903','test_1','15-A','','','','A','2017/7/1',''),(12,14,'ONMATH-903','test_2','15-B','','','','B','2017/7/1',''),(13,14,'ONMATH-903','test_3','16-A','','3','','A','2017/7/1',''),(14,14,'ONMATH-903','test_4','16-B','43','','','C','2017/7/1',''),(15,14,'ONMATH-903','test_5','17-A','','','','A','2017/7/1',''),(16,14,'ONMATH-903','test_6','17-B','','','','A','2017/7/1','haha'),(17,14,'ONMATH-903','test_7','18-A','','','23','A','2017/7/1',''),(18,14,'ONMATH-903','test_8','18-B','','3','','A','2017/7/1',''),(19,14,'ONMATH-903','test_9','19-A','','','','A','2017/7/1',''),(20,14,'ONMATH-903','test_10','19-B','','','','C','2017/7/21',''),(21,21,'ONMATH-909','haha_1','20-A','','','43','A','2017/7/21',''),(22,21,'ONMATH-909','haha_2','20-B','','','','A','2017/7/21',''),(23,21,'ONMATH-909','haha_3','21-A','43','4','','D','2017/7/21',''),(24,21,'ONMATH-909','haha_4','21-B','','','','D','2017/7/21',''),(25,21,'ONMATH-909','haha_5','22-A','','','','D','2017/7/21','haha'),(26,21,'ONMATH-909','haha_6','22-B','3','','','D','2017/7/21',''),(27,21,'ONMATH-909','haha_7','123-A','','','43','D','2017/7/21',''),(28,21,'ONMATH-909','haha_8','123-B','','4','','D','2017/7/21',''),(29,21,'ONMATH-909','haha_9','131-A','43','','','D','2017/7/21',''),(30,21,'ONMATH-909','haha_10','131-B','','4','','D','2017/7/21',''),(31,21,'ONMATH-909','Haha_1','test_id_1','','','','D','','haha'),(32,21,'ONMATH-909','Haha_2','test_id_2','3','','1','A','','test'),(33,21,'ONMATH-909','Haha_3','test_id_3','','','','A','',''),(34,21,'ONMATH-909','Haha_4','test_id_4','','','','A','',''),(35,21,'ONMATH-909','Haha_5','test_id_5','','1','','C','',''),(36,21,'ONMATH-909','Haha_6','test_id_6','','','','A','',''),(37,21,'ONMATH-909','Haha_7','test_id_7','','','3','A','','haha'),(38,21,'ONMATH-909','Haha_8','test_id_8','','','','A','',''),(39,21,'ONMATH-909','Haha_9','test_id_9','5','','6','D','',''),(40,21,'ONMATH-909','Haha_10','test_id_10','','','','A','','');
/*!40000 ALTER TABLE `quality_check` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receive_sample`
--

DROP TABLE IF EXISTS `receive_sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `receive_sample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sample_id` varchar(45) NOT NULL,
  `project_number` varchar(45) NOT NULL,
  `express_number` varchar(45) NOT NULL,
  `comment` varchar(100) DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample_id_UNIQUE` (`sample_id`),
  UNIQUE KEY `project_id_UNIQUE` (`project_number`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receive_sample`
--

LOCK TABLES `receive_sample` WRITE;
/*!40000 ALTER TABLE `receive_sample` DISABLE KEYS */;
/*!40000 ALTER TABLE `receive_sample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rna_sample_sequencing_type`
--

DROP TABLE IF EXISTS `rna_sample_sequencing_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rna_sample_sequencing_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `three_eukaryotic_mrna_seq` varchar(1) DEFAULT 'Y',
  `mrna_seq_prokaryotae` varchar(1) DEFAULT 'Y',
  `low_initial_amount_of_eukaryotic_mrna_seq` varchar(1) DEFAULT 'Y',
  `strand_specific_transcriptome` varchar(1) DEFAULT 'Y',
  `incrna_seq` varchar(1) DEFAULT 'Y',
  `c_dna_transcriptome` varchar(1) DEFAULT 'Y',
  `cdna_single_cell_transcriptom` varchar(1) DEFAULT 'Y',
  `small_rna_sequencing` varchar(1) DEFAULT 'Y',
  `plasma_small_rna_equencing` varchar(1) DEFAULT 'Y',
  `rna_sample_sequencing_type_other` varchar(45) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rna_sample_sequencing_type`
--

LOCK TABLES `rna_sample_sequencing_type` WRITE;
/*!40000 ALTER TABLE `rna_sample_sequencing_type` DISABLE KEYS */;
INSERT INTO `rna_sample_sequencing_type` VALUES (1,1,'N','N','N','N','N','N','N','N','N',''),(2,2,'N','N','N','N','N','N','N','N','N',''),(3,3,'N','N','N','N','N','N','N','N','N',''),(4,10,'N','N','N','N','N','N','N','Y','N',''),(5,12,'N','N','N','N','N','N','N','N','Y',''),(6,13,'Y','Y','Y','Y','Y','Y','Y','Y','Y','1'),(7,14,'N','N','N','N','N','N','N','N','N',''),(8,17,'Y','N','N','N','N','N','N','Y','N',''),(9,18,'N','N','N','N','N','N','N','N','N',''),(10,19,'N','N','N','N','N','N','N','Y','N',''),(11,20,'N','N','N','N','Y','N','N','Y','N',''),(12,21,'N','N','N','N','N','N','N','N','N','');
/*!40000 ALTER TABLE `rna_sample_sequencing_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_info_detail`
--

DROP TABLE IF EXISTS `sample_info_detail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_info_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `project_number` varchar(45) NOT NULL,
  `sample_name` varchar(45) DEFAULT NULL,
  `sample_id` varchar(45) NOT NULL,
  `express_number` varchar(45) DEFAULT NULL,
  `product_num` varchar(45) DEFAULT NULL,
  `sendsample_time` varchar(45) DEFAULT NULL,
  `sendsample_comment` varchar(100) DEFAULT NULL,
  `rin` varchar(45) DEFAULT NULL,
  `concentration` varchar(45) DEFAULT NULL,
  `volume` varchar(45) DEFAULT NULL,
  `qualitycheck_results` varchar(1) DEFAULT NULL,
  `qualitycheck_time` varchar(45) DEFAULT NULL,
  `qualitycheck_comment` varchar(100) DEFAULT NULL,
  `lib_id` varchar(45) DEFAULT NULL,
  `lib_time` varchar(45) DEFAULT NULL,
  `lib_comment` varchar(100) DEFAULT NULL,
  `upmachine_comment` varchar(100) DEFAULT NULL,
  `upmachine_time` varchar(45) DEFAULT NULL,
  `upmachine_num` varchar(45) DEFAULT NULL,
  `upmachine_type` varchar(45) DEFAULT NULL,
  `upmachine_mode` varchar(45) DEFAULT NULL,
  `downmachine_num` varchar(45) DEFAULT NULL,
  `downmachine_time` varchar(45) DEFAULT NULL,
  `downmachine_comment` varchar(100) DEFAULT NULL,
  `q20` varchar(45) DEFAULT NULL,
  `q30` varchar(45) DEFAULT NULL,
  `id_alias` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample_id_UNIQUE` (`sample_id`),
  UNIQUE KEY `id_alias_UNIQUE` (`id_alias`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_info_detail`
--

LOCK TABLES `sample_info_detail` WRITE;
/*!40000 ALTER TABLE `sample_info_detail` DISABLE KEYS */;
INSERT INTO `sample_info_detail` VALUES (11,14,'ONMATH-903','test_1','15-A','41343242','1','2017/6/28','','','','','A','2017/7/1','','','2017/7/3','','','2017/7/5','2','','','2017/7/8','','2','','',NULL),(12,14,'ONMATH-903','test_2','15-B','41343242','1','2017/6/28','','','','','B','2017/7/1','','lib_id_12','2017/7/3','','','2017/7/5','2','','','2017/7/8','','2','','2',NULL),(13,14,'ONMATH-903','test_3','16-A','','1','2017/6/28','','','3','','A','2017/7/1','','lib_id_13','2017/7/3','','','2017/7/5','2','','','2017/7/8','','2','','',NULL),(14,14,'ONMATH-903','test_4','16-B','41435354','1','2017/6/28','','43','','','C','2017/7/1','','lib_id_14','2017/7/3','','','2017/7/5','2','','','2017/7/8','','2','','',NULL),(15,14,'ONMATH-903','test_5','17-A','41435354','1','2017/6/28','','','','','A','2017/7/1','','lib_id_15','2017/7/3','','test','2017/7/5','2','','','2017/7/8','','2','','',NULL),(16,14,'ONMATH-903','test_6','17-B','41435354','1','2017/6/28','','','','','A','2017/7/1','haha','lib_id_16','2017/7/3','','','2017/7/5','2','','','2017/7/8','','2','','32',NULL),(17,14,'ONMATH-903','test_7','18-A','41435354','1','2017/6/28','','','','23','A','2017/7/1','','lib_id_17','2017/7/3','','','2017/7/5','2','','','2017/7/8','','2','','',NULL),(18,14,'ONMATH-903','test_8','18-B','41435354','1','2017/6/28','','','3','','A','2017/7/1','','lib_id_18','2017/7/3','','','2017/7/5','2','','','2017/7/8','','2','','',NULL),(19,14,'ONMATH-903','test_9','19-A','41435354','1','2017/6/28','','','','','A','2017/7/1','','lib_id_19','2017/7/3','haha','','2017/7/5','2','','','2017/7/8','','2','','',NULL),(20,14,'ONMATH-903','test_10','19-B','','1','2017/7/17','','','','','C','2017/7/21','','','2017/7/23','','','2017/7/25','2','','','2017/7/30','','2','','',NULL),(21,21,'ONMATH-909','haha_1','20-A','1213','1','2017/7/17','','','','43','A','2017/7/21','','lib_id_21','2017/7/23','','','2017/7/25','','','','2017/7/30','','','','32',NULL),(22,21,'ONMATH-909','haha_2','20-B','','1','2017/7/17','','','','','A','2017/7/21','','lib_id_22','2017/7/23','','','2017/7/25','','','','2017/7/30','test','','','',NULL),(23,21,'ONMATH-909','haha_3','21-A','','2','2017/7/17','','43','4','','D','2017/7/21','','lib_id_23','2017/7/23','','test','2017/7/25','','','','2017/7/30','','','','',NULL),(24,21,'ONMATH-909','haha_4','21-B','','3','2017/7/17','haha','','','','D','2017/7/21','','lib_id_24','2017/7/23','','','2017/7/25','6','','','2017/7/30','','6','','',NULL),(25,21,'ONMATH-909','haha_5','22-A','35352354','','2017/7/17','','','','','D','2017/7/21','haha','lib_id_25','2017/7/23','','','2017/7/25','','','','2017/7/30','','','','32',NULL),(26,21,'ONMATH-909','haha_6','22-B','35352354','2','2017/7/17','','3','','','D','2017/7/21','','lib_id_26','2017/7/23','','','2017/7/25','','','','2017/7/30','','','','32',NULL),(27,21,'ONMATH-909','haha_7','123-A','35352354','1','2017/7/17','','','','43','D','2017/7/21','dsd','lib_id_27','2017/7/23','','saad','2017/7/25','5','','','2017/7/30','','4','','',NULL),(28,21,'ONMATH-909','haha_8','123-B','35352354','','2017/7/17','','','4','','D','2017/7/21','','','2017/7/23','haha','','2017/7/25','','','','2017/7/30','','','','',NULL),(29,21,'ONMATH-909','haha_9','131-A','35352354','','2017/7/17','','43','','','D','2017/7/21','','lib_id_29','2017/7/23','','','2017/7/25','','','','2017/7/30','','','','',NULL),(30,21,'ONMATH-909','haha_10','131-B','35352354','2','2017/7/17','df','','4','','D','2017/7/21','','lib_id_30','2017/7/23','','','2017/7/25','','','','2017/7/30','','','','',NULL);
/*!40000 ALTER TABLE `sample_info_detail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_other`
--

DROP TABLE IF EXISTS `sample_other`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_other` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `reagent_kit_method` varchar(1) DEFAULT 'N',
  `ctab_method` varchar(1) DEFAULT 'N',
  `trizol_method` varchar(1) DEFAULT 'N',
  `other_method` varchar(45) DEFAULT '',
  `berry_handel` varchar(1) DEFAULT 'N',
  `ret_handel` varchar(1) DEFAULT 'N',
  `other_handel` varchar(45) DEFAULT '',
  `accord_contract` varchar(1) DEFAULT 'N',
  `special_needs` varchar(1) DEFAULT 'N',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_other`
--

LOCK TABLES `sample_other` WRITE;
/*!40000 ALTER TABLE `sample_other` DISABLE KEYS */;
INSERT INTO `sample_other` VALUES (1,1,'Y','Y','Y','','N','N','','N','N'),(2,2,'N','N','N','','N','N','','N','N'),(3,3,'N','N','N','','N','N','','N','N'),(4,10,'N','N','N','','N','N','','N','N'),(5,12,'N','N','N','','N','N','','N','N'),(6,13,'N','N','N','','N','N','','N','N'),(7,14,'N','N','N','','N','N','','N','N'),(8,17,'N','N','N','','N','N','','N','N'),(9,18,'N','N','N','','N','N','','N','N'),(10,19,'N','N','N','','N','N','','N','N'),(11,20,'N','N','N','','N','N','','N','N'),(12,21,'N','N','N','','N','N','','N','N');
/*!40000 ALTER TABLE `sample_other` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_packet_information`
--

DROP TABLE IF EXISTS `sample_packet_information`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_packet_information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `master_id` int(11) DEFAULT NULL,
  `sample_id_alias` varchar(45) DEFAULT NULL,
  `sample_group` varchar(45) DEFAULT '',
  `repeated_experiment` varchar(45) DEFAULT '',
  `sample_name` varchar(45) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=75 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_packet_information`
--

LOCK TABLES `sample_packet_information` WRITE;
/*!40000 ALTER TABLE `sample_packet_information` DISABLE KEYS */;
INSERT INTO `sample_packet_information` VALUES (4,2,NULL,'a','',''),(5,2,NULL,'b','',''),(6,2,NULL,'c','',''),(67,1,'OM-006','a','','399-45R'),(68,1,'OM-006','c','','399-45R'),(69,1,'OM-007','d','','12312df'),(70,1,'OM-005','f','','测死'),(71,1,'OM-007','g','','12312df'),(72,1,'OM-007','t','','12312df'),(73,1,'OM-0010','u','','ddd33'),(74,1,'OM-007','y','','12312df');
/*!40000 ALTER TABLE `sample_packet_information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_project_master`
--

DROP TABLE IF EXISTS `sample_project_master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_project_master` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_number` varchar(45) NOT NULL,
  `project_name` text,
  `cust_organization` text,
  `cust_user` varchar(45) DEFAULT '',
  `email` varchar(45) DEFAULT '',
  `cust_tel` varchar(45) DEFAULT '',
  `sale_name` varchar(45) DEFAULT '',
  `sp_delive_date` varchar(45) DEFAULT '',
  `sp_sum` varchar(45) DEFAULT '',
  `species` varchar(45) DEFAULT '',
  `project_leader` varchar(45) DEFAULT '陈中旭',
  `status` varchar(45) DEFAULT '等待送样',
  `created_by` varchar(45) DEFAULT '',
  `create_time` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `project_number` (`project_number`)
) ENGINE=InnoDB AUTO_INCREMENT=22 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_project_master`
--

LOCK TABLES `sample_project_master` WRITE;
/*!40000 ALTER TABLE `sample_project_master` DISABLE KEYS */;
INSERT INTO `sample_project_master` VALUES (6,'ONMATH-6',NULL,NULL,'tttetset',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'wait_send',NULL,'2017-06-06'),(7,'ONMATH-7',NULL,NULL,'tttetset',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'wait_send',NULL,'2017-06-06'),(8,'ONMATH-8','testttt','','tttetset','','','','','','','chencheng','wait_send','test','2017-06-06 09:14:44.235154'),(10,'ONMATH-10','11231231','','213123123','','','','','','','chencheng','wait_send','test','2017-06-06 09:18:10.389281'),(12,'ONMATH-900','4444','','5555','','','','','','','chencheng','send_sample','test','2017-06-06 09:26:42.492849'),(14,'ONMATH-903','test-test','test','test--test','','','','','','','chencheng','send_sample','test','2017-06-07 04:41:18.758856'),(15,'ONMATH-904','haha','','haha','','','','','','','chencheng','wait_send','test','2017-06-23 19:26:43.477432'),(16,'ONMATH-905','haha','','haha','','','','','','','chencheng','wait_send','test','2017-06-23 19:29:26.224983'),(17,'ONMATH-906','haha','','haha','','','','','','','chencheng','wait_send','test','2017-06-23 19:30:30.841083'),(19,'ONMATH-907','test_project1','四川农业大学','haha','haha@haha.com','','','','','','chencheng','wait_send','haha','2017-07-17 11:11:43.131307'),(20,'ONMATH-908','test_project2','四川农业大学','haha','haha@haha.com','','','','','鸡','chencheng','wait_send','haha','2017-07-17 15:28:01.598447'),(21,'ONMATH-909','haha',NULL,'fafa',NULL,NULL,NULL,NULL,NULL,NULL,NULL,'downmachine',NULL,'2017-07-20');
/*!40000 ALTER TABLE `sample_project_master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_species`
--

DROP TABLE IF EXISTS `sample_species`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_species` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `lyophillization` varchar(1) DEFAULT 'Y',
  `te_buffer` varchar(1) DEFAULT 'Y',
  `ddh2o` varchar(1) DEFAULT 'N',
  `depc` varchar(1) DEFAULT 'N',
  `sample_species_other` varchar(45) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_species`
--

LOCK TABLES `sample_species` WRITE;
/*!40000 ALTER TABLE `sample_species` DISABLE KEYS */;
INSERT INTO `sample_species` VALUES (1,1,'N','N','N','N',''),(2,2,'Y','N','N','N',''),(3,3,'Y','N','N','N',''),(4,4,'N','N','N','N',''),(5,5,'N','N','N','N',''),(6,6,'N','N','N','N',''),(7,7,'N','N','N','N',''),(8,8,'N','N','N','N',''),(9,10,'N','Y','N','N',''),(10,12,'N','N','N','N',''),(11,13,'Y','Y','Y','Y','1'),(12,14,'N','N','N','N',''),(13,17,'Y','N','N','N',''),(14,18,'N','N','N','N',''),(15,19,'Y','N','N','N',''),(16,20,'Y','N','N','N',''),(17,21,'Y','N','N','N','');
/*!40000 ALTER TABLE `sample_species` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_table`
--

DROP TABLE IF EXISTS `sample_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_table` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `sample_name` char(50) DEFAULT NULL,
  `sepcies` char(50) DEFAULT NULL,
  `product_num` char(50) DEFAULT NULL,
  `library_type` char(50) DEFAULT NULL,
  `concentration` char(50) DEFAULT NULL,
  `volume` char(50) DEFAULT NULL,
  `data_quantity` char(50) DEFAULT NULL,
  `fragment_length` char(50) DEFAULT NULL,
  `od_260_or_280` char(50) DEFAULT NULL,
  `od_260_or_230` char(50) DEFAULT NULL,
  `comment` char(50) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample_table_id_uindex` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=188 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_table`
--

LOCK TABLES `sample_table` WRITE;
/*!40000 ALTER TABLE `sample_table` DISABLE KEYS */;
INSERT INTO `sample_table` VALUES (20,1,'sample_name','狗','2','','3','','12','5','2','3','haha'),(21,1,'sample_name','狗','2','','4','','12','5','2','3',''),(22,1,'sample_name','狗','2','','7','','12','5','2','3',''),(23,1,'wwww','www','www','www','ww','w','w','w','w','w','w'),(24,1,'2','2','2','2','2','2','2','2','2','2','2'),(25,1,'1111','111','1','1','1','1','1','1','1','1','1'),(26,1,'3','3','3','3','3','3','3','3','3','3','3'),(36,12,'sample_name','狗','2','','3','','12','5','2','3','haha'),(37,12,'sample_name','狗','2','','2','','12','5','2','3',''),(38,12,'sample_name','狗','2','','2','','12','5','2','3',''),(39,12,'sample_name','狗','2','','3','','12','5','2','3',''),(40,12,'sample_name','狗','2','','4','','12','5','2','3',''),(41,13,'1','1','1','1','1','1','1','1','1','1','1'),(42,14,'sample_name','狗','2','','3','','12','5','2','3','haha'),(43,14,'sample_name','狗','2','','2','','12','5','2','3',''),(44,14,'sample_name','狗','2','','1','','12','5','2','3',''),(45,14,'sample_name','狗','2','','2','','12','5','2','3',''),(46,14,'sample_name','狗','2','','3','','12','5','2','3',''),(47,14,'sample_name','狗','2','','3','','12','5','2','3',''),(48,14,'sample_name','狗','2','','4','','12','5','2','3',''),(49,14,'sample_name','狗','2','','5','','12','5','2','3',''),(50,14,'sample_name','狗','2','','7','','12','5','2','3',''),(51,14,'dafadsf','猫','3','4','5','8','9','0','-','=','2'),(153,19,'test1','鸡','2','','','','','','','',''),(154,19,'test2','鸡','1','','','','','','','',''),(155,19,'test3','鸡','1','','','','','','','',''),(156,19,'test4','鸡','1','','','','','','','',''),(157,19,'test5','鸡','1','','','','','','','',''),(158,19,'test6','鸡','1','','','','','','','',''),(159,19,'test7','鸡','1','','','','','','','',''),(160,19,'test8','鸡','1','','','','','','','',''),(161,19,'test9','鸡','1','','','','','','','',''),(162,19,'test10','鸡','3','','','','','','','',''),(163,19,'test11','鸡','1','','','','','','','',''),(164,19,'test1','鸡','2','','','','','','','',''),(165,19,'test13','鸡','1','','','','','','','',''),(166,19,'test3','鸡','1','','','','','','','',''),(167,19,'test4','鸡','1','','','','','','','',''),(168,19,'test5','鸡','1','','','','','','','',''),(169,19,'test6','鸡','1','','','','','','','',''),(170,19,'test7','鸡','1','','','','','','','',''),(171,19,'test8','鸡','1','','','','','','','',''),(172,19,'test9','鸡','1','','','','','','','',''),(173,19,'test10','鸡','3','','','','','','','',''),(174,19,'test11','鸡','1','','','','','','','',''),(175,20,'test1','鸡','2','','','','','','','',''),(176,20,'test2','鸡','2','dna','','','','','','',''),(177,20,'test3','鸡','1','','','','','','','',''),(178,20,'test4','鸡','1','','','','','','','',''),(179,20,'test5','鸡','1','','','','','','','',''),(180,20,'test6','鸡','1','','','','','','','',''),(181,20,'test7','鸡','1','','','','','','','',''),(182,20,'test8','鸡','1','','','','','','','',''),(183,20,'test9','鸡','1','','','','','','','',''),(184,20,'test10','鸡','3','','','','','','','',''),(185,20,'test11','鸡','1','','','','','','','',''),(186,10,'test1212','','','','','','','','','',''),(187,21,'da','da','da','','','','da','','da','da','');
/*!40000 ALTER TABLE `sample_table` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sample_type`
--

DROP TABLE IF EXISTS `sample_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sample_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) NOT NULL,
  `genomic_dna` varchar(1) DEFAULT 'Y',
  `chip_dna` varchar(1) DEFAULT 'Y',
  `pcr_fragment` varchar(1) DEFAULT 'Y',
  `free_dna` varchar(1) DEFAULT 'Y',
  `mitochondrial_dna` varchar(1) DEFAULT 'Y',
  `others_dna` varchar(45) DEFAULT '',
  `total_rna` varchar(1) DEFAULT 'Y',
  `to_ribosomal_rna` varchar(1) DEFAULT 'Y',
  `small_rna` varchar(1) DEFAULT 'Y',
  `c_dna` varchar(1) DEFAULT 'Y',
  `plasma_rna` varchar(1) DEFAULT 'Y',
  `other_rna` varchar(45) DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sample_type`
--

LOCK TABLES `sample_type` WRITE;
/*!40000 ALTER TABLE `sample_type` DISABLE KEYS */;
INSERT INTO `sample_type` VALUES (1,1,'N','N','N','N','N','','N','N','N','N','N',''),(2,2,'N','N','N','N','N','','N','N','N','N','N',''),(3,3,'N','N','N','N','N','','N','N','N','N','N',''),(4,4,'N','N','N','N','N','','N','N','N','N','N',''),(5,5,'N','N','N','N','N','','N','N','N','N','N',''),(6,6,'N','N','N','N','N','','N','N','N','N','N',''),(7,7,'N','N','N','N','N','','N','N','N','N','N',''),(8,8,'N','N','N','N','N','','N','N','N','N','N',''),(9,10,'N','N','N','N','N','','N','N','N','N','N',''),(10,12,'N','N','N','N','N','','N','N','N','N','N',''),(11,13,'Y','Y','Y','Y','Y','1','Y','Y','Y','Y','Y','1'),(12,14,'N','N','N','N','N','','N','N','N','N','N',''),(13,17,'N','N','N','N','N','','N','N','N','N','N',''),(14,18,'N','N','N','N','N','','N','N','N','N','N',''),(15,19,'N','N','N','N','N','','N','Y','N','N','N',''),(16,20,'N','N','N','N','N','','N','N','Y','N','N',''),(17,21,'N','N','N','N','N','','N','N','N','N','N','');
/*!40000 ALTER TABLE `sample_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `send_sample`
--

DROP TABLE IF EXISTS `send_sample`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `send_sample` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `project_number` varchar(45) DEFAULT NULL,
  `sample_name` varchar(45) DEFAULT NULL,
  `species` varchar(45) DEFAULT NULL,
  `express_number` varchar(45) DEFAULT NULL,
  `product_num` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `send_sample`
--

LOCK TABLES `send_sample` WRITE;
/*!40000 ALTER TABLE `send_sample` DISABLE KEYS */;
INSERT INTO `send_sample` VALUES (1,12,'ONMATH-900','sample_name_1','chicken','2113234','1','2017/6/21',''),(2,12,'ONMATH-900','sample_name_2','chicken','2113234','1','2017/6/21',''),(3,12,'ONMATH-900','sample_name_3','chicken','2113234','1','2017/6/21',''),(4,12,'ONMATH-900','sample_name_4','chicken','2113234','1','2017/6/21',''),(5,12,'ONMATH-900','sample_name_5','chicken','2113234','1','2017/6/21','haha'),(6,12,'ONMATH-900','sample_name_6','chicken','43424234','1','2017/6/21',''),(7,12,'ONMATH-900','sample_name_7','chicken','43424234','1','2017/6/21',''),(8,12,'ONMATH-900','sample_name_8','chicken','43424234','1','2017/6/21',''),(9,12,'ONMATH-900','sample_name_9','chicken','43424234','1','2017/6/21',''),(10,12,'ONMATH-900','sample_name_10','chicken','43424234','1','2017/6/21',''),(11,14,'ONMATH-903','test_1','dog','41343242','1','2017/6/28','600'),(12,14,'ONMATH-903','test_2','dog','41343242','1','2017/6/28',''),(13,14,'ONMATH-903','test_3','dog','','1','2017/6/28',''),(14,14,'ONMATH-903','test_4','dog','41435354','1','2017/6/28',''),(15,14,'ONMATH-903','test_5','dog','41435354','1','2017/6/28',''),(16,14,'ONMATH-903','test_6','dog','41435354','1','2017/6/28',''),(17,14,'ONMATH-903','test_7','dog','41435354','1','2017/6/28',''),(18,14,'ONMATH-903','test_8','dog','41435354','1','2017/6/28',''),(19,14,'ONMATH-903','test_9','dog','41435354','1','2017/6/28',''),(20,14,'ONMATH-903','test_10','dog','','1','2017/7/17',''),(67,21,'ONMATH-909','test_name_1','狗','12313222','1','2017-08-01','tesfa'),(68,21,'ONMATH-909','test_name_2','狗','12313222','1','2017-08-01',''),(69,21,'ONMATH-909','test_name_3','狗','12313222','1','2017-08-02','test'),(70,21,'ONMATH-909','test_name_4','狗','12313222','1','2017-08-02','hsa'),(71,21,'ONMATH-909','test_name_5','狗','12313222','2','2017-08-03',''),(72,21,'ONMATH-909','test_name_6','狗','12313222','1','2017-08-03','haha'),(73,21,'ONMATH-909','test_name_7','狗','12313222','2','2017-08-04',''),(74,21,'ONMATH-909','test_name_8','狗','12313222','1','2017-08-04',''),(75,21,'ONMATH-909','test_name_9','狗','12313222','1','2017-08-05','');
/*!40000 ALTER TABLE `send_sample` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upmachine`
--

DROP TABLE IF EXISTS `upmachine`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `upmachine` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `project_id` int(11) DEFAULT NULL,
  `project_number` varchar(45) DEFAULT NULL,
  `sample_name` varchar(45) DEFAULT NULL,
  `sample_id` varchar(45) DEFAULT NULL,
  `upmachinetype` varchar(45) DEFAULT NULL,
  `mode` varchar(45) DEFAULT NULL,
  `data_count` varchar(45) DEFAULT NULL,
  `time` varchar(45) DEFAULT NULL,
  `comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `sample_id_UNIQUE` (`sample_id`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upmachine`
--

LOCK TABLES `upmachine` WRITE;
/*!40000 ALTER TABLE `upmachine` DISABLE KEYS */;
INSERT INTO `upmachine` VALUES (1,12,'ONMATH-900','sample_name_1','10-A','','','4','2017/6/30',''),(2,12,'ONMATH-900','sample_name_2','10-B','','','4','2017/6/30',''),(3,12,'ONMATH-900','sample_name_3','11-A','','','4','2017/6/30',''),(4,12,'ONMATH-900','sample_name_4','11-B','','','4','2017/6/30','test'),(5,12,'ONMATH-900','sample_name_5','12-A','','','4','2017/6/30',''),(6,12,'ONMATH-900','sample_name_6','12-B','','','','2017/6/30',''),(7,12,'ONMATH-900','sample_name_7','13-A','','','6','2017/6/30',''),(8,12,'ONMATH-900','sample_name_8','13-B','','','','2017/6/30',''),(9,12,'ONMATH-900','sample_name_9','14-A','','','3','2017/6/30',''),(10,12,'ONMATH-900','sample_name_10','14-B','','','','2017/6/30','test'),(11,14,'ONMATH-903','test_1','15-A','','','2','2017/7/5',''),(12,14,'ONMATH-903','test_2','15-B','','','2','2017/7/5',''),(13,14,'ONMATH-903','test_3','16-A','','','2','2017/7/5',''),(14,14,'ONMATH-903','test_4','16-B','','','2','2017/7/5',''),(15,14,'ONMATH-903','test_5','17-A','','','2','2017/7/5',''),(16,14,'ONMATH-903','test_6','17-B','','','2','2017/7/5',''),(17,14,'ONMATH-903','test_7','18-A','','','2','2017/7/5',''),(18,14,'ONMATH-903','test_8','18-B','','','2','2017/7/5',''),(19,14,'ONMATH-903','test_9','19-A','','','2','2017/7/5',''),(20,14,'ONMATH-903','test_10','19-B','','','2','2017/7/25',''),(21,21,'ONMATH-909','haha_1','20-A','','','','2017/7/25',''),(22,21,'ONMATH-909','haha_2','20-B','','','','2017/7/25','test'),(23,21,'ONMATH-909','haha_3','21-A','','','','2017/7/25',''),(24,21,'ONMATH-909','haha_4','21-B','','','6','2017/7/25',''),(25,21,'ONMATH-909','haha_5','22-A','','','','2017/7/25',''),(26,21,'ONMATH-909','haha_6','22-B','','','','2017/7/25',''),(27,21,'ONMATH-909','haha_7','123-A','','','5','2017/7/25',''),(28,21,'ONMATH-909','haha_8','123-B','','','','2017/7/25',''),(29,21,'ONMATH-909','haha_9','131-A','','','','2017/7/25',''),(30,21,'ONMATH-909','haha_10','131-B','','','','2017/7/25','');
/*!40000 ALTER TABLE `upmachine` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info`
--

DROP TABLE IF EXISTS `user_info`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `customer_name` varchar(45) DEFAULT '',
  `password` varchar(200) NOT NULL,
  `e_mail` varchar(45) DEFAULT '',
  `tel` varchar(45) DEFAULT '',
  `company` varchar(100) DEFAULT '',
  `age` int(5) unsigned DEFAULT '0',
  `sex` varchar(2) DEFAULT '',
  `role` varchar(45) DEFAULT 'user',
  `status` varchar(1) DEFAULT 'Y',
  `field` varchar(100) DEFAULT '',
  `notes` varchar(200) DEFAULT '',
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info`
--

LOCK TABLES `user_info` WRITE;
/*!40000 ALTER TABLE `user_info` DISABLE KEYS */;
INSERT INTO `user_info` VALUES (1,'测试用户','','test','test','123456','',0,'','user','Y','','','2016-04-09 22:03:39','2016-04-09 22:03:39'),(2,'test','test','pbkdf2:sha1:1000$2f5P80F1$d2abf20af5d243894cbe24bfd1a3f50724ce080b','test@qq.com','13455556666','omath',0,'','user','Y','chinan','','2016-04-09 22:24:26','2017-06-04 09:12:43'),(3,'陈佳林','','chenjialin','839588325@qq.com','18628264390','',0,'','manager','Y','','','2016-04-09 22:45:19','2016-04-09 22:45:19'),(4,'zxchen','','2008','hugoczx@163.com','18215509986','',0,'','manager','Y','','','2016-04-12 07:41:12','2016-04-12 07:41:12'),(5,'mytest','','123','safsd','34153241','',0,'','user','Y','','','2016-04-12 07:42:44','2016-04-12 07:42:44'),(6,'bom','bom','11111111111','as@aa.com','13344445555','dfa',0,'','user','Y','畜牧/兽医学','','2016-10-15 12:41:15','2016-10-15 12:41:15'),(7,'chencheng','陈诚','pbkdf2:sha1:1000$XEWnS32p$f91cbf1dbbc9a815b17fa6ba6c01afe2ee59fe60','291552579@qq.com','18583994795','onmath',0,'','manager','Y','','','2017-06-23 17:57:35','2017-06-23 17:57:35'),(8,'haha','haha','pbkdf2:sha1:1000$7qN4GCS7$0eabc89794017715c21c98ebd08bc65be2bbfdbe','haha@haha.com','13548019589','haha',0,'','user','Y','生物学','','2017-07-14 11:24:41','2017-07-14 11:24:41');
/*!40000 ALTER TABLE `user_info` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-14 10:15:57
