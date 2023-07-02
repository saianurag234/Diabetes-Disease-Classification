import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import numpy as np
import time

if 'prediction' in st.session_state:
    final_prediction = st.session_state['prediction']

if(final_prediction == 0):
    st.header("The Paitent is not having Diabetes")

if(final_prediction == 1):
    st.markdown("<h1 style='font-size: 48px;'>The Patient is having Diabetes</h1>", unsafe_allow_html=True)

back = st.button("Click here to try again")
if back:
    switch_page("Patient Data")
