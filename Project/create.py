import streamlit as st
from database import add_data

def create():
    # col1, col2 = st.columns(2)
    # with col1:
    #     train_no = st.number_input("Train No:")
    #     train_name = st.text_input("Train Name:")
    #     train_type = st.text_input("Train Type:")
    # with col2:
    #     source = st.selectbox("Source", ["Bengaluru", "Chennai", "Mangaluru"])
    #     dest = st.selectbox("Destination", ["Bengaluru", "Chennai", "Mangaluru"])
    #     available = st.radio("Availability",["Yes", "No"])

    if st.button("Add Train"):
        # add_data(train_no, train_name, train_type, source, dest, available)
        st.success("Successfully added Train: {}".format(train_name))