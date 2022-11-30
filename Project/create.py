import streamlit as st
from database import *


def create_for_Petrolpump():
    with st.container():
        Registration_No = st.text_input("Registration_No:")
        Petrolpump_Name = st.text_input("Petrolpump_Name:")
        Company_Name = st.text_input("Company_Name:")
        Opening_Year = st.number_input("Opening_Year:")
        State = st.text_input("State:")
        City = st.text_input("City:")
    
    if st.button("Add Petrolpump Details"):
        add_Petrolpump_data(Registration_No,Petrolpump_Name,Company_Name,Opening_Year,State,City)
        st.success("Successfully added Petrolpump details: {}".format(Registration_No))


def create_for_Owners():
    with st.container():
        Owner_Name = st.text_input("Owner_Name:")
        Contact_NO = st.text_input("Contact_NO:")
        DOB = st.date_input("DOB:")
        Gender = st.text_input("Gender:")
        Address = st.text_input("Enter Address")
        Partnership = st.number_input("Your Partership")
        
    if st.button("Add Owners Details"):
        add_Owners_data(Owner_Name, Contact_NO, DOB, Gender, Address, Partnership)
        st.success("Successfully added Owners details: {}".format(Owner_Name))


def create_for_Employee():
    with st.container():
        Employee_ID = st.text_input("Employee_ID")
        Emp_Name = st.text_input("Emp_Name:")
        Emp_Gender = st.text_input("Emp_Gender:")
        Designation = st.text_input(" Designation:")
        DOB= st.date_input("DOB:")
        Salary = st.number_input("Salary:")
        Emp_Address=st.text_input("Emp_Address:")
        Email_ID=st.text_input("Email_ID:")
        Petrolpump_No=st.text_input("Petrolpump_No:")
        Manager_ID=st.text_input("Manager_ID:")

    if st.button("Add Employee Details"):
        add_Employee_data(Employee_ID, Emp_Name,  Emp_Gender,   Designation,  DOB, Salary,  Emp_Address, Email_ID , Petrolpump_No, Manager_ID)
        st.success("Successfully added Employee details: {}".format(Employee_ID))


def create_for_Customer():
    with st.container():
        Customer_Code = st.text_input("Customer_Code")
        C_Name = st.text_input("C_Name:")
        Phone_No = st.text_input("Phone_No:")
        Email_ID=st.text_input("Email_ID")
        Gender = st.text_input("Gender:")
        City = st.text_input("City:")
        Age = st.number_input("Age")
    
    if st.button("Add Customer Details"):
        add_Customer_data(Customer_Code , C_Name , Phone_No  , Email_ID , Gender,  City , Age)
        st.success("Successfully added Customer details: {}".format(Customer_Code))



def create_for_Invoice():
    with st.container():
        Invoice_No=st.text_input(" Invoice_No:")
        Date=st.date_input("Date:")
        Payment_Type=st.text_input("Payment_Type:")
        Fuel_Amount=st.number_input("Fuel_Amount:")
        Fuel_Type=st.text_input("Fuel_Type:")
        Discount=st.number_input("Discount:")
        Total_Price=st.number_input("Total_Price:")
        Customer_Code=st.text_input("Customer_Code:")

        
    if st.button("Add Invoice Details"):
        add_Invoice_data(Invoice_No , Date , Payment_Type , Fuel_Amount , Fuel_Type , Discount  , Total_Price , Customer_Code)
        st.success("Successfully added Invoice details: {}".format(Invoice_No))

def create_for_Tanker():
    with st.container():
        Tanker_ID = st.text_input("Tanker_ID:")
        Capacity = st.number_input("Capacity:")
        pressure = st.number_input("pressure:")
        Fuel_ID = st.text_input("Fuel_ID")
        Fuel_Amount = st.number_input("Fuel_Amount")
        Fuel_Name= st.text_input("Fuel_Name:")
        Fuel_Price= st.number_input("Fuel_Price:")
        Petrolpump_No=st.text_input("Petrolpump_No:")

    if st.button("Add Tanker Details"):
        add_Tanker_data(Tanker_ID  , Capacity,  pressure,  Fuel_ID , Fuel_Amount, Fuel_Name , Fuel_Price , Petrolpump_No)
        st.success("Successfully added Tanker details: {}".format(Tanker_ID))