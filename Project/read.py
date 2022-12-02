import pandas as pd
import streamlit as st
from database import *


def read_for_Petrolpump():
    result = view_all_Petrolpump_data()
    df = pd.DataFrame(result, columns=['Registration_No','Petrolpump_Name','Company_Name','Opening_Year','State','City'])
    with st.expander("View all Petrolpumps"):
        st.dataframe(df)

def read_for_Owners():
    result = view_all_Owners_data()
    df = pd.DataFrame(result, columns=['Owner_Name', 'Contact_NO', 'DOB', 'Gender', 'Address', 'Partnership'])
    with st.expander("View all Owners"):
        st.dataframe(df)

def read_for_Employee():
    result = view_all_Employee_data()
    df = pd.DataFrame(result, columns=['Employee_ID', 'Emp_Name', 'Emp_Gender', 'Designation', 'DOB', 'Salary',  'Emp_Address', 'Email_ID' , 'Petrolpump_No', 'Manager_ID'])
    with st.expander("View all Employees"):
        st.dataframe(df)

def read_for_Customer():
    result = view_all_Customer_data()
    df = pd.DataFrame(result, columns=['Customer_Code', 'C_Name' , 'Phone_No' , 'Email_ID' , 'Gender', 'City' , 'Age'])
    with st.expander("View all Customers"):
        st.dataframe(df)

def read_for_Invoice():
    result = view_all_Invoice_data()
    df = pd.DataFrame(result, columns=['Invoice_No' , 'Date','Payment_Type', 'Fuel_Amount' , 'Fuel_Type' , 'Discount' , 'Total_Price' , 'Customer_Code'])
    with st.expander("View all Invoices"):
        st.dataframe(df)

def read_for_Tanker():
    result = view_all_Tanker_data()
    df = pd.DataFrame(result, columns=['Tanker_ID', 'Capacity', 'pressure', 'Fuel_ID' , 'Fuel_Amount', 'Fuel_Name' , 'Fuel_Price' , 'Petrolpump_No'])
    with st.expander("View all Tankers"):
        st.dataframe(df)
