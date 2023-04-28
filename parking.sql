CREATE DATABASE parking;
USE parking;

CREATE TABLE NguoiGuiXe (
	phone varchar(10),
    name varchar(255)
);
CREATE TABLE Xe (
	plate varchar(255) PRIMARY KEY,
    vehicleType int,
    phone varchar(10)
);
CREATE TABLE VeGuiXe (
	ticketID int NOT NULL AUTO_INCREMENT,
    workerID int NOT NULL,
    cash int NOT NULL,
    plate varchar(255),
    PRIMARY KEY (ID)
);
CREATE TABLE NhanVien (
	workerID int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    phone varchar(10),
    PRIMARY KEY (workerID)
);
SET SQL_SAFE_UPDATES = 0;

ALTER TABLE NhanVien ADD UNIQUE (phone);
ALTER TABLE VeGuiXe ADD UNIQUE (plate);
