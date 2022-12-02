SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";

ALTER TABLE `Tanker`
   ADD KEY `Petrolpump_No` (`Petrolpump_No`);

ALTER TABLE `Employee`
   ADD KEY `Petrolpump_No` (`Petrolpump_No`),
   ADD KEY `Manager_ID` (`Manager_ID`);

ALTER TABLE `Invoice`
   ADD KEY `Date` (`Date`),
   ADD KEY  `Customer_Code` (`Customer_Code`);

ALTER TABLE `Sales`
   ADD KEY `Petrolpump_No` (`Petrolpump_No`);

ALTER TABLE `Owns`
   ADD CONSTRAINT `Owns_ibfk_1` FOREIGN KEY (`Registration_No`) REFERENCES `PetrolPump` (`Registration_No`),
   ADD CONSTRAINT `Owns_ibfk_2` FOREIGN KEY (`Owner_Name`) REFERENCES `Owners` (`Owner_Name`);


ALTER TABLE `Tanker`
   ADD CONSTRAINT `Tanker_ibfk_1` FOREIGN KEY (`Petrolpump_No`) REFERENCES `PetrolPump` (`Registration_No`);

ALTER TABLE `Employee`
   ADD CONSTRAINT `Employee_ibfk_1` FOREIGN KEY (`Petrolpump_No`) REFERENCES `PetrolPump` (`Registration_No`),
   ADD CONSTRAINT `Employee_ibfk_2` FOREIGN KEY (`Manager_ID`) REFERENCES `Employee` (`Employee_ID`);

ALTER TABLE `Invoice`
   ADD CONSTRAINT `Invoice_ibfk_1` FOREIGN KEY (`Date`) REFERENCES `Sales` (`Date`),
   ADD CONSTRAINT `Invoice_ibfk_2` FOREIGN KEY (`Customer_Code`) REFERENCES `Customer` (`Customer_Code`);

ALTER TABLE `Sales`
   ADD CONSTRAINT `Sales_ibfk_1` FOREIGN KEY (`Petrolpump_No`) REFERENCES `PetrolPump` (`Registration_No`);

ALTER TABLE `Contacts`
   ADD CONSTRAINT `Contacts_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`);

ALTER TABLE `Serves`
   ADD CONSTRAINT `Serves_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`),
   ADD CONSTRAINT `Serves_ibfk_2` FOREIGN KEY (`Customer_Code`) REFERENCES `Customer` (`Customer_Code`);

ALTER TABLE `Sales_Manage`
   ADD CONSTRAINT `Sales_Manage_ibfk_1` FOREIGN KEY (`Employee_ID`) REFERENCES `Employee` (`Employee_ID`),
   ADD CONSTRAINT `Sales_Manage_ibfk_2` FOREIGN KEY (`Sales_No`) REFERENCES `Sales` (`Sales_No`),
   ADD CONSTRAINT `Sales_Manage_ibfk_3` FOREIGN KEY (`Date`) REFERENCES `Sales` (`Date`);

COMMIT;