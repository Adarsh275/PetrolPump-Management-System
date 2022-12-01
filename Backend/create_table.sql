SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


CREATE TABLE IF NOT EXISTS `PetrolPump`(
   `Registration_No` varchar(10) NOT NULL,
   `Petrolpump_Name` varchar(50) NOT NULL, 
   `Company_Name` varchar(30) DEFAULT NULL, 
   `Opening_Year` int(5) DEFAULT NULL,
   `State` varchar(30) DEFAULT NULL,
   `City` varchar(40) NOT NULL,
   PRIMARY KEY(`Registration_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `PetrolPump` (`Registration_No`, `Petrolpump_Name`,`Company_Name`, `Opening_Year`, `State`, `City`) VALUES
('HPC805103', 'Sumaraj Petroleum', 'Hindustan Petroleum Corporation',2016,'Bihar','Hisua'),
('BP110054', 'Rajinder Service Station', 'Bharat Petroleum',2012,'Delhi','CENTRAL DELHI'),
('IOC560008', 'Madhu Enterprises', 'Indian Oil Corporation',2008,'Karnataka','Banglore'),
('OIL380013', 'Perusahaan Minyak and Gas Bumi', 'Oil India Limited',2006,'Gujarat','Ahmedabad'),
('RPL673573','Tamarassery Reliance Retail Outlet','Reliance Petroleum Limited',2013,'Kerala','Thamarasserry');


CREATE TABLE IF NOT EXISTS `Owners`(
   `Owner_Name` varchar(20) NOT NULL,
   `Contact_NO` char(10) NOT NULL, 
   `DOB` date DEFAULT NULL, 
   `Gender` char DEFAULT NULL,
   `Address` varchar(255) DEFAULT NULL,
   `Partnership` int(5) NOT NULL,
   PRIMARY KEY(`Owner_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Owners` (`Owner_Name`, `Contact_NO`, `DOB`, `Gender`, `Address`, `Partnership`) VALUES
('Pawan Kumar','9431073500', '1971-01-03', 'M', 'Friends colony more,Patna,Bihar',35 ),
('Avinash Shankar','8783249500','1973-07-15', 'M', 'Buddha colony,Patna,Bihar',25),
('Vikash Kumar Tarun', '7486249500', '1975-02-05','M','Tapeshwer Path,Boring road,Patna,Bihar',45),
('Nirmal Sethi', '6427894500', '1999-09-11','F','Pritam Nagar, Paldi, Ahmedabad, Gujarat',70),
('Neerja Bhanot', '5963154800','2000-02-24', 'F', 'Quarters, Sarojini Nagar,New Delhi',55);


CREATE TABLE IF NOT EXISTS `Tanker`(
   `Tanker_ID` varchar(10) NOT NULL,
   `Capacity` float(10) DEFAULT NULL, 
   `pressure` float(10) DEFAULT NULL, 
   `Fuel_ID` varchar(10) NOT NULL,
   `Fuel_Amount` float(15) DEFAULT NULL,
   `Fuel_Name` varchar(20) DEFAULT NULL,
   `Fuel_Price` float(5) NOT NULL,
   `Petrolpump_No`varchar(10) DEFAULT NULL,
   PRIMARY KEY(`Tanker_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Tanker` (`Tanker_ID`, `Capacity`, `pressure`, `Fuel_ID`,`Fuel_Amount`, `Fuel_Name`,  `Fuel_Price`, `Petrolpump_No`) VALUES
('BR6872', 5000,550,'A1234',513.50,'PetrolE10',101.72,'HPC805103'),
('JK2611', 1000,845,'L7363',238.24,'Kerosene',77.03,'OIL380013'),
('MP4928', 5000,1545,'K5363',1200.95,'CNG',99.50,'BP110054'),
('JH7523', 10000,3500,'Z6353',751.89,'Diesel',87.89,'HPC805103'),
('UP9875', 15000,785,'R4743',576.26,'Gasoline91',107.05,'OIL380013');


CREATE TABLE IF NOT EXISTS `Employee`(
   `Employee_ID` varchar(10) NOT NULL,
   `Emp_Name` varchar(30) NOT NULL, 
   `Emp_Gender`char DEFAULT NULL, 
   `Designation` varchar(10) DEFAULT NULL,
   `DOB` date DEFAULT NULL, 
   `Salary` int(20) DEFAULT NULL,
   `Emp_Address` varchar(255) NOT NULL,
   `Email_ID`varchar(100) NOT NULL,
   `Petrolpump_No`varchar(10) DEFAULT NULL,
   `Manager_ID` varchar(10) DEFAULT NULL,
   PRIMARY KEY(`Employee_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Employee` (`Employee_ID`, `Emp_Name`, `Emp_Gender`, `Designation`, `DOB`, `Salary`, `Emp_Address`, `Email_ID`, `Petrolpump_No`, `Manager_ID`) VALUES
('FOED452','Sheela Reddy','F','FOOD MANAGEMENT','1989-11-28',45000,'dakbangla choraha,patna','sheela@gmail.com','HPC805103','MANG957'),
('DRHD746','Hima Ullal','F','COOKING','1995-04-18',25000,'Bikram Road, Patna','hima@gmail.com','HPC805103','FOED452'),
('MANG957','Aman kumar','M','MANAGER','1992-01-21',65000,'Boaring road, patna','Aman@outlook.com','HPC805103','MANG957'),
('FDNG652','Hradha Nayar','F','NOZZEL PERSON','1987-08-09',35000,'Pandit Bigha, Gaya','hradha@hotmail.com','HPC805103','FDEW353'),
('FDSNG43','Hemant','M','CLEANING','1995-01-23',20000,'Kanvada, Magrol road, Surat','hemant@gmail.com','OIL380013',NULL),
('SNGED76','Animesh','M','NOZZEL PERSON','1982-08-13',45000,'Industrial Development Area, Sector 16, Gurugram, Haryana' ,'animesh@gmail.com','OIL380013',NULL),
('FDEW353','Saideepak Reddy','M','NOZZEL PERSON','2000-06-30',40000,'Lodwadih, Topchanchi, Jharkhand','saideepak@outlook.com','HPC805103','MANG957');


CREATE TABLE IF NOT EXISTS `Customer`(
   `Customer_Code` varchar(10) NOT NULL,
   `C_Name` varchar(30) NOT NULL, 
   `Phone_No`char(10) DEFAULT NULL, 
   `Email_ID`varchar(100) DEFAULT NULL,
   `Gender`char DEFAULT NULL, 
   `City` varchar(50) DEFAULT NULL,
   `Age` int(3) DEFAULT NULL,
   PRIMARY KEY(`Customer_Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Customer` (`Customer_Code`, `C_Name`, `Phone_No`, `Email_ID`, `Gender`, `City`, `Age`) VALUES
('SFG252','Akash','6542589700','akash@gmail.com','M','Bihar', 27),
('GHE785','Praneet','7539514600','praneet@yahoo.com','M','Orissa',59),
('FJD253','Chetan','8426951300','chetan@hotmail.com','M','Bengalore', 24),
('OUI325','Ayush','7618425500','ayush@outlook.com','M','Kota',18),
('CGM235','Vinesh','6794324600','vines@pesu.pes.edu','M','Kolkata',54),
('BFR426','Anamika',9569731800,'anamika@gmai.com','F','Jharkhand',26);


CREATE TABLE IF NOT EXISTS `Invoice`(
   `Invoice_No` varchar(10) NOT NULL,
   `Date` date NOT NULL,
   `Payment_Type` varchar(20) NOT NULL,
   `Fuel_Amount` float(15) DEFAULT NULL,
   `Fuel_Type` varchar(15) DEFAULT NULL,
   `Discount` int(5) DEFAULT NULL,
   `Total_Price` float(10) NOT NULL,
   `Customer_Code` varchar(10) NULL,
   PRIMARY KEY(`Invoice_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Invoice` (`Invoice_No`, `Date`, `Payment_Type`, `Fuel_Amount`, `Fuel_Type`, `Discount`, `Total_Price`, `Customer_Code`) VALUES
('XC34','2022-11-20','Cash',7,'PetrolE10',10,640.83,'BFR426'),
('NR43','2022-11-20','UPI', 5.4,'Gasoline91',NULL, 578.07,'GHE785'),
('MN34','2020-06-30','Credit Card', 15.8,'Diesel',7.5, 1284.51,'OUI325'),
('FG43','2022-10-27','UPI', 4.9,'Gasoline91',5, 498.32,'SFG252'),
('DS85','2019-08-19','Debit Card', 6.8,'Diesel',NULL, 597.65,'OUI325');


CREATE TABLE IF NOT EXISTS `Sales`(
   `Sales_No` varchar(10) NOT NULL,
   `Date` date NOT NULL, 
   `Nozzel_No` int(4) NOT NULL,
   `Starting_Reading` int(7) NOT NULL,
   `Ending_Reading` int(7) NOT NULL,
   `Total_Sales` float(10) NOT NULL,
   `Sales_Amount` float(10) NOT NULL,
   `Petrolpump_No`varchar(10) DEFAULT NULL,
   PRIMARY KEY(`Sales_No`,`Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Sales` (`Sales_No`, `Date`, `Nozzel_No`, `Starting_Reading`, `Ending_Reading`, `Total_Sales`, `Sales_Amount`, `Petrolpump_No`) VALUES
('FGHGE32','2022-11-20', 1, 45687,49782 , 17584.45, 106.52,'HPC805103'),
('MVBER67','2022-11-20', 2, 48325, 53842, 4253.45, 205.5,'OIL380013'),
('IUOSF98','2019-08-19', 2, 12757, 23454, 1254.71, 89.45,'HPC805103'),
('GDZJD24','2019-08-19', 1, 62725,68725 , 5466.45, 125.85,'OIL380013'),
('QWRGH87','2022-11-22', 3, 12758, 19758, 7854.65, 425.25,'HPC805103');


CREATE TABLE IF NOT EXISTS `Owns`(
   `Registration_No` varchar(10) NOT NULL,
   `Owner_Name` varchar(20) NOT NULL,
   PRIMARY KEY(`Registration_No`, `Owner_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Owns` (`Registration_No`,`Owner_Name`) VALUES
('HPC805103','Pawan Kumar'),
('HPC805103','Avinash Shankar'),
('HPC805103','Vikash Kumar Tarun'),
('OIL380013','Nirmal Sethi'),
('OIL380013','Vikash Kumar Tarun'),
('BP110054','Neerja Bhanot'),
('BP110054','Pawan Kumar');


CREATE TABLE IF NOT EXISTS `Contacts`(
   `Employee_ID` varchar(10) NOT NULL,
   `Contact_NO` char(10) NOT NULL,
   PRIMARY KEY(`Employee_ID`, `Contact_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Contacts` (`Employee_ID`, `Contact_NO`) VALUES
('MANG957','6299337300'),
('MANG957','8540074600'),
('FOED452','6256575800'),
('FOED452','9678225400'),
('FDSNG43','8312243800'),
('FDNG652','5249785500');


CREATE TABLE IF NOT EXISTS `Serves`(
   `Employee_ID` varchar(10) NOT NULL,
   `Customer_Code` varchar(10) NOT NULL,
   PRIMARY KEY(`Employee_ID`, `Customer_Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Serves` (`Employee_ID`, `Customer_Code`) VALUES
('FDEW353','SFG252'),
('FDEW353','CGM235'),
('FDEW353','BFR426'),
('FDNG652','SFG252'),
('FDNG652','CGM235');

CREATE TABLE IF NOT EXISTS `Sales_Manage`(
   `Employee_ID` varchar(10) NOT NULL,
   `Sales_No` varchar(10) NOT NULL,
   `Date` date NOT NULL, 
   PRIMARY KEY(`Employee_ID`, `Sales_No`, `Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

INSERT INTO `Sales_Manage`(`Employee_ID`, `Sales_No`, `Date`) VALUES
('FDEW353','FGHGE32','2022-11-20'),
('FDEW353','IUOSF98','2019-08-19'),
('FDNG652','QWRGH87','2022-11-22'),
('SNGED76','GDZJD24','2019-08-19'),
('SNGED76','MVBER67','2022-11-20');

COMMIT;