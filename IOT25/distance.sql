-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 29, 2023 at 07:46 PM
-- Server version: 10.3.39-MariaDB-0+deb10u1
-- PHP Version: 7.3.31-1~deb10u5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `sensor`
--

-- --------------------------------------------------------

--
-- Table structure for table `distance`
--

CREATE TABLE `distance` (
  `RecordID` mediumint(9) NOT NULL,
  `inches` int(11) NOT NULL,
  `timestamp` text CHARACTER SET latin7 COLLATE latin7_general_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `distance`
--

INSERT INTO `distance` (`RecordID`, `inches`, `timestamp`) VALUES
(11, 79, '2023-10-29 19:40:48.351849'),
(12, 46, '2023-10-29 19:40:53.384652'),
(13, 50, '2023-10-29 19:40:58.412680'),
(14, 79, '2023-10-29 19:41:03.439317'),
(15, 48, '2023-10-29 19:41:08.474435'),
(16, 193, '2023-10-29 19:41:13.531259'),
(17, 79, '2023-10-29 19:41:18.563023'),
(18, 79, '2023-10-29 19:41:23.599838'),
(19, 79, '2023-10-29 19:41:28.633533'),
(20, 62, '2023-10-29 19:41:33.665200'),
(21, 68, '2023-10-29 19:41:38.699373'),
(22, 193, '2023-10-29 19:41:43.755327'),
(23, 79, '2023-10-29 19:41:48.789655'),
(24, 79, '2023-10-29 19:41:53.823871'),
(25, 57, '2023-10-29 19:41:58.855345'),
(26, 79, '2023-10-29 19:42:03.897226'),
(27, 193, '2023-10-29 19:42:08.949736'),
(28, 79, '2023-10-29 19:42:13.983478'),
(29, 43, '2023-10-29 19:42:19.018053'),
(30, 48, '2023-10-29 19:42:24.063334'),
(31, 79, '2023-10-29 19:42:29.101298'),
(32, 79, '2023-10-29 19:42:34.135573'),
(33, 73, '2023-10-29 19:42:39.167367'),
(34, 48, '2023-10-29 19:42:44.196170'),
(35, 193, '2023-10-29 19:42:49.250894');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `distance`
--
ALTER TABLE `distance`
  ADD PRIMARY KEY (`RecordID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `distance`
--
ALTER TABLE `distance`
  MODIFY `RecordID` mediumint(9) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=76;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
