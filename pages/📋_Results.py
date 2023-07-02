import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import numpy as np
import time

image_url = "https://img.freepik.com/free-vector/diabetes-flat-composition-medical-with-patient-symptoms-complications-blood-sugar-meter-treatments-medication_1284-28998.jpg?w=500"

if 'prediction' in st.session_state:
    final_prediction = st.session_state['prediction']

if(final_prediction == 0):
    st.header("The Paitent is not having Diabetes")

if(final_prediction == 1):
    st.markdown("<h1 style='font-size: 38px;'>The Patient is having Diabetes</h1>", unsafe_allow_html=True)
    st.image(image_url)

st.title(" ")
back = st.button("Click here to try again")
if back:
    switch_page("Patient Data")
