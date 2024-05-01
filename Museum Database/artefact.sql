DROP DATABASE IF EXISTS Artefacts;

CREATE DATABASE Artefacts;

USE Artefacts;

CREATE TABLE Restauration (
  ID int(10) PRIMARY KEY,
  FQ_Restauration varchar(50) NOT NULL UNIQUE
);

CREATE TABLE Location (
  ID int(100) PRIMARY KEY,
  Room_Number varchar(50) NOT NULL UNIQUE 
);

CREATE TABLE Historical_Period (
  ID int NOT NULL PRIMARY KEY,
  Historical_Period_Name varchar(20) NOT NULL UNIQUE
);

CREATE TABLE State (
  ID int NOT NULL PRIMARY KEY,
  State varchar(30) NOT NULL UNIQUE
);

CREATE TABLE Artefact (
  Name_Artefact varchar(50),
  ID int NOT NULL PRIMARY KEY UNIQUE,
  Characteristics varchar(255),
  Year_Acquired year,
  Historical_Period_Name varchar(20) NOT NULL, 
  FQ_Restauration varchar(50) NOT NULL,
  State varchar(30) NOT NULL,
  Room_Number varchar(50) NOT NULL,                          
  FOREIGN KEY (Historical_Period_Name) REFERENCES Historical_Period(Historical_Period_Name),
  FOREIGN KEY (Room_Number) REFERENCES Location(Room_Number),
  FOREIGN KEY (FQ_Restauration) REFERENCES Restauration(FQ_Restauration),
  FOREIGN KEY (State) REFERENCES State(State)
);


INSERT INTO State (ID, State)
VALUES
(1, 'Research Finished'),
(2, 'Ongoing Research'),
(3, 'In Restauration');

INSERT INTO Restauration (ID, FQ_Restauration)
VALUES
(1, 'Every 6 months'),
(2, 'Every 1 year'),
(3, 'Every 2 years'),
(4, 'Every 3 years'),
(5, 'Every 4 years');

INSERT INTO Location (ID, Room_Number)
VALUES
(0, 'Restauration Room'),
(1, 'Room 1'),
(2, 'Room 2'),
(3, 'Room 3');


INSERT INTO Historical_Period (ID, Historical_Period_Name) 
VALUES 
(1, 'Archaic Period'),
(2, 'Classical Period'),
(3, 'Hellenistic Period'),
(4, 'Old Kingdom'),
(5, 'Middle Kingdom'),
(6, 'New Kingdom'),
(7, 'Ptolemaic Period');

INSERT INTO Artefact (Name_Artefact, ID, FQ_Restauration, Characteristics, Year_Acquired, Historical_Period_Name, Room_Number, State) 
VALUES
('Tetradrachma', 1002003004, 'Every 4 years', 'A Greek four drachma silver coin from 227-221 BCE from Macedonia. It displays the face of Poseidon, God of the seas.', 2009, 'Hellenistic Period', 'Room 1', 'Research Finished'),
('Lekythos', 1005006007, 'Every 1 year', 'A white Pottery Lekythos from the Greek Classical Period, still in Research.', 2014, 'Classical Period', 'Restauration Room', 'In Restauration'),
('Amphora', 1008009000, 'Every 1 year', 'Year unknown, from Hellenistic Period, an Amphora possibly displaying a shrine scene.', 2023, 'Hellenistic Period', 'Restauration Room', 'In Restauration'),
('Drinking Vessel', 1009008007, 'Every 1 year', 'Found in Athens, this pottery Drinking cup, also known as skyphos, displays two armed warriors in combat, on each side, with the name of one of the warriors painted.', 2012, 'Archaic Period', 'Room 2', 'Research Finished'),
('Ostracon', 2001002003, 'Every 2 years', 'A limestone chip used for sketching, found in the Valley of the Kings, it represents a hunting scene with an unidentified pharaoh.', 2022, 'New Kingdom', 'Room 3', 'Ongoing Research'),
('Traveling Boat',2004005006, 'Every 6 months', 'A model of a riverboat from the Middle Kingdom, found in a hidden chamber.',  2017, 'Middle Kingdom', 'Restauration Room', 'In Restauration'),
('Nikare Statue', 2007008009, 'Every 2 years', 'Statue representing Nikare with his family, from the Old Kingdom.', 2022, 'Old Kingdom', 'Room 3', 'Research Finished'),
('Statue of Tawaret', 2009008007, 'Every 3 years', 'Statuette representing Goddess Tawaret, protector of pregnant women, especially during childbirth.', 2023, 'Ptolemaic Period', 'Room 3', 'Ongoing Research');
