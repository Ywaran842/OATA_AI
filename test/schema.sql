-- MySQL dump 10.13  Distrib 8.0.36, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: test
-- ------------------------------------------------------
-- Server version 8.0.39-0ubuntu0.22.04.1

CREATE TABLE IF NOT EXISTS Users1 (
  username varchar(30) NOT NULL,
  password varchar(250) NOT NULL,
  mailid varchar(45) NOT NULL,
  id varchar(36) NOT NULL,
  PRIMARY KEY (id),
  UNIQUE KEY id_UNIQUE (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
