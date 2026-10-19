import pandas as pd 
import streamlit as st 

#---PAGE SETUP---
about_page = st.Page(
    page="pages/about_me.py",
    title="About Developer",
    icon=":material/account_circle:",
    default=True,
)

excel_data_analysis_page = st.Page(
    page="pages/excel_dashboard.py",
    title="Excel Data Analysis",
    icon=":material/bar_chart:",
)

#---NAVIGATION SETUP---
pg1 = st.navigation(
    {
        "Info":[about_page],
        "Project":[excel_data_analysis_page],
     }
)

st.logo("images/ico_streamlit_py.png")
st.sidebar.text("Made with ❤️ by AK")

#---RUN NAVIGATION---
pg1.run()
