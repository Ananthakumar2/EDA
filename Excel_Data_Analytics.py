# https://www.youtube.com/watch?v=Sb0A9i6d320

import pandas as pd #pip install pandas openpyxl
#import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit

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
#pg1 = st.navigation(pages=[about_page,excel_data_analysis_page,testing_page])
pg1 = st.navigation(
    {
        "Info":[about_page],
        "Project":[excel_data_analysis_page],
     }
)

#st.logo(":material/lightbulb_circle:")
st.logo("images/ico_streamlit_py.png")
st.sidebar.text("Made with ❤️ by AK")

#---RUN NAVIGATION---
pg1.run()
