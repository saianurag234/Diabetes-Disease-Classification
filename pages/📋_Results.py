import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import numpy as np
import time


final_prediction = prediction

if(prediction == 0):
    st.subheader("The Paitent is not having Diabetes")

if(prediction == 1):
    st.subheader("The Paitent is having Diabetes")

back = st.button("Click here to try again")
if back:
    switch_page("Upload Image")
