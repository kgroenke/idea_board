-- MySQL dump 10.13  Distrib 5.6.24, for osx10.8 (x86_64)
--
-- Host: 127.0.0.1    Database: new_red_belt
-- ------------------------------------------------------
-- Server version	5.5.42

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
-- Table structure for table `ideas`
--

DROP TABLE IF EXISTS `ideas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `ideas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content` text,
  `like_count` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_ideas_users_idx` (`user_id`),
  CONSTRAINT `fk_ideas_users` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ideas`
--

LOCK TABLES `ideas` WRITE;
/*!40000 ALTER TABLE `ideas` DISABLE KEYS */;
INSERT INTO `ideas` VALUES (1,'We should make waffles that taste like bacon!',5,1),(2,'Lets make a car that runs on water',6,2),(3,'I would like to see a perpetual motion machine',2,3),(4,'Someone should develop a hybrid electric razor scooter.',2,1);
/*!40000 ALTER TABLE `ideas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `likes`
--

DROP TABLE IF EXISTS `likes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `likes` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `idea_id` int(11) NOT NULL,
  `liker_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_likes_ideas1_idx` (`idea_id`),
  KEY `fk_likes_users1_idx` (`liker_id`),
  CONSTRAINT `fk_likes_ideas1` FOREIGN KEY (`idea_id`) REFERENCES `ideas` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_likes_users1` FOREIGN KEY (`liker_id`) REFERENCES `users` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `likes`
--

LOCK TABLES `likes` WRITE;
/*!40000 ALTER TABLE `likes` DISABLE KEYS */;
INSERT INTO `likes` VALUES (1,'2015-10-01 13:07:30','2015-10-01 13:07:30',1,2),(2,'2015-10-01 13:07:44','2015-10-01 13:07:44',1,3),(3,'2015-10-01 13:07:52','2015-10-01 13:07:52',1,3),(4,'2015-10-01 13:07:56','2015-10-01 13:07:56',1,3),(5,'2015-10-01 13:08:20','2015-10-01 13:08:20',2,3),(6,'2015-10-01 13:08:25','2015-10-01 13:08:25',2,3),(7,'2015-10-01 13:08:30','2015-10-01 13:08:30',2,1),(8,'2015-10-01 13:51:51','2015-10-01 13:51:51',1,1),(9,'2015-10-01 13:52:28','2015-10-01 13:52:28',4,1),(10,'2015-10-01 13:56:15','2015-10-01 13:56:15',3,1),(11,'2015-10-01 14:03:36','2015-10-01 14:03:36',2,1),(12,'2015-10-01 14:03:39','2015-10-01 14:03:39',2,1),(13,'2015-10-01 14:03:40','2015-10-01 14:03:40',2,1),(14,'2015-10-01 15:11:27','2015-10-01 15:11:27',4,4),(16,'2015-10-01 15:37:49','2015-10-01 15:37:49',3,1);
/*!40000 ALTER TABLE `likes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `alias` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `pw_hash` varchar(255) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (1,'Kelsey','kgroenke','krgroenke@gmail.com','$2a$12$AU748uNQIGJ.MNFx.MjueeJntj8S0A3OKG35XjV2P2FV/4QreoZUu','2015-10-01 12:43:02','2015-10-01 12:43:02'),(2,'Alexa Groenke','agroenke','alexa.groenke@gmail.com','$2a$12$gwJgwQ5YpCN/CF4vA1tuG.Ka6auWUoa.ZmvgsA6uRMSz8nB8YYxwS','2015-10-01 12:44:28','2015-10-01 12:44:28'),(3,'Tevon Edwards','tedwards','tevonedwards@gmail.com','$2a$12$ry0PlM96o6E0h2MbdmP6k.vNMhk7ZB6AoyVgq17w4JzpTMWYOgXJC','2015-10-01 12:45:03','2015-10-01 12:45:03'),(4,'Hannah Simonson','hsimonson','hsimonson@gmail.com','$2a$12$CszOLjlJA51SXh1hpNq76eF9nyUUh1ma8z1AEyQjt7cbEovi2od5q','2015-10-01 15:11:18','2015-10-01 15:11:18');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-10-01 15:56:05
