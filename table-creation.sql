-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema grade_12_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema grade_12_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `grade_12_db` DEFAULT CHARACTER SET utf8 ;
USE `grade_12_db` ;

-- -----------------------------------------------------
-- Table `grade_12_db`.`Hospital`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Hospital` (
  `No` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NOT NULL,
  `Age` INT UNSIGNED NOT NULL,
  `Department` VARCHAR(45) NULL,
  `Dateofadm` DATE NULL,
  `Charges` INT UNSIGNED NULL,
  `Sex` CHAR(1) NULL,
  PRIMARY KEY (`No`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`School_Bus`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`School_Bus` (
  `RtNo` INT NOT NULL AUTO_INCREMENT,
  `Area_covered` VARCHAR(45) NULL,
  `Capacity` INT NULL,
  `Noofstud` INT NULL,
  `Dist` INT NULL,
  `Transporter` VARCHAR(45) NULL,
  `Charges` INT NULL,
  PRIMARY KEY (`RtNo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Coach`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Coach` (
  `CoachID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `CoachName` VARCHAR(45) NULL,
  `Age` INT UNSIGNED NULL,
  `Sports` VARCHAR(45) NULL,
  `DOJ` DATE NULL,
  `Fee` INT NULL,
  `Sex` CHAR(1) NULL,
  PRIMARY KEY (`CoachID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Worker`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Worker` (
  `Ecode` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `Designation` VARCHAR(45) NULL,
  `PLevel` VARCHAR(10) NULL,
  `DOB` DATE NULL,
  PRIMARY KEY (`Ecode`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Movie`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Movie` (
  `No` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Title` VARCHAR(45) NULL,
  `Type` VARCHAR(45) NULL,
  `Rating` VARCHAR(5) NULL,
  `Stars` VARCHAR(25) NULL,
  `Qty` INT NULL,
  `Price` FLOAT(5,2) NULL,
  PRIMARY KEY (`No`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Sports_Master`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Sports_Master` (
  `Event_name` VARCHAR(45) NULL,
  `Evt_code` INT NOT NULL,
  `No_in_team` INT NULL,
  `Event_date` DATE NULL,
  `Category` VARCHAR(10) NULL,
  PRIMARY KEY (`Evt_code`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Employee`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Employee` (
  `Eid` INT NOT NULL AUTO_INCREMENT,
  `Name` VARCHAR(45) NULL,
  `Deptid` INT NULL,
  `Qualification` VARCHAR(30) NULL,
  `Sex` CHAR(1) NULL,
  PRIMARY KEY (`Eid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Items`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Items` (
  `No` INT NOT NULL AUTO_INCREMENT,
  `ItemName` VARCHAR(45) NULL,
  `CostPerItem` INT UNSIGNED NULL,
  `Quantity` INT UNSIGNED NULL,
  `DateOfPurchase` DATE NULL,
  PRIMARY KEY (`No`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Stationery`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Stationery` (
  `S_ID` CHAR(4) NOT NULL,
  `StationeryName` VARCHAR(45) NULL,
  `Company` CHAR(3) NULL,
  `Price` INT UNSIGNED NULL,
  PRIMARY KEY (`S_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Voter`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Voter` (
  `Vno` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Vname` VARCHAR(45) NULL,
  `Age` INT UNSIGNED NULL,
  `Address` VARCHAR(45) NULL,
  `Phone` INT NULL,
  PRIMARY KEY (`Vno`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Interiors`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Interiors` (
  `NO` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `ITEMNAME` VARCHAR(45) NULL,
  `TYPE` VARCHAR(45) NULL,
  `DATEOFSTOCK` DATE NULL,
  `PRICE` INT NULL,
  `DISCOUNT` INT NULL,
  PRIMARY KEY (`NO`))
ENGINE = InnoDB
COMMENT = '	';


-- -----------------------------------------------------
-- Table `grade_12_db`.`Watches`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Watches` (
  `Watchid` CHAR(4) NOT NULL,
  `Watch_Name` VARCHAR(45) NULL,
  `Price` INT NULL,
  `Type` VARCHAR(45) NULL,
  `Qty_Store` INT NULL,
  PRIMARY KEY (`Watchid`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Customer_Info`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Customer_Info` (
  `SNo` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `Acc_No` INT NULL,
  `Cust_Name` VARCHAR(45) NULL,
  `Cust_Add` VARCHAR(45) NULL,
  `Cust_City` VARCHAR(45) NULL,
  `Cust__Phone` CHAR(10) NULL,
  PRIMARY KEY (`SNo`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Transaction_Detail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Transaction_Detail` (
  `Trans_Id` CHAR(4) NOT NULL,
  `Acc_No` INT NULL,
  `Transaction_Type` VARCHAR(45) NULL,
  `Amount` INT NULL,
  PRIMARY KEY (`Trans_Id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Flights`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Flights` (
  `FNO` CHAR(5) NOT NULL,
  `Source` VARCHAR(45) NULL,
  `Dest` VARCHAR(45) NULL,
  `No_of_fl` INT NULL,
  `No_of_stop` INT NULL,
  PRIMARY KEY (`FNO`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `grade_12_db`.`Fares`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `grade_12_db`.`Fares` (
  `FNO` CHAR(5) NOT NULL,
  `Airlines` VARCHAR(45) NULL,
  `Fare` INT NULL,
  `TAX` INT NULL,
  PRIMARY KEY (`FNO`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
