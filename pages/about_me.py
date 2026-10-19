# https://www.youtube.com/watch?v=Sb0A9i6d320

import pandas as pd #pip install pandas openpyxl
#import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit
#import re
#import requests
#import time

#---ABOUT SECTION---
    
#col1,col2 = st.columns([1,2], gap="small",vertical_alignment="center")
col1, col2 = st.columns([0.2, 0.8], vertical_alignment="center")        
with col1:
    st.image("./images/ak1.png",width=100)
             
with col2:
    #st.subheader("AK@Ananthakumar")
    st.markdown(
        '<p style="font-size:20px; font-weight:bold; margin-bottom:1px;">AK@Ananthakumar</p>',
        unsafe_allow_html=True
    )
    st.write(
        ":green[{ Role }]: IT Academician & Trainer, Data Analyst & Data Engineer, and App Developer.",
    )
    st.write(
        ":green[{ Mail-ID }]: sri.ak25@gmail.com"
    )
   
st.write("\n")
st.write(":blue[Teaching Experience]")
st.write(
    """
    - 2004 to 2013: Lecturer/Professor in Colleges [India].
    - 2013 to 2018: Head in CSE [Africa].
    """
    )
st.write(":blue[Experience - IT Trainer]")
st.write(
    """
    - Since 2018: Working as an Academician, IT Trainer & Developer.
    """
    )
st.write(":blue[IT Industry Certifications]")
st.write(
    """
    - Google    : Data Analytics.
    - IBM       : Python - Data Science, Data Analytics & Data Visualization
    - IBM       : MySQL
    - Microsoft : Certified Innovative Educator
    """
    )
st.write(":blue[Details of Projects]")
st.write(
    """
    - Online Basic Python Code Tester
    - Online Basic Streamlit Code Tester
    - Web Browser & Web Data Analysis
    - Android: Data Analysis of Diabetics Patients
    - Android: Mobile Attendance App; Python - Server Code; firebase - Database 
    - and etc.,
    """
    )
