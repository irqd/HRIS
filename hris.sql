-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 10, 2023 at 01:38 AM
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
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `id` int(11) NOT NULL,
  `date` date NOT NULL,
  `attendance_type` enum('Present','Absent','Unavailable') NOT NULL,
  `status` enum('Approved','Declined','Pending') NOT NULL,
  `start_shift` time NOT NULL,
  `end_shift` time NOT NULL,
  `checked_in` time DEFAULT NULL,
  `checked_out` time DEFAULT NULL,
  `pre_ot` time NOT NULL,
  `post_ot` time DEFAULT NULL,
  `employee_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Table structure for table `departments`
--

CREATE TABLE `departments` (
  `id` int(11) NOT NULL,
  `department_name` varchar(50) NOT NULL,
  `supervisor` varchar(50) DEFAULT NULL,
  `description` varchar(500) DEFAULT NULL,
  `date_created` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `departments`
--

INSERT INTO `departments` (`id`, `department_name`, `supervisor`, `description`, `date_created`) VALUES
(1, 'IT Department', NULL, 'IT Dept.', '2023-02-09'),
(2, 'HR Department', NULL, 'Hr Dept.', '2023-02-09');

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
(1, 'Deposoy', 'Ivan Rey', 'Quistadio', 'Male', '2001-07-12', 'Single', '0912345678901', 'ivan@gmail.com', 'Muntinlupa', 'Ivan', '0912345678901', 'Self', '0123456789', '0123456789', '0123456789', '0123456789', '2023-02-09', 1),
(2, 'Paguio', 'Alfred', 'Umali', 'Male', '2000-03-06', 'Single', '0912345678901', 'alfred@gmail.com', 'Muntinlupa', 'Alfred', '0912345678901', 'Self', '9876543210', '9876543210', '9876543210', '9876543210', '2023-02-09', 2);

-- --------------------------------------------------------

--
-- Table structure for table `employment_info`
--

CREATE TABLE `employment_info` (
  `id` int(11) NOT NULL,
  `description` varchar(500) DEFAULT NULL,
  `salary_package` varchar(50) NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date DEFAULT NULL,
  `status` enum('Hired','Retired','Terminated') NOT NULL,
  `employee_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employment_info`
--

INSERT INTO `employment_info` (`id`, `description`, `salary_package`, `start_date`, `end_date`, `status`, `employee_id`) VALUES
(1, 'Employment Info of Ivan', '15000', '2023-02-09', NULL, 'Hired', 1),
(2, 'For alfred', '15000', '2023-02-09', NULL, 'Hired', 2);

-- --------------------------------------------------------

--
-- Table structure for table `leave`
--

CREATE TABLE `leave` (
  `id` int(11) NOT NULL,
  `type` enum('Sick_Leave','SIL','Maternity_Leave','Paternity_Leave','Vacation_Leave','Parental_Leave','Rehabilitation_Leave','Study_Leave') NOT NULL,
  `date_requested` date NOT NULL,
  `start_date` date NOT NULL,
  `end_date` date NOT NULL,
  `status` enum('Approved','Declined','Pending') NOT NULL,
  `approved_date` date NOT NULL,
  `approved_by` varchar(50) NOT NULL,
  `employee_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

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
(2, 'HR Sttaff', 'Hr Staff', 'Hiring', '2023-02-09', 2);

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
(1, 'Ivan Rey Q. Deposoy', 'images/profile.svg', 'ivan@gmail.com', '$2b$12$jlLnqDSpT8mdWITfXRJgz./owKxivBamnDNl7S7kAK2xSV7oIdMDW', 'Employee', '2023-02-09', 1),
(2, 'Alfred U. Paguio', 'images/profile.svg', 'alfred@gmail.com', '$2b$12$jlLnqDSpT8mdWITfXRJgz./owKxivBamnDNl7S7kAK2xSV7oIdMDW', 'Admin', '2023-02-09', 2);

--
-- Indexes for dumped tables
--

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
  ADD KEY `employee_id` (`employee_id`);

--
-- Indexes for table `leave`
--
ALTER TABLE `leave`
  ADD PRIMARY KEY (`id`),
  ADD KEY `employee_id` (`employee_id`);

--
-- Indexes for table `positions`
--
ALTER TABLE `positions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `department_id` (`department_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `company_email` (`company_email`),
  ADD UNIQUE KEY `access` (`access`),
  ADD KEY `employee_id` (`employee_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `attendance`
--
ALTER TABLE `attendance`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `departments`
--
ALTER TABLE `departments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `employee_info`
--
ALTER TABLE `employee_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `employment_info`
--
ALTER TABLE `employment_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `leave`
--
ALTER TABLE `leave`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `positions`
--
ALTER TABLE `positions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`);

--
-- Constraints for table `employee_info`
--
ALTER TABLE `employee_info`
  ADD CONSTRAINT `employee_info_ibfk_1` FOREIGN KEY (`position_id`) REFERENCES `positions` (`id`);

--
-- Constraints for table `employment_info`
--
ALTER TABLE `employment_info`
  ADD CONSTRAINT `employment_info_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`);

--
-- Constraints for table `leave`
--
ALTER TABLE `leave`
  ADD CONSTRAINT `leave_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`);

--
-- Constraints for table `positions`
--
ALTER TABLE `positions`
  ADD CONSTRAINT `positions_ibfk_1` FOREIGN KEY (`department_id`) REFERENCES `departments` (`id`);

--
-- Constraints for table `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_1` FOREIGN KEY (`employee_id`) REFERENCES `employee_info` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
