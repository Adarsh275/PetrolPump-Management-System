import mysql.connector 
mydb = mysql.connector.connect(
   host="localhost",
   user="root", 
   password="", 
   database="Petrolpump_Management"
)

c = mydb.cursor()

def create_table(): 
   c.execute('CREATE TABLE IF NOT EXISTS Petrolpump (Registration_No varchar(10) NOT NULL, Petrolpump_Name varchar(50) NOT NULL,  Company_Name varchar(30) DEFAULT NULL, Opening_Year int(5) DEFAULT NULL, State varchar(30) DEFAULT NULL,City varchar(40) NOT NULL, PRIMARY KEY(Registration_No))')
   c.execute('CREATE TABLE IF NOT EXISTS Owners( Owner_Name varchar(20) NOT NULL, Contact_NO char(10) NOT NULL, DOB date DEFAULT NULL, Gender char DEFAULT NULL, Address varchar(255) DEFAULT NULL, Partnership int(5) NOT NULL, PRIMARY KEY(Owner_Name))')
   c.execute('CREATE TABLE IF NOT EXISTS Employee( Employee_ID varchar(10) NOT NULL, Emp_Name varchar(30) NOT NULL,  Emp_Gender char DEFAULT NULL,  Designation varchar(10) DEFAULT NULL, DOB date DEFAULT NULL,  Salary int(20) DEFAULT NULL, Emp_Address varchar(255) NOT NULL, Email_ID varchar(100) NOT NULL, Petrolpump_No varchar(10) DEFAULT NULL, Manager_ID varchar(10) DEFAULT NULL, PRIMARY KEY(Employee_ID)) ')
   c.execute('CREATE TABLE IF NOT EXISTS Customer( Customer_Code varchar(10) NOT NULL, C_Name varchar(30) NOT NULL, Phone_No char(10) DEFAULT NULL,  Email_ID varchar(100) DEFAULT NULL, Gender char DEFAULT NULL,  City varchar(50) DEFAULT NULL, Age int(3) DEFAULT NULL, PRIMARY KEY(Customer_Code))')
   c.execute('CREATE TABLE IF NOT EXISTS Invoice( Invoice_No varchar(10) NOT NULL, Date date NOT NULL, Payment_Type varchar(20) NOT NULL, Fuel_Amount float(15) DEFAULT NULL, Fuel_Type varchar(15) DEFAULT NULL, Discount int(5) DEFAULT NULL, Total_Price float(10) NOT NULL, Customer_Code varchar(10) NULL, PRIMARY KEY(Invoice_No))')
   c.execute('CREATE TABLE IF NOT EXISTS Tanker( Tanker_ID varchar(10) NOT NULL, Capacity float(10) DEFAULT NULL,  pressure float(10) DEFAULT NULL,  Fuel_ID varchar(10) NOT NULL, Fuel_Amount float(15) DEFAULT NULL, Fuel_Name varchar(20) DEFAULT NULL, Fuel_Price float(5) NOT NULL, Petrolpump_No varchar(10) DEFAULT NULL, PRIMARY KEY(Tanker_ID))')


def add_Petrolpump_data(Registration_No,Petrolpump_Name,Company_Name,Opening_Year,State,City):
    c.execute('insert into Petrolpump (Registration_No,Petrolpump_Name,Company_Name,Opening_Year,State,City) values (%s,%s,%s,%s,%s,%s)',(Registration_No,Petrolpump_Name,Company_Name,Opening_Year,State,City) )
    mydb.commit()

def add_Owners_data(Owner_Name, Contact_NO, DOB, Gender, Address, Partnership):
    c.execute('INSERT INTO Owners  (Owner_Name, Contact_NO, DOB, Gender, Address, Partnership) VALUES (%s,%s,%s,%s,%s,%s)',(Owner_Name, Contact_NO, DOB, Gender, Address, Partnership))
    mydb.commit()
    
def add_Employee_data(Employee_ID, Emp_Name,  Emp_Gender,   Designation,  DOB, Salary,  Emp_Address, Email_ID , Petrolpump_No, Manager_ID):
    c.execute('insert into Employee  (Employee_ID, Emp_Name,  Emp_Gender,   Designation,  DOB, Salary,  Emp_Address, Email_ID , Petrolpump_No, Manager_ID) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(Employee_ID, Emp_Name,  Emp_Gender,   Designation,  DOB, Salary,  Emp_Address, Email_ID , Petrolpump_No, Manager_ID))
    mydb.commit()

def add_Customer_data(Customer_Code, C_Name , Phone_No  , Email_ID , Gender,  City , Age):
    c.execute('INSERT INTO Customer  (Customer_Code , C_Name , Phone_No  , Email_ID , Gender,  City , Age) VALUES (%s,%s,%s,%s,%s,%s,%s)',(Customer_Code , C_Name , Phone_No  , Email_ID , Gender,  City , Age))
    mydb.commit() 

def add_Invoice_data(Invoice_No , Date  , Payment_Type , Fuel_Amount , Fuel_Type , Discount  , Total_Price , Customer_Code):
    c.execute('INSERT INTO Invoice  (Invoice_No , Date  , Payment_Type , Fuel_Amount , Fuel_Type , Discount  , Total_Price , Customer_Code) Values (%s,%s,%s,%s,%s,%s,%s,%s)',(Invoice_No , Date  , Payment_Type , Fuel_Amount , Fuel_Type , Discount  , Total_Price , Customer_Code))
    mydb.commit()

def add_Tanker_data(Tanker_ID  , Capacity,  pressure,  Fuel_ID , Fuel_Amount, Fuel_Name , Fuel_Price , Petrolpump_No):
    c.execute('INSERT INTO Tanker  (Tanker_ID  , Capacity,  pressure,  Fuel_ID , Fuel_Amount, Fuel_Name , Fuel_Price , Petrolpump_No) Values (%s,%s,%s,%s,%s,%s,%s,%s)',(Tanker_ID  , Capacity,  pressure,  Fuel_ID , Fuel_Amount, Fuel_Name , Fuel_Price , Petrolpump_No))
    mydb.commit()


def view_all_Petrolpump_data():
    c.execute('SELECT * FROM Petrolpump')
    data = c.fetchall()
    return data

def view_all_Owners_data():
    c.execute('SELECT * FROM Owners')
    data = c.fetchall()
    return data

def view_all_Employee_data():
    c.execute('SELECT * FROM Employee')
    data = c.fetchall()
    return data

def view_all_Customer_data():
    c.execute('SELECT * FROM Customer')
    data = c.fetchall()
    return data

def view_all_Invoice_data():
    c.execute('SELECT * FROM Invoice')
    data = c.fetchall()
    return data

def view_all_Tanker_data():
    c.execute('SELECT * FROM Tanker')
    data = c.fetchall()
    return data


def view_only_Registration_No():
    c.execute("select Registration_No from Petrolpump")
    data = c.fetchall()
    return data

def view_only_Owner_Name():
    c.execute("select Owner_Name from Owners")
    data = c.fetchall()
    return data

def view_only_Employee_ID():
    c.execute("select Employee_ID from Employee")
    data = c.fetchall()
    return data

def view_only_Customer_Code():  
    c.execute("select Customer_Code from Customer")
    data = c.fetchall()
    return data

def view_only_Invoice_No():
    c.execute("select Invoice_No from Invoice")
    data = c.fetchall()
    return data

def view_only_Tanker_ID():
    c.execute("select Tanker_ID from Tanker")
    data = c.fetchall()
    return data


def get_all_info_Petrolpump(selected_Petrolpump):
    c.execute('select * from Petrolpump where Registration_No="{}"'.format(selected_Petrolpump))
    data = c.fetchall()
    return data

def get_all_info_Owners(selected_Owners): 
    c.execute('select * from  Owners where Owner_Name="{}"'.format(selected_Owners))
    data = c.fetchall()
    return data

def get_all_info_Employee(selected_Employee):
    c.execute('select * from Employee where Employee_ID="{}"'.format(selected_Employee))
    data = c.fetchall()
    return data

def get_all_info_Customer(selected_Customer):
    c.execute('select * from Customer where Customer_Code="{}"'.format(selected_Customer))
    data = c.fetchall()
    return data

def get_all_info_Invoice(selected_Invoice):
    c.execute('select * from Invoice where Invoice_No="{}"'.format(selected_Invoice))
    data = c.fetchall()
    return data

def get_all_info_Tanker(selected_Tanker):
    c.execute('select * from Tanker where Tanker_ID="{}"'.format(selected_Tanker))
    data = c.fetchall()
    return data


def edit_Petrolpump_data(new_Petrolpump_Name, new_Company_Name, new_Opening_Year, new_State, new_City, Registration_No):
    c.execute("update Petrolpump set Petrolpump_Name=%s,Company_Name=%s,Opening_Year=%s,State=%s,City=%s where Registration_No=%s", (new_Petrolpump_Name, new_Company_Name, new_Opening_Year, new_State, new_City, Registration_No))
    mydb.commit()
    data = view_all_Petrolpump_data()
    return data

def edit_Owners_data(new_Contact_NO, new_DOB, new_Gender,new_Address, new_Partnership, Owner_Name):
    c.execute("update Owners set Contact_NO=%s, DOB=%s, Gender=%s, Address=%s, Partnership=%s where Owner_Name=%s", (new_Contact_NO, new_DOB, new_Gender,new_Address, new_Partnership, Owner_Name))
    mydb.commit()
    data = view_all_Owners_data()
    return data

def edit_Employee_data(new_Emp_Name, new_Emp_Gender,  new_Designation, new_DOB,new_Salary,  new_Emp_Address, new_Email_ID , new_Petrolpump_No, new_Manager_ID, Employee_ID):
    c.execute("update Employee set Emp_Name=%s,  Emp_Gender=%s,   Designation=%s,  DOB=%s, Salary=%s,  Emp_Address=%s, Email_ID=%s, Petrolpump_No=%s, Manager_ID=%s where Employee_ID=%s", (new_Emp_Name, new_Emp_Gender, new_Designation, new_DOB,new_Salary, new_Emp_Address, new_Email_ID ,new_Petrolpump_No, new_Manager_ID, Employee_ID))
    mydb.commit()
    data = view_all_Employee_data()
    return data

def edit_Customer_data(new_C_Name , new_Phone_No  , new_Email_ID , new_Gender,  new_City , new_Age, Customer_Code):
    c.execute("update Customer set C_Name=%s , Phone_No=%s , Email_ID=%s , Gender=%s,  City=%s , Age=%s where Customer_Code=%s", (new_C_Name , new_Phone_No , new_Email_ID , new_Gender, new_City , new_Age, Customer_Code))
    mydb.commit()
    data = view_all_Customer_data()
    return data

def edit_Invoice_data( new_Date , new_Payment_Type , new_Fuel_Amount , new_Fuel_Type , new_Discount  ,new_Total_Price , new_Customer_Code, Invoice_No):
    c.execute("update Invoice set Date=%s ,  Payment_Type=%s , Fuel_Amount=%s , Fuel_Type=%s , Discount=%s  , Total_Price=%s , Customer_Code=%s where Invoice_No=%s", (new_Date , new_Payment_Type , new_Fuel_Amount , new_Fuel_Type , new_Discount  ,new_Total_Price , new_Customer_Code, Invoice_No))
    mydb.commit()
    data = view_all_Invoice_data()
    return data

def edit_Tanker_data(new_Capacity,  new_pressure,  new_Fuel_ID , new_Fuel_Amount, new_Fuel_Name , new_Fuel_Price ,new_Petrolpump_No, Tanker_ID):
    c.execute("update Tanker set Capacity=%s,  pressure=%s,  Fuel_ID=%s, Fuel_Amount=%s, Fuel_Name=%s, Fuel_Price=%s, Petrolpump_No=%s where Tanker_ID=%s", (new_Capacity,  new_pressure,  new_Fuel_ID , new_Fuel_Amount, new_Fuel_Name , new_Fuel_Price ,new_Petrolpump_No, Tanker_ID))
    mydb.commit()
    data = view_all_Tanker_data()
    return data


def delete_data_Petrolpump(selected_Petrolpump):
    c.execute('DELETE FROM Petrolpump WHERE Registration_No="{}"'.format(selected_Petrolpump))
    mydb.commit()

def delete_data_Owners(selected_Owners):
    c.execute('DELETE FROM Owners WHERE Owner_Name="{}"'.format(selected_Owners))
    mydb.commit()

def delete_data_Employee(selected_Employee):
    c.execute('DELETE FROM Employee WHERE Employee_ID="{}"'.format(selected_Employee))
    mydb.commit()

def delete_data_Customer(selected_Customer):
    c.execute('DELETE FROM Customer WHERE Customer_Code="{}"'.format(selected_Customer))
    mydb.commit()

def delete_data_Invoice(selected_Invoice):
    c.execute('DELETE FROM Invoice WHERE Invoice_No="{}"'.format(selected_Invoice))
    mydb.commit()

def delete_data_Tanker(selected_Tanker):
    c.execute('DELETE FROM Tanker WHERE Tanker_ID="{}"'.format(selected_Tanker))
    mydb.commit()


def TOTAL_Amount(tanker_id):
    query = "SET @p0='{}';".format(tanker_id)
    c.execute(query)
    print(query)

    query = "SELECT `TOTAL_AMOUNT`(@p0) AS `TOTAL_AMOUNT`;"
    c.execute(query)
    print(query)
    result = c.fetchall()
    print(result)
    return result