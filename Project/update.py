import pandas as pd
import streamlit as st
from database import *


def update_for_Petrolpump():
    result = view_all_Petrolpump_data()
    df = pd.DataFrame(result, columns=['Registration_No','Petrolpump_Name','Company_Name','Opening_Year','State','City'])
    with st.expander("Current Petrolpump details"):
        st.dataframe(df)
    list_of_Petrolpump = [i[0] for i in view_only_Registration_No()]
    
    selected_Petrolpump = st.selectbox("Petrolpumps to Edit", list_of_Petrolpump)
    
    selected_result = get_all_info_Petrolpump(selected_Petrolpump)
   
    if selected_result:
        Registration_No = selected_result[0][0]
        Petrolpump_Name = selected_result[0][1]
        Company_Name = selected_result[0][2]
        Opening_Year = selected_result[0][3]
        State = selected_result[0][4]
        City = selected_result[0][5]
        with st.container():
            new_Petrolpump_Name = st.text_input("Petrolpump_Name:", Petrolpump_Name)
            new_Company_Name = st.text_input("Company_Name:", Company_Name)
            new_Opening_Year = st.number_input("Opening_Year",Opening_Year)
            new_State = st.text_input("State",State)
            new_City = st.text_input("City",City)
        
        if st.button("Update Petrolpump"):
            edit_Petrolpump_data(new_Petrolpump_Name, new_Company_Name, new_Opening_Year, new_State, new_City, Registration_No)
            st.success("Successfully updated")

    result2 = view_all_Petrolpump_data()
    df2 = pd.DataFrame(result2, columns=['Registration_No','Petrolpump_Name','Company_Name','Opening_Year','State','City'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_for_Owners():
    result = view_all_Owners_data()
    
    df = pd.DataFrame(result, columns=['Owner_Name', 'Contact_NO', 'DOB', 'Gender', 'Address', 'Partnership'])
    with st.expander("Current Owners details"):
        st.dataframe(df)
    list_of_Owners = [i[0] for i in view_only_Owner_Name()]
   
    selected_Owners = st.selectbox("Owners to Edit", list_of_Owners)
   
    selected_result = get_all_info_Owners(selected_Owners)
    
    if selected_result:
        Owner_Name = selected_result[0][0]
        Contact_NO = selected_result[0][1]
        DOB = selected_result[0][2]
        Gender = selected_result[0][3]
        Address = selected_result[0][4]
        Partnership = selected_result[0][5]
        with st.container():
            new_Contact_NO = st.text_input("Contact_NO:",Contact_NO )
            new_DOB = st.date_input("DOB:",DOB)
            new_Gender = st.text_input("Gender:",Gender )
            new_Address = st.text_input("Address:", Address)
            new_Partnership = st.number_input("Partnership:", Partnership)
        if st.button("Update Owners"):
            edit_Owners_data(new_Contact_NO, new_DOB, new_Gender,new_Address, new_Partnership, Owner_Name)
            st.success("Successfully updated")

    result2 = view_all_Owners_data()
    df2 = pd.DataFrame(result2, columns=['Owner_Name', 'Contact_NO', 'DOB', 'Gender', 'Address', 'Partnership'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_for_Employee():
    result = view_all_Employee_data()
   
    df = pd.DataFrame(result, columns=['Employee_ID', 'Emp_Name', 'Emp_Gender', 'Designation','DOB', 'Salary', 'Emp_Address', 'Email_ID' , 'Petrolpump_No', 'Manager_ID'])
    with st.expander("Current Employee details"):
        st.dataframe(df)
    list_of_Employee = [i[0] for i in view_only_Employee_ID()]
   
    selected_Employee = st.selectbox("Employee to Edit", list_of_Employee)
    
    selected_result = get_all_info_Employee(selected_Employee)
    
    if selected_result:
        Employee_ID = selected_result[0][0]
        Emp_Name = selected_result[0][1]
        Emp_Gender = selected_result[0][2]
        Designation = selected_result[0][3]
        DOB = selected_result[0][4]
        Salary = selected_result[0][5]
        Emp_Address = selected_result[0][6]
        Email_ID = selected_result[0][7]
        Petrolpump_No = selected_result[0][8]
        Manager_ID = selected_result[0][9]
        with st.container():
            new_Emp_Name= st.text_input("Emp_Name:", Emp_Name)
            new_Emp_Gender= st.text_input("Emp_Gender:", Emp_Gender)
            new_Designation= st.text_input("Designation:", Designation)
            new_DOB= st.date_input("DOB:", DOB)
            new_Salary= st.number_input("Salary:", Salary)
            new_Emp_Address= st.text_input("Emp_Address:", Emp_Address)
            new_Email_ID= st.text_input("Email_ID:", Email_ID)
            new_Petrolpump_No= st.text_input("Petrolpump_No:", Petrolpump_No)
            new_Manager_ID= st.text_input("Manager_ID:", Manager_ID)

        if st.button("Update Employee"):
            try:
                edit_Employee_data(new_Emp_Name, new_Emp_Gender,  new_Designation, new_DOB, new_Salary,  new_Emp_Address, new_Email_ID , new_Petrolpump_No, new_Manager_ID, Employee_ID)
                st.success("Successfully updated")
            except Exception as err:
                st.exception(err)

    result2 = view_all_Employee_data()
    df2 = pd.DataFrame(result2, columns=['Employee_ID', 'Emp_Name', 'Emp_Gender', 'Designation','DOB', 'Salary', 'Emp_Address', 'Email_ID' , 'Petrolpump_No', 'Manager_ID'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_for_Customer():
    result = view_all_Customer_data()
    df = pd.DataFrame(result, columns=['Customer_Code', 'C_Name' , 'Phone_No', 'Email_ID' , 'Gender', 'City' , 'Age'])
    with st.expander("Current Customer details"):
        st.dataframe(df)
    list_of_Customer = [i[0] for i in view_only_Customer_Code()]
    selected_Customer = st.selectbox("Customer to Edit", list_of_Customer)
    selected_result = get_all_info_Customer(selected_Customer)
    if selected_result:
        Customer_Code = selected_result[0][0]
        C_Name = selected_result[0][1]
        Phone_No = selected_result[0][2]
        Email_ID = selected_result[0][3]
        Gender = selected_result[0][4]
        City = selected_result[0][5]
        Age = selected_result[0][6]

        with st.container():
            new_C_Name = st.text_input("customer name:", C_Name)
            new_Phone_No = st.text_input("Phone_No:", Phone_No)
            new_Email_ID = st.text_input("Email_ID:", Email_ID)
            new_Gender = st.text_input("Gender:", Gender)
            new_City = st.text_input("City:", City)
            new_Age = st.number_input("Age:", Age)
        if st.button("Update Customer"):
            edit_Customer_data(new_C_Name , new_Phone_No  , new_Email_ID , new_Gender,  new_City , new_Age, Customer_Code)
            st.success("Successfully updated")

    result2 = view_all_Customer_data()
    df2 = pd.DataFrame(result2, columns=['Customer_Code', 'C_Name' , 'Phone_No', 'Email_ID' , 'Gender', 'City' , 'Age'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_for_Invoice():
    result = view_all_Invoice_data()
    df = pd.DataFrame(result, columns=['Invoice_No', 'Date' , 'Payment_Type', 'Fuel_Amount', 'Fuel_Type', 'Discount', 'Total_Price', 'Customer_Code'])
    with st.expander("Current Invoice details"):
        st.dataframe(df)
    list_of_Invoice = [i[0] for i in view_only_Invoice_No()]
    selected_Invoice = st.selectbox("Invoice to Edit", list_of_Invoice)
    selected_result = get_all_info_Invoice(selected_Invoice)
    if selected_result:
        Invoice_No = selected_result[0][0]
        Date = selected_result[0][1]
        Payment_Type = selected_result[0][2]
        Fuel_Amount = selected_result[0][3]
        Fuel_Type = selected_result[0][4]
        Discount = selected_result[0][5]
        Total_Price = selected_result[0][6]
        Customer_Code = selected_result[0][7]
        with st.container():
            new_Date = st.date_input("Date:", Date)
            new_Payment_Type = st.text_input("Payment_Type:", Payment_Type)
            new_Fuel_Amount = st.number_input("Fuel_Amount:", Fuel_Amount)
            new_Fuel_Type = st.text_input("Fuel_Type:", Fuel_Type)
            new_Discount = st.number_input("Discount:", Discount)
            new_Total_Price = st.number_input("Total_Price:", Total_Price)
            new_Customer_Code = st.text_input("Customer_Code:", Customer_Code)

        if st.button("Update Invoice"):
            edit_Invoice_data(new_Date , new_Payment_Type , new_Fuel_Amount , new_Fuel_Type, new_Discount, new_Total_Price , new_Customer_Code, Invoice_No)
            st.success("Successfully updated")

    result2 = view_all_Invoice_data()
    df2 = pd.DataFrame(result2, columns=['Invoice_No' , 'Date', 'Payment_Type' , 'Fuel_Amount' , 'Fuel_Type' , 'Discount' , 'Total_Price' , 'Customer_Code'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_for_Tanker():
    result = view_all_Tanker_data()
    df = pd.DataFrame(result, columns=['Tanker_ID', 'Capacity', 'pressure', 'Fuel_ID' , 'Fuel_Amount', 'Fuel_Name' , 'Fuel_Price' , 'Petrolpump_No'])
    with st.expander("Current Tanker details"):
        st.dataframe(df)
    list_of_Tankers = [i[0] for i in view_only_Tanker_ID()]
    selected_Tanker = st.selectbox("Tankers to Edit", list_of_Tankers)
    selected_result = get_all_info_Tanker(selected_Tanker)
    
    if selected_result:
        Tanker_ID = selected_result[0][0]
        Capacity = selected_result[0][1]
        pressure = selected_result[0][2]
        Fuel_ID = selected_result[0][3]
        Fuel_Amount = selected_result[0][4]
        Fuel_Name = selected_result[0][5]
        Fuel_Price = selected_result[0][6]
        Petrolpump_No = selected_result[0][7]
        
        with st.container():
            new_Capacity = st.text_input("Tanker Capacity:", Capacity)
            new_pressure = st.number_input("pressure:", pressure)
            new_Fuel_ID = st.text_input("Fuel_ID:", Fuel_ID)
            new_Fuel_Amount = st.number_input("Fuel_Amount:", Fuel_Amount)
            new_Fuel_Name = st.text_input("Fuel_Name:", Fuel_Name)
            new_Fuel_Price = st.number_input("Fuel_Price:", Fuel_Price)
            new_Petrolpump_No = st.text_input("Petrolpump No:", Petrolpump_No)
        if st.button("Update Tankers"):
            edit_Tanker_data(new_Capacity,  new_pressure,  new_Fuel_ID , new_Fuel_Amount, new_Fuel_Name , new_Fuel_Price ,new_Petrolpump_No, Tanker_ID)
            st.success("Successfully updated")

    result2 = view_all_Tanker_data()
    df2 = pd.DataFrame(result2, columns=['Tanker_ID', 'Capacity', 'pressure', 'Fuel_ID' , 'Fuel_Amount', 'Fuel_Name' , 'Fuel_Price' , 'Petrolpump_No'])
    with st.expander("Updated data"):
        st.dataframe(df2)
