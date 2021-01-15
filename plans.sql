/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.7.32-0ubuntu0.16.04.1 
*********************************************************************
*/
/*!40101 SET NAMES utf8 */;

create table `plans` (
	`plan_id` int (11),
	`plan_name` varchar (765),
	`plan_description` text ,
	`plan_amount` int (11),
	`plan_added` datetime ,
	`plan_icon` varchar (300),
	`plan_type` char (3),
	`plan_service_id` int (11),
	`plan_gst_amount` int (11),
	`plan_video` text ,
	`plan_sample_report` text ,
	`plan_original_price` int (11),
	`plan_isActive` char (3),
	`plan_created_by` int (11),
	`plan_updated_date` datetime ,
	`plan_updated_by` int (11),
	`last_modified` timestamp 
); 




