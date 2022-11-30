
import streamlit as st
import mysql.connector
import pandas as pd

from create import *
from database import *
from delete import *
from read import *
from update import *

def main():
   st.title("Petrol Pump Management System")
   menu = ["PetrolPump", "Owners", "Employee", "Customer","Invoice", "Tanker","Custom Query"]
   choice = st.sidebar.selectbox("Menu", menu)

   create_table()
   
   if choice == "PetrolPump":
      menu = ["Add", "View", "Update", "remove"]
      choice2 = st.sidebar.selectbox("Menu", menu)
      if choice2 == "Add":
         st.subheader("Enter Petrolpump Details:")
         create_for_Petrolpump()
      elif choice2 == "View":
         st.subheader("View the Petrolpump details:")
         read_for_Petrolpump()
      elif choice2 == "Update":
         st.subheader("Updated petrolpump  tasks")
         update_for_Petrolpump()
      elif choice2 == "remove":
         st.subheader("Deleted petrolpump  tasks")
         delete_for_Petrolpump()

   elif choice == "Owners":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("Menu", menu)
      if choice2 == "Add":
            st.subheader("Enter Owners Details:")
            create_for_Owners()
      elif choice2 == "View":
            st.subheader("View Owners details:")
            read_for_Owners()
      elif choice2 == "Update":
            st.subheader("Update created tasks")
            update_for_Owners()
      elif choice2 == "Remove":
            st.subheader("Delete created tasks")
            delete_for_Owners()

   elif choice == "Employee":
      menu = ["Add", "View", "Update", "Remove"]
      choice2 = st.sidebar.selectbox("Menu", menu)
      if choice2 == "Add":
         st.subheader("Enter Employee Details:")
         create_for_Employee()
      elif choice2 == "View":
         st.subheader("View the Employee details:")
         read_for_Employee()
      elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Employee()
      elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Employee()

   elif choice == "Customer":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("Menu", menu)
     if choice2 == "Add":
         st.subheader("Enter trainer Details:")
         create_for_Customer()
     elif choice2 == "View":
         st.subheader("View the trainer details:")
         read_for_Customer()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Customer()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Customer()

   elif choice == "Invoice":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("Menu", menu)
     if choice2 == "Add":
         st.subheader("Enter Invoice Details:")
         create_for_Invoice()
     elif choice2 == "View":
         st.subheader("View the Invoice details:")
         read_for_Invoice()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Invoice()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Invoice()

   elif choice == "Tanker":
     menu = ["Add", "View", "Update", "Remove"]
     choice2 = st.sidebar.selectbox("Menu", menu)
     if choice2 == "Add":
         st.subheader("Enter Tanker Details:")
         create_for_Tanker()
     elif choice2 == "View":
         st.subheader("View the Tanker details:")
         read_for_Tanker()
     elif choice2 == "Update":
         st.subheader("Update created tasks")
         update_for_Tanker()
     elif choice2 == "Remove":
         st.subheader("Delete created tasks")
         delete_for_Tanker()


   elif choice == "Custom Query":
      query = st.text_input("Enter Your Query:")
      if st.button("Run Query"):
         c.execute(query)
         data = c.fetchall()
         st.dataframe(data)

   else:
      st.subheader("About tasks")

if __name__ == '__main__':
   main()