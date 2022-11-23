import streamlit as st
from create import create
from database import create_table
from delete import delete
from read import read
from update import update

def main():
   st.title("Petrol Pump Management App")
   menu = ["Add", "View", "Upgrade", "Remove", "Custom Query"]
   choice = st.sidebar.selectbox("Menu", menu)
   create_table()
   if choice == "Add":
      st.subheader("Enter Dealer Details:")
      create()
   elif choice == "View":
      st.subheader("View created tasks")
      read()
   elif choice == "Upgrad":
      st.subheader("Update created tasks")
      update()
   elif choice == "Remove":
      st.subheader("Delete created tasks")
      delete()
   
   elif choice == "Custom Query":
      query = st.text_input("Enter Your Query:")
      c.execute(query)
      data = c.fetchall()
      st.dataframe(data)

   else:
      st.subheader("About tasks")

if __name__ == '__main__':
   main()




