import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import numpy as np
import time

if 'prediction' in st.session_state:
    final_prediction = st.session_state['prediction']

if(final_prediction == 0):
    st.header("The Paitent is not having Diabetes")

if(final_prediction == 1):
    st.markdown("**The Patient is having Diabetes**")

back = st.button("Click here to try again")
if back:
    switch_page("Patient Data")
