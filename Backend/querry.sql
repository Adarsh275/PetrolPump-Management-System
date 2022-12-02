



-- Join 

-- 1 --

SELECT PetrolPump.Registration_No FROM PetrolPump INNER JOIN Employee ON PetrolPump.Registration_No = Employee.Petrolpump_No;

-- 2 --

SELECT Petrolpump.Registration_No FROM Petrolpump left join Employee on Petrolpump.Registration_No = Employee.Petrolpump_No WHERE Employee.Petrolpump_No is NULL;

-- 3 --

 SELECT PetrolPump.Registration_No FROM PetrolPump LEFT JOIN Employee ON PetrolPump.Registration_No = Employee.Petrolpump_No;

-- 4 --

SELECT Invoice.Invoice_No ,Invoice.Date ,Invoice.Payment_Type, Customer.C_Name , Customer.Phone_No FROM Invoice RIGHT OUTER JOIN Customer ON Customer.Customer_Code = Invoice.Customer_Code; 

--  Aggriate Functions 


-- 1 --
select avg(Age) from Customer where Gender='M';

-- 2 --

SELECT Emp_Name,TIMESTAMPDIFF(YEAR, DOB, CURDATE()) AS age FROM Employee;

--  3 --

SELECT * , max(Total_Price) FROM Invoice ;

-- 4 --

SELECT Sales_No, Sales_Amount, Petrolpump_No, max(Sales_Amount) FROM Sales WHERE DATE='2022-11-20';

--  SET Operations

--  1 --
 SELECT Owner_Name from Owners as Names UNION SELECT EMP_Name from Employee ;

-- 2 --
SELECT Registration_No from Petrolpump INTERSECT SELECT Petrolpump_No from Employee;

-- 3 --

  SELECT Petrolpump_Name FROM Petrolpump where Registration_No IN(SELECT Petrolpump.Registration_No FROM Petrolpump left join Employee on Petrolpump.Registration_No = Employee.Petrolpump_No WHERE Employee.Petrolpump_No is NULL);

--  4 --
SELECT  C_Name from Customer UNION SELECT Owner_Name from Owners;

--  Trigger --
DELIMITER $$
CREATE TRIGGER salary_check 
BEFORE UPDATE
ON Employee FOR EACH ROW
BEGIN
declare WAGE int(7);
declare error_msg varchar(225);
set error_msg = ("Error: Insufficient Salary For Living");
set WAGE = new.WAGE;
if salary < 300000 then
signal sqlstate '45000'
set MESSAGE_TEXT = error_msg;
end if;
END $$

DELIMITER ;

--  to drop trigger 
drop trigger salary_check;

-- text 
UPDATE Employee SET Salary = 15000 WHERE Email_ID = "sfeer334";




-- Function 
DELIMITER $$
CREATE FUNCTION `TOTAL_AMOUNT`(`TID` VARCHAR(10)) RETURNS float
    DETERMINISTIC
BEGIN
	
    DECLARE BILL FLOAT;
    DECLARE RATE FLOAT;
    DECLARE VOL FLOAT;
    
    SET RATE = (SELECT FUEL_PRICE FROM TANKER WHERE TANKER_ID = TID);
    SET VOL = (SELECT FUEL_AMOUNT FROM TANKER WHERE TANKER_ID = TID);
    
    SET BILL = RATE * VOL;
    
    RETURN BILL;
    
END$$
DELIMITER ;

-- TO EXECUTE

SET @p0='BR6872'; SELECT `TOTAL_AMOUNT`(@p0) AS `TOTAL_AMOUNT`;

--  Procedure

DELIMITER $$
create procedure p()
begin
SELECT PetrolPump.Registration_No FROM PetrolPump INNER JOIN Employee ON PetrolPump.Registration_No = Employee.Petrolpump_No;
END $$

--  Modification --

DELIMITER $$
create procedure Modify()
begin
select total_sales, sales_amount from sales where month(date) = 11;
END $$