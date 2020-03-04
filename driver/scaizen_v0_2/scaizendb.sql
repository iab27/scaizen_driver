-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 18-02-2020 a las 15:30:52
-- Versión del servidor: 10.3.16-MariaDB
-- Versión de PHP: 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `scaizendb`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `batchprocess`
--

CREATE TABLE `batchprocess` (
  `id_batchProcess` int(11) NOT NULL,
  `batch` int(11) NOT NULL,
  `id_process` int(11) NOT NULL,
  `blockchain` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tiemporeal`
--

CREATE TABLE `tiemporeal` (
  `id_tiempoReal` int(11) NOT NULL,
  `timeStamp` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `GOVsolicitado` float NOT NULL,
  `GOVcomponente` float NOT NULL,
  `GOVtotal` float NOT NULL,
  `GSV` float NOT NULL,
  `flujoPreset` float NOT NULL,
  `flujoTR` float NOT NULL,
  `presionPreset` float NOT NULL,
  `presionTR` float NOT NULL,
  `densidadTR` float NOT NULL,
  `densidadComponent` float NOT NULL,
  `temperaturaTR` float NOT NULL,
  `temperaturaAvg` float NOT NULL,
  `masaTR` float NOT NULL,
  `BSWTR` float NOT NULL,
  `gravidadTR` float NOT NULL,
  `kFactor` tinyint(4) NOT NULL,
  `unidadGOV` char(7) NOT NULL,
  `unidadFlujo` char(7) NOT NULL,
  `unidadPresion` char(7) NOT NULL,
  `unidadDensidad` char(7) NOT NULL,
  `unidadTemperatura` char(7) NOT NULL,
  `unidadMasa` char(7) NOT NULL,
  `unidadBSW` char(7) NOT NULL,
  `unidadGravidad` char(7) NOT NULL,
  `blockchain` varchar(64) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `batchprocess`
--
ALTER TABLE `batchprocess`
  ADD PRIMARY KEY (`id_batchProcess`);

--
-- Indices de la tabla `tiemporeal`
--
ALTER TABLE `tiemporeal`
  ADD PRIMARY KEY (`id_tiempoReal`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `batchprocess`
--
ALTER TABLE `batchprocess`
  MODIFY `id_batchProcess` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `tiemporeal`
--
ALTER TABLE `tiemporeal`
  MODIFY `id_tiempoReal` int(11) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
