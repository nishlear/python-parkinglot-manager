CREATE DATABASE parking;
USE parking;

CREATE TABLE member(
	memberID int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    plate varchar(255),
    PRIMARY KEY (memberID)
);

CREATE TABLE staff(
	staffID int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    phone varchar(255),
    PRIMARY KEY (staffID)
);

CREATE TABLE ticket(
	ticketID int NOT NULL AUTO_INCREMENT,
    staffID int NOT NULL,
    memberID int,
    cash int,
    plate varchar(255),
    vehicletype int,
    time_in datetime,
    time_out datetime,
    PRIMARY KEY (ticketID),
    FOREIGN KEY (staffID) REFERENCES staff(staffID),
    FOREIGN KEY (memberID) REFERENCES member(memberID)
);

ALTER TABLE ticket ADD UNIQUE (plate);
ALTER TABLE staff ADD UNIQUE (phone);



