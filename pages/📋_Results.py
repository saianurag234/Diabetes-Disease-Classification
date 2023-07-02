import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import numpy as np
import time

image_url = "https://us.123rf.com/450wm/ximagination/ximagination2102/ximagination210201046/163994189-diabetes-2d-flat-vector-concept-for-banner-website-illustration-landing-page-flyer-etc.jpg?ver=6"

if 'prediction' in st.session_state:
    final_prediction = st.session_state['prediction']

if(final_prediction == 0):
    st.header("The Paitent is not having Diabetes")

if(final_prediction == 1):
    st.markdown("<h1 style='font-size: 38px;'>The Patient is having Diabetes</h1>", unsafe_allow_html=True)
    st.markdown(
    f'<div style="display: flex; justify-content: center;">'
    f'<img src="{image_url}" alt="Image" width="550" align="center">'
    '</div>',
    unsafe_allow_html=True
)

st.title(" ")
back = st.button("Click here to try again")
if back:
    switch_page("Patient Data")
