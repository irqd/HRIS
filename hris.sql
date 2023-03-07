-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Mar 07, 2023 at 04:18 AM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hris`
--

-- --------------------------------------------------------

--
-- Table structure for table `alembic_version`
--

CREATE TABLE `alembic_version` (
  `version_num` varchar(32) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `alembic_version`
--

INSERT INTO `alembic_version` (`version_num`) VALUES
('6cfc7a6fcccd');

-- --------------------------------------------------------

--
-- Table structure for table `announcements`
--

CREATE TABLE `announcements` (
  `id` int(11) NOT NULL,
  `date_created` date NOT NULL,
  `announced_by` varchar(500) NOT NULL,
  `message` varchar(500) NOT NULL,
  `title` varchar(500) NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `announcements`
--

INSERT INTO `announcements` (`id`, `date_created`, `announced_by`, `message`, `title`, `user_id`) VALUES
(28, '2023-02-21', 'Alfred U. Paguio', 'Test Test Test Test Test Test', 'Announcement #1', 2),
(29, '2023-02-22', 'Alfred U. Paguio', 'Test', 'Today is feb 22', 2),
(30, '2023-02-23', 'Alfred U. Paguio', 'Description', 'Announcement 2-23', 2),
(31, '2023-02-25', 'Alfred U. Paguio', 'Hello test', 'Announcement!', 2),
(32, '2023-02-26', 'Alfred U. Paguio', 'Test', 'Announcement #1', 2),
(33, '2023-02-26', 'Alfred U. Paguio', 'Test', 'Test', 2),
(34, '2023-02-27', 'Alfred U. Paguio', 'Test', 'Test', 2),
(36, '2023-03-06', 'Alfred U. Paguio', 'Test', 'Title', 2);

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `attendance_type` enum('Present','Absent','Late','Unavailable','On_Leave') NOT NULL,
  `status` enum('Approved','Declined','Pending') NOT NULL,
  `start_shift` time NOT NULL,
  `end_shift` time NOT NULL,
  `checked_in` time DEFAULT NULL,
  `checked_out` time DEFAULT NULL,
  `pre_ot` time DEFAULT NULL,
  `post_ot` time DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`id`, `date`, `attendance_type`, `status`, `start_shift`, `end_shift`, `checked_in`, `checked_out`, `pre_ot`, `post_ot`, `employee_id`) VALUES
(121, '2023-02-22', 'Present', 'Approved', '08:00:00', '17:00:00', '06:00:00', '20:00:00', '06:00:00', '20:00:00', 2),
(123, '2023-02-23', 'Present', 'Approved', '08:00:00', '17:00:00', '07:58:00', '09:31:36', '07:58:00', NULL, 2),
(124, '2023-02-24', 'Present', 'Approved', '08:00:00', '17:00:00', '07:55:00', '18:48:00', '07:55:00', '18:48:00', 2),
(125, '2023-02-27', 'On_Leave', 'Approved', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 2),
(126, '2023-02-28', 'On_Leave', 'Approved', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 2),
(127, '2023-03-01', 'On_Leave', 'Approved', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 2),
(128, '2023-03-02', 'On_Leave', 'Approved', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 2),
(129, '2023-03-03', 'On_Leave', 'Approved', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 2),
(136, '2023-02-20', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '20:00:00', NULL, '20:00:00', 2),
(137, '2023-02-21', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '20:00:00', NULL, '20:00:00', 2),
(138, '2023-02-17', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(139, '2023-02-16', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '20:00:00', NULL, '20:00:00', 2),
(140, '2023-02-15', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(141, '2023-02-14', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(142, '2023-02-13', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(143, '2023-02-10', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(144, '2023-02-09', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '20:00:00', NULL, '20:00:00', 2),
(145, '2023-02-08', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '20:00:00', NULL, '20:00:00', 2),
(146, '2023-02-07', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '20:00:00', NULL, '20:00:00', 2),
(147, '2023-02-06', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(148, '2023-02-03', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(149, '2023-02-02', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(150, '2023-02-01', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 2),
(151, '2023-02-01', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(152, '2023-02-02', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(153, '2023-02-03', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(154, '2023-02-06', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(155, '2023-02-07', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(156, '2023-02-08', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(157, '2023-02-09', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(159, '2023-02-10', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(160, '2023-02-13', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(161, '2023-02-14', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(162, '2023-02-15', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(170, '2023-02-16', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(172, '2023-02-17', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(178, '2023-02-20', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(179, '2023-02-21', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(180, '2023-02-22', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(181, '2023-02-23', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(182, '2023-02-24', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(189, '2023-02-27', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 30),
(190, '2023-02-27', 'On_Leave', 'Approved', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 1),
(191, '2023-02-28', 'Present', 'Approved', '08:00:00', '17:00:00', '08:00:00', '17:00:00', NULL, NULL, 1),
(193, '2023-03-06', 'Unavailable', 'Pending', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 30),
(194, '2023-03-07', 'Unavailable', 'Pending', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 30),
(195, '2023-03-08', 'Unavailable', 'Pending', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 30),
(196, '2023-03-09', 'Unavailable', 'Pending', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 30),
(197, '2023-03-10', 'Unavailable', 'Pending', '08:00:00', '17:00:00', NULL, NULL, NULL, NULL, 30),
(198, '2023-03-06', 'Present', 'Pending', '08:00:00', '17:00:00', '08:00:00', NULL, NULL, NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `id` int(11) NOT NULL,
  `department_name` varchar(50) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date_created` date NOT NULL,
  `manager` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`id`, `department_name`, `description`, `date_created`, `manager`) VALUES
(1, 'IT Department', 'IT Dept.', '2023-02-09', 'Ivan Rey Quistadio Deposoy'),
(2, 'HR Department', 'Hr Department Description.', '2023-02-09', 'Alfred Umali Paguio'),
(7, 'Marketing Department', 'the face of the company', '2023-02-22', 'Andriane S Cabuyao');

-- --------------------------------------------------------

--
-- Table structure for table `employee_info`
--

CREATE TABLE `employee_info` (
  `id` int(11) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `first_name` varchar(50) NOT NULL,
  `middle_name` varchar(50) NOT NULL,
  `gender` varchar(50) NOT NULL,
  `birth_date` date NOT NULL,
  `civil_status` varchar(50) NOT NULL,
  `mobile` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `address` varchar(50) NOT NULL,
  `emergency_name` varchar(50) NOT NULL,
  `emergency_contact` varchar(50) NOT NULL,
  `emergency_relationship` varchar(50) NOT NULL,
  `tin` varchar(50) NOT NULL,
  `SSS` varchar(50) NOT NULL,
  `phil_health` varchar(50) NOT NULL,
  `pag_ibig` varchar(50) NOT NULL,
  `date_created` date NOT NULL,
  `position_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee_info`
--

INSERT INTO `employee_info` (`id`, `last_name`, `first_name`, `middle_name`, `gender`, `birth_date`, `civil_status`, `mobile`, `email`, `address`, `emergency_name`, `emergency_contact`, `emergency_relationship`, `tin`, `SSS`, `phil_health`, `pag_ibig`, `date_created`, `position_id`) VALUES
(1, 'Deposoy', 'Ivan Rey', 'Quistadio', 'Male', '2001-07-12', 'Single', '0912345678901', 'ivan@gmail.com', 'Muntinlupa', 'Ivan', '0912345678901', 'Self', '0123456789', '0123456789', '0123456789', '0123456789', '2023-02-09', 13),
(2, 'Paguio', 'Alfred', 'Umali', 'Male', '2000-06-03', 'Single', '098765432125', 'alfred@gmail.com', 'Muntinlupa', 'Alfred', '09876543212', 'Self', '9876543210', '9876543210', '9876543210', '9876543210', '2023-02-09', 13),
(30, 'Cabuyao', 'Andriane', 'S', 'Male', '2023-02-26', 'Single', '09876543211', 'andraine@gmail.com', 'Muntinlupa', 'Andriane', '098765432111', 'Self', '903469034634', '9063490673', '349067349063', '340673406749', '2023-02-26', 17),
(32, 'Doe', 'John', 'Lennon', 'Male', '2000-12-25', 'Married', '09876543219', 'john@gmail.com', 'Muntinlupa', 'Jane', '09876543219', 'Spouse', '768577475739', '7394573489', '234985734897', '239485672896', '2023-02-28', 1),
(33, 'Crownguard', 'Luxanna', 'D', 'Female', '2002-06-15', 'Single', '09876543212', 'luxanna@gmail.com', 'High Silvermere, Demacia', 'Garen Crownguard', '09876746326124', 'Brother', '895723523752', '9468768943', '493873896347', '342895723895', '2023-02-28', 18);

-- --------------------------------------------------------

--
-- Table structure for table `employment_info`
--

CREATE TABLE `employment_info` (
  `id` int(11) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `status` enum('Hired','Retired','Terminated','Resigned') NOT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `salary_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employment_info`
--

INSERT INTO `employment_info` (`id`, `description`, `start_date`, `end_date`, `status`, `employee_id`, `salary_id`) VALUES
(1, 'Employment Info of Ivan', '2023-02-09', NULL, 'Hired', 1, 4),
(2, 'For alfred', '2023-02-09', NULL, 'Hired', 2, 3),
(30, 'Test', '2023-02-26', NULL, 'Hired', 30, 4),
(32, 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae, quas quo optio assumenda dignissimos nemo rerum mollitia quae accusantium provident ipsum itaque. Corrupti et culpa iste nobis deleniti sint sequi.', '2023-02-28', NULL, 'Hired', 32, 3),
(33, 'Luxanna is an intern in the HR Department', '2023-02-28', NULL, 'Hired', 33, 8);

-- --------------------------------------------------------

--
-- Table structure for table `leave`
--

CREATE TABLE `leave` (
  `id` int(11) NOT NULL,
  `type` enum('Sick_Leave','SIL','Maternity_Leave','Paternity_Leave','Vacation_Leave','Parental_Leave','Rehabilitation_Leave','Study_Leave') NOT NULL,
  `date_requested` date NOT NULL,
  `leave_date` date NOT NULL,
  `status` enum('Approved','Declined','Pending') NOT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `processed_date` date DEFAULT NULL,
  `processed_by` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `leave`
--

INSERT INTO `leave` (`id`, `type`, `date_requested`, `leave_date`, `status`, `employee_id`, `processed_date`, `processed_by`) VALUES
(39, 'Sick_Leave', '2023-02-22', '2023-02-27', 'Approved', 2, '2023-02-23', 'Alfred U. Paguio'),
(40, 'Sick_Leave', '2023-02-22', '2023-02-28', 'Approved', 2, '2023-02-23', 'Alfred U. Paguio'),
(41, 'Sick_Leave', '2023-02-22', '2023-03-01', 'Approved', 2, '2023-02-23', 'Alfred U. Paguio'),
(42, 'Sick_Leave', '2023-02-22', '2023-03-02', 'Approved', 2, '2023-02-23', 'Alfred U. Paguio'),
(43, 'Sick_Leave', '2023-02-22', '2023-03-03', 'Approved', 2, '2023-02-23', 'Alfred U. Paguio'),
(44, 'Sick_Leave', '2023-02-23', '2023-02-23', 'Approved', 2, '2023-02-23', 'Alfred U. Paguio'),
(61, 'Sick_Leave', '2023-02-27', '2023-02-27', 'Approved', 1, '2023-02-27', 'Alfred U. Paguio'),
(62, 'Sick_Leave', '2023-03-06', '2023-03-07', 'Approved', 2, '2023-03-06', 'Alfred U. Paguio'),
(63, 'Sick_Leave', '2023-03-06', '2023-03-08', 'Approved', 2, '2023-03-06', 'Alfred U. Paguio'),
(64, 'Sick_Leave', '2023-03-06', '2023-03-09', 'Approved', 2, '2023-03-06', 'Alfred U. Paguio'),
(65, 'Sick_Leave', '2023-03-06', '2023-03-10', 'Approved', 2, '2023-03-06', 'Alfred U. Paguio');

-- --------------------------------------------------------

--
-- Table structure for table `messages`
--

CREATE TABLE `messages` (
  `id` int(11) NOT NULL,
  `message` varchar(500) NOT NULL,
  `create_date` date NOT NULL,
  `create_time` time NOT NULL,
  `room_user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `messages`
--

INSERT INTO `messages` (`id`, `message`, `create_date`, `create_time`, `room_user_id`) VALUES
(1, 'Hello', '2023-03-06', '10:24:04', 23),
(2, 'Hi', '2023-03-06', '10:24:16', 24);

-- --------------------------------------------------------

--
-- Table structure for table `payslips`
--

CREATE TABLE `payslips` (
  `id` int(11) NOT NULL,
  `start_cut_off` date NOT NULL,
  `end_cut_off` date NOT NULL,
  `days_present` int(11) NOT NULL,
  `gross_pay` float NOT NULL,
  `deductions` float NOT NULL,
  `net_pay` float NOT NULL,
  `employee_id` int(11) DEFAULT NULL,
  `total_regular_hours` float NOT NULL,
  `pre_ot_hours` float NOT NULL,
  `post_ot_hours` float NOT NULL,
  `total_ot_hours` float NOT NULL,
  `name` varchar(500) NOT NULL,
  `allowance` float NOT NULL,
  `status` enum('Approved','Declined','Pending') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payslips`
--

INSERT INTO `payslips` (`id`, `start_cut_off`, `end_cut_off`, `days_present`, `gross_pay`, `deductions`, `net_pay`, `employee_id`, `total_regular_hours`, `pre_ot_hours`, `post_ot_hours`, `total_ot_hours`, `name`, `allowance`, `status`) VALUES
(215, '2023-02-16', '2023-02-28', 8, 4900, 1191.25, 6708.75, 1, 56, 0, 0, 0, 'Ivan Rey Quistadio Deposoy', 3000, 'Approved'),
(216, '2023-02-16', '2023-02-28', 7, 8177.45, 1079.5, 10097.9, 2, 78.6367, 2.11, 13.8, 15.91, 'Alfred Umali Paguio', 3000, 'Approved'),
(217, '2023-02-16', '2023-02-28', 1, 700, 1191.25, 2508.75, 30, 8, 0, 0, 0, 'Andriane S Cabuyao', 3000, 'Pending'),
(218, '2023-02-16', '2023-02-28', 0, 0, 1079.5, 1920.5, 32, 0, 0, 0, 0, 'John Lennon Doe', 3000, 'Pending'),
(219, '2023-02-16', '2023-02-28', 0, 0, 0, 0, 33, 0, 0, 0, 0, 'Luxanna D Crownguard', 0, 'Pending'),
(230, '2023-01-01', '2023-01-15', 0, 0, 1191.25, 1808.75, 1, 0, 0, 0, 0, 'Ivan Rey Quistadio Deposoy', 3000, 'Pending'),
(231, '2023-01-01', '2023-01-15', 0, 0, 1079.5, 1920.5, 2, 0, 0, 0, 0, 'Alfred Umali Paguio', 3000, 'Pending'),
(232, '2023-01-01', '2023-01-15', 0, 0, 1191.25, 1808.75, 30, 0, 0, 0, 0, 'Andriane S Cabuyao', 3000, 'Pending'),
(233, '2023-01-01', '2023-01-15', 0, 0, 1079.5, 1920.5, 32, 0, 0, 0, 0, 'John Lennon Doe', 3000, 'Pending'),
(234, '2023-01-01', '2023-01-15', 0, 0, 0, 0, 33, 0, 0, 0, 0, 'Luxanna D Crownguard', 0, 'Pending'),
(235, '2023-02-01', '2023-02-15', 11, 7700, 1191.25, 9508.75, 1, 88, 0, 0, 0, 'Ivan Rey Quistadio Deposoy', 3000, 'Approved'),
(236, '2023-02-01', '2023-02-15', 11, 9590, 1191.25, 11398.8, 2, 88, 0, 9, 9, 'Alfred Umali Paguio', 3000, 'Approved'),
(237, '2023-02-01', '2023-02-15', 0, 9800, 1191.25, 11608.8, 30, 88, 5, 5, 10, 'Andriane S Cabuyao', 3000, 'Approved'),
(238, '2023-02-01', '2023-02-15', 0, 0, 1079.5, 1920.5, 32, 0, 0, 0, 0, 'John Lennon Doe', 3000, 'Pending'),
(239, '2023-02-01', '2023-02-15', 0, 0, 0, 0, 33, 0, 0, 0, 0, 'Luxanna D Crownguard', 0, 'Pending'),
(255, '2023-03-01', '2023-03-15', 0, 0, 1191.25, 1808.75, 1, 0, 0, 0, 0, 'Ivan Rey Quistadio Deposoy', 3000, 'Pending'),
(256, '2023-03-01', '2023-03-15', 0, 0, 1079.5, 1920.5, 2, 0, 0, 0, 0, 'Alfred Umali Paguio', 3000, 'Pending'),
(257, '2023-03-01', '2023-03-15', 0, 0, 1191.25, 1808.75, 30, 0, 0, 0, 0, 'Andriane S Cabuyao', 3000, 'Pending'),
(258, '2023-03-01', '2023-03-15', 0, 0, 1079.5, 1920.5, 32, 0, 0, 0, 0, 'John Lennon Doe', 3000, 'Pending'),
(259, '2023-03-01', '2023-03-15', 0, 0, 0, 0, 33, 0, 0, 0, 0, 'Luxanna D Crownguard', 0, 'Pending'),
(265, '2023-03-16', '2023-03-31', 0, 0, 1191.25, 1808.75, 1, 0, 0, 0, 0, 'Ivan Rey Quistadio Deposoy', 3000, 'Pending'),
(266, '2023-03-16', '2023-03-31', 0, 0, 1079.5, 1920.5, 2, 0, 0, 0, 0, 'Alfred Umali Paguio', 3000, 'Pending'),
(267, '2023-03-16', '2023-03-31', 0, 0, 1191.25, 1808.75, 30, 0, 0, 0, 0, 'Andriane S Cabuyao', 3000, 'Pending'),
(268, '2023-03-16', '2023-03-31', 0, 0, 1079.5, 1920.5, 32, 0, 0, 0, 0, 'John Lennon Doe', 3000, 'Pending'),
(269, '2023-03-16', '2023-03-31', 0, 0, 0, 0, 33, 0, 0, 0, 0, 'Luxanna D Crownguard', 0, 'Pending'),
(270, '2023-01-16', '2023-01-31', 0, 0, 1191.25, 1808.75, 1, 0, 0, 0, 0, 'Ivan Rey Quistadio Deposoy', 3000, 'Pending'),
(271, '2023-01-16', '2023-01-31', 0, 0, 1079.5, 1920.5, 2, 0, 0, 0, 0, 'Alfred Umali Paguio', 3000, 'Pending'),
(272, '2023-01-16', '2023-01-31', 0, 0, 1191.25, 1808.75, 30, 0, 0, 0, 0, 'Andriane S Cabuyao', 3000, 'Pending'),
(273, '2023-01-16', '2023-01-31', 0, 0, 1079.5, 1920.5, 32, 0, 0, 0, 0, 'John Lennon Doe', 3000, 'Pending'),
(274, '2023-01-16', '2023-01-31', 0, 0, 0, 0, 33, 0, 0, 0, 0, 'Luxanna D Crownguard', 0, 'Pending');

-- --------------------------------------------------------

--
-- Table structure for table `positions`
--

CREATE TABLE `positions` (
  `id` int(11) NOT NULL,
  `position_name` varchar(50) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `position_status` enum('Hiring','Full') NOT NULL,
  `date_created` date NOT NULL,
  `department_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `positions`
--

INSERT INTO `positions` (`id`, `position_name`, `description`, `position_status`, `date_created`, `department_id`) VALUES
(1, 'Web Developer', 'Web Dev', 'Hiring', '2023-02-09', 1),
(2, 'HR Staff', 'Hr Staff', 'Hiring', '2023-02-09', 2),
(3, 'Recruiter', 'Recruiter in HR Dept.', 'Hiring', '2023-02-11', 2),
(4, 'Dev Ops', 'Position for IT Dept.', 'Hiring', '2023-02-14', 1),
(11, 'Chief Marketing Officer', 'Reports directly to the chief executive officer (CEO)', 'Full', '2023-02-22', 7),
(12, 'HR Manager', 'HR Manager', 'Hiring', '2023-02-26', 2),
(13, 'IT Manager', 'IT Manager', 'Hiring', '2023-02-26', 1),
(16, 'Marketing Position #1', 'Marketing', 'Hiring', '2023-02-27', 7),
(17, 'Marketing Manager', 'Description', 'Hiring', '2023-02-27', 7),
(18, 'Intern', 'Description for the position of Intern in HR dept.', 'Hiring', '2023-02-28', 2);

-- --------------------------------------------------------

--
-- Table structure for table `rooms`
--

CREATE TABLE `rooms` (
  `id` int(11) NOT NULL,
  `room_name` varchar(50) NOT NULL,
  `create_date` date NOT NULL,
  `create_time` time NOT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `rooms`
--

INSERT INTO `rooms` (`id`, `room_name`, `create_date`, `create_time`, `user_id`) VALUES
(12, 'Alfred U. Paguio_Ivan Rey Q. Deposoy', '2023-03-06', '08:03:19', 2),
(15, 'Alfred U. Paguio_Andriane S Cabuyao', '2023-03-06', '12:31:44', 2),
(16, 'Alfred U. Paguio_John Lennon Doe', '2023-03-06', '16:18:35', 2);

-- --------------------------------------------------------

--
-- Table structure for table `room_users`
--

CREATE TABLE `room_users` (
  `id` int(11) NOT NULL,
  `room_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `room_users`
--

INSERT INTO `room_users` (`id`, `room_id`, `user_id`) VALUES
(23, 12, 2),
(24, 12, 1),
(29, 15, 2),
(30, 15, 29),
(31, 16, 2),
(32, 16, 31);

-- --------------------------------------------------------

--
-- Table structure for table `salaries`
--

CREATE TABLE `salaries` (
  `id` int(11) NOT NULL,
  `salary_name` varchar(50) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `daily_rate` float NOT NULL,
  `hourly_rate` float NOT NULL,
  `bir_tax` float NOT NULL,
  `sss_tax` float NOT NULL,
  `phil_health_tax` float NOT NULL,
  `pag_ibig_tax` float NOT NULL,
  `ot_rate` float NOT NULL,
  `allowance` float NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `salaries`
--

INSERT INTO `salaries` (`id`, `salary_name`, `description`, `daily_rate`, `hourly_rate`, `bir_tax`, `sss_tax`, `phil_health_tax`, `pag_ibig_tax`, `ot_rate`, `allowance`) VALUES
(3, 'Regular', 'Regular Employee Salary', 560, 70, 0, 617.5, 277.2, 184.8, 168, 3000),
(4, 'Manager', 'Manager Salary', 700, 87.5, 0, 655, 321.75, 214.5, 210, 3000),
(7, 'Partime', 'Partime Employee Salary', 463, 58, 0, 0, 0, 0, 168, 1500),
(8, 'Intern', 'Salary for intern', 0, 0, 0, 0, 0, 0, 0, 0);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `name` varchar(60) NOT NULL,
  `image_path` varchar(50) DEFAULT 'images/profile.svg',
  `company_email` varchar(50) NOT NULL,
  `password_hash` varchar(60) NOT NULL,
  `access` enum('Employee','Admin') NOT NULL,
  `date_created` date NOT NULL,
  `employee_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `name`, `image_path`, `company_email`, `password_hash`, `access`, `date_created`, `employee_id`) VALUES
(1, 'Ivan Rey Q. Deposoy', 'images/uploads/4w4nink5ml.jpg', 'ivan@gmail.com', '$2b$12$KZ..KIgbRgMGB.0aSnHCweZyPo5s2BRQDHzoEL1TVYW8ASLYJIdu.', 'Employee', '2023-02-09', 1),
(2, 'Alfred U. Paguio', 'images/uploads/ufkeclxkg8.png', 'alfred@gmail.com', '$2b$12$fR4Yp3GE.RAXxA5aNOXXVuMW7CQd01tKG.y.PMP4DcdLQMVjij7ny', 'Admin', '2023-02-09', 2),
(29, 'Andriane S Cabuyao', 'images/uploads/pshwxjuf3x.jpg', 'andraine@gmail.com', '$2b$12$hN2kN/hjxo/iWloAPjPGsunZn92xokwtB6/wIAvSdXBznMMaDAs/m', 'Employee', '2023-02-26', 30),
(31, 'John Lennon Doe', 'images/uploads/uezg0m54zb.png', 'john@gmail.com', '$2b$12$kmdt2Vlp4PkfBEym1iUXK.yuEonDji0akDRmQFUMf3PUPC/48Omsy', 'Employee', '2023-02-28', 32),
(32, 'Luxanna D Crownguard', 'images/uploads/oqoml2mncw.jpg', 'lux@gmail.com', '$2b$12$5mmC4T/OdO67gN1J43iXSOIjDr5NLtBlYB7KdQ2BzACCjWUmi314a', 'Employee', '2023-02-28', 33);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `alembic_version`
--
ALTER TABLE `alembic_version`
  ADD PRIMARY KEY (`version_num`);

--
-- Indexes for table `announcements`
--
ALTER TABLE `announcements`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employee_id` (`employee_id`);

--
-- Indexes for table `departments`
--
ALTER TABLE `departments`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `employee_info`
--
ALTER TABLE `employee_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `tin` (`tin`),
  ADD UNIQUE KEY `SSS` (`SSS`),
  ADD UNIQUE KEY `phil_health` (`phil_health`),
  ADD UNIQUE KEY `pag_ibig` (`pag_ibig`),
  ADD KEY `position_id` (`position_id`);

--
-- Indexes for table `employment_info`
--
ALTER TABLE `employment_info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employee_id` (`employee_id`),
  ADD KEY `salary_id` (`salary_id`);

--
-- Indexes for table `leave`
--
ALTER TABLE `leave`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employee_id` (`employee_id`);

--
-- Indexes for table `messages`
--
ALTER TABLE `messages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_user_id` (`room_user_id`);

--
-- Indexes for table `payslips`
--
ALTER TABLE `payslips`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employee_id` (`employee_id`);

--
-- Indexes for table `positions`
--
ALTER TABLE `positions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `department_id` (`department_id`);

--
-- Indexes for table `rooms`
--
ALTER TABLE `rooms`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `room_users`
--
ALTER TABLE `room_users`
  ADD PRIMARY KEY (`id`),
  ADD KEY `room_id` (`room_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `salaries`
--
ALTER TABLE `salaries`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `company_email` (`company_email`),
  ADD KEY `employee_id` (`employee_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `announcements`
--
ALTER TABLE `announcements`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=37;

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=199;

--
-- AUTO_INCREMENT for table `departments`
--
ALTER TABLE `departments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `employee_info`
--
ALTER TABLE `employee_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `employment_info`
--
ALTER TABLE `employment_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=34;

--
-- AUTO_INCREMENT for table `leave`
--
ALTER TABLE `leave`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=66;

--
-- AUTO_INCREMENT for table `messages`
--
ALTER TABLE `messages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `payslips`
--
ALTER TABLE `payslips`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=275;

--
-- AUTO_INCREMENT for table `positions`
--
ALTER TABLE `positions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT for table `rooms`
--
ALTER TABLE `rooms`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT for table `room_users`
--
ALTER TABLE `room_users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT for table `salaries`
--
ALTER TABLE `salaries`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `announcements`
--
ALTER TABLE `announcements`
  ADD CONSTRAINT `announcements_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `employee_info`
--
ALTER TABLE `employee_info`
  ADD CONSTRAINT `employee_info_ibfk_1` FOREIGN KEY (`position_id`) REFERENCES `positions` (`id`);

--
-- Constraints for table `employment_info`
--
ALTER TABLE `employment_info`
  ADD CONSTRAINT `employment_info_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `employment_info_ibfk_2` FOREIGN KEY (`salary_id`) REFERENCES `salaries` (`id`);

--
-- Constraints for table `leave`
--
ALTER TABLE `leave`
  ADD CONSTRAINT `leave_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `messages`
--
ALTER TABLE `messages`
  ADD CONSTRAINT `messages_ibfk_1` FOREIGN KEY (`room_user_id`) REFERENCES `room_users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `payslips`
--
ALTER TABLE `payslips`
  ADD CONSTRAINT `payslips_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `positions`
--
ALTER TABLE `positions`
  ADD CONSTRAINT `positions_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `rooms`
--
ALTER TABLE `rooms`
  ADD CONSTRAINT `rooms_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `room_users`
--
ALTER TABLE `room_users`
  ADD CONSTRAINT `room_users_ibfk_1` FOREIGN KEY (`room_id`) REFERENCES `rooms` (`id`) ON DELETE CASCADE,
  ADD CONSTRAINT `room_users_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE;

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
