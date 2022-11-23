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

-- INSERT INTO `PetrolPump` (`Registration_No`, `Petrolpump_Name`,`Company_Name`, `Opening_Year`, `State`, `City`) VALUES
-- ('', '', '',  ,'', ''),
-- ('', '', '',  ,'', ''),
-- ('', '', '',  ,'', ''),
-- ('', '', '',  ,'', ''),
-- ('', '', '',  ,'', '');


CREATE TABLE IF NOT EXISTS `Owners`(
   `Owner_Name` varchar(20) NOT NULL,
   `Contact_NO` char(10) NOT NULL, 
   `DOB` date DEFAULT NULL, 
   `Gender` char DEFAULT NULL,
   `Address` varchar(255) DEFAULT NULL,
   `Partnership` int(5) NOT NULL,
   PRIMARY KEY(`Owner_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- INSERT INTO `Owners` (`Owner_Name`, `Contact_NO`, `DOB`, `Gender`, `Address`, `Partnership`) VALUES
-- ('', '', '', '', '', ),
-- ('', '', '', '', '', ),
-- ('', '', '', '', '', ),
-- ('', '', '', '', '', ),
-- ('', '', '', '', '', );


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

-- INSERT INTO `Tanker` (`Tanker_ID`, `Capacity`, `pressure`, `Fuel_ID`, `Fuel_Name`, `Fuel_Amount`, `Fuel_Price`, `Petrolpump_No`) VALUES
-- ('', , ,'', ,'', ,''),
-- ('', , ,'', ,'', ,''),
-- ('', , ,'', ,'', ,''),
-- ('', , ,'', ,'', ,''),
-- ('', , ,'', ,'', ,'');


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

-- INSERT INTO (`Employee_ID`, `Emp_Name`, `Emp_Gender`, `Designation`, `DOB`, `Salary`, `Emp_Address`, `Email_ID`, `Petrolpump_No`, `Manager_ID`) VALUES
-- ('','','','','', ,'','','',''),
-- ('','','','','', ,'','','',''),
-- ('','','','','', ,'','','',''),
-- ('','','','','', ,'','','',''),
-- ('','','','','', ,'','','','');


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

-- INSERT INTO (`Customer_Code`, `C_Name`, `Phone_No`, `Email_ID`, `Gender`, `City`, `Age`) VALUES
-- ('','','','','','', ),
-- ('','','','','','', ),
-- ('','','','','','', ),
-- ('','','','','','', ),
-- ('','','','','','', );


CREATE TABLE IF NOT EXISTS `Invoice`(
   `Invoice_No` varchar(10) NOT NULL,
   `Date` date NOT NULL, 
   `Time` time NOT NULL, 
   `Payment_Type` varchar(20) NOT NULL,
   `Fuel_Amount` float(15) DEFAULT NULL,
   `Fuel_Type` varchar(15) DEFAULT NULL,
   `Discount` int(5) DEFAULT NULL,
   `Total_Price` float(10) NOT NULL,
   `Customer_Code` varchar(10) NULL,
   PRIMARY KEY(`Invoice_No`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- INSERT INTO (`Invoice_No`, `Date`, `Time`, `Payment_Type`, `Fuel_Amount`, `Fuel_Type`, `Discount`, `Total_Price`, `Customer_Code`) VALUES
-- ('','','','',  ,'', , ,''),
-- ('','','','',  ,'', , ,''),
-- ('','','','',  ,'', , ,''),
-- ('','','','',  ,'', , ,''),
-- ('','','','',  ,'', , ,'');


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

-- INSERT INTO (`Sales_No`, `Date`, `Nozzel_No`, `Starting_Reading`, `Ending_Reading`, `Total_Sales`, `Sales_Amount`, `Petrolpump_No`) VALUES
-- ('','', , , , , ,''),
-- ('','', , , , , ,''),
-- ('','', , , , , ,''),
-- ('','', , , , , ,''),
-- ('','', , , , , ,'');


CREATE TABLE IF NOT EXISTS `Owns`(
   `Registration_No` varchar(10) NOT NULL,
   `Owner_Name` varchar(20) NOT NULL,
   PRIMARY KEY(`Registration_No`, `Owner_Name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- INSERT INTO (`Registration_No`,`Owner_Name`) VALUES
-- ('',''),
-- ('',''),
-- ('',''),
-- ('',''),
-- ('',''),
-- ('',''),
-- ('','');


CREATE TABLE IF NOT EXISTS `Contacts`(
   `Employee_ID` varchar(10) NOT NULL,
   `Contact_NO` char(10) NOT NULL,
   PRIMARY KEY(`Employee_ID`, `Contact_NO`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- INSERT INTO (`Employee_ID`, `Contact_NO`) VALUES
-- ('',''),
-- ('',''),
-- ('',''),
-- ('',''),
-- ('',''),
-- ('','');


CREATE TABLE IF NOT EXISTS `Serves`(
   `Employee_ID` varchar(10) NOT NULL,
   `Customer_Code` varchar(10) NOT NULL,
   PRIMARY KEY(`Employee_ID`, `Customer_Code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- INSERT INTO (`Employee_ID`, `Customer_Code`) VALUES
-- ('',''),
-- ('',''),
-- ('',''),
-- ('',''),
-- ('','');

CREATE TABLE IF NOT EXISTS `Sales_Manage`(
   `Employee_ID` varchar(10) NOT NULL,
   `Sales_No` varchar(10) NOT NULL,
   `Date` date NOT NULL, 
   PRIMARY KEY(`Employee_ID`, `Sales_No`, `Date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- INSERT INTO (`Employee_ID`, `Sales_No`, `Date`) VALUES
-- ('','',''),
-- ('','',''),
-- ('','',''),
-- ('','',''),
-- ('','',''),
-- ('','','');

COMMIT;