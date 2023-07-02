import streamlit as st
from streamlit_extras.switch_page_button import switch_page

st.title("Diabetes Disease Classification")


data_entry = st.button("Click Here to enter the details of the patients")
if want_to_contribute:
    switch_page("Patient Data")
