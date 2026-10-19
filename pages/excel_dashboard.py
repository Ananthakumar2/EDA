# https://www.youtube.com/watch?v=Sb0A9i6d320

import pandas as pd #pip install pandas openpyxl
#import plotly.express as px #pip install plotly-express
import streamlit as st #pip install streamlit
excel_file_ref=0

def file_open_view(df):
    """
    df = pd.read_excel(
        #io='Royal_Enfield_Data.xlsx',
        io=selected_file,
        engine='openpyxl',
        sheet_name='book1',
        skiprows=0,
        usecols='B:N',
        nrows=16
    )"""
    #remove the first column of sheet
    df = df.iloc[:, 1:]
    
    selected_columns = st.multiselect(
        "Select columns to display",
        options=df.columns.tolist(),
        default=df.columns.tolist()
    )

    #Display the whole sheet
    st.dataframe(df[selected_columns])

def file_da_analytics_report(df):
    """
    df = pd.read_excel(
        io=selected_file,
        engine='openpyxl',
        sheet_name='book1',
        skiprows=0,
    )"""
    df = df.iloc[:, 1:]

    # --------------------------------------------------
    # KPI CARDS
    # --------------------------------------------------
    total_rows = len(df)
    total_columns = len(df.columns)
    missing_values = int(df.isna().sum().sum())
    duplicate_rows = int(df.duplicated().sum())

    st.markdown(
        '<p style="font-size:20px; font-weight:bold; margin-bottom:1px;"> 📌 Dataset Overview</p>',
        unsafe_allow_html=True
    )

    st.markdown("""
    <style>
    div[data-testid="stMetricValue"] {
        font-size: 24px;
    }
    div[data-testid="stMetricLabel"] {
        font-size: 18px;
    }
    </style>
    """, unsafe_allow_html=True)

    k1, k2, k3, k4 = st.columns(4)

    k1.metric("Total Records", f"{total_rows:,}")
    k2.metric("Total Columns", f"{total_columns:,}")
    k3.metric("Missing Values", f"{missing_values:,}")
    k4.metric("Duplicate Rows", f"{duplicate_rows:,}")
    
    data = []
    try:
        
        for col in df.columns:
            data.append({
                "Column Name": col,
                "Data Type": str(df[col].dtype),
                "Highest Value":max(df[col]),
                "Lowest Value":min(df[col]),
                #"High Frequency":sum(df[col]) if str(df[col].dtype)!='str',
            })
        st.table(data)
    except:
        st.error("Please check the values of all the columns in your excel sheet",icon=":material/insert_chart:")

    #Break
    st.divider()

    #Next portion
    st.markdown(
        '<p style="font-size:20px; font-weight:bold; margin-bottom:1px;">Data Analytics - Graph</p>',
        unsafe_allow_html=True
    )

    x_label = st.selectbox("Select Column-(X-Axis)", df.columns)
    y_value = st.multiselect("Select Column(s)-(Y-Axis)", df.select_dtypes(include="number").columns)

    if y_value:
        col1, col2 = st.columns(2, gap="small")
        with col1:
            fig1 = px.line(
                df,
                x=x_label,
                y=y_value,
                title = f"<span style='color:blue'>{x_label}</span> vs <span style='color:blue'>{', '.join(y_value)}</span>",
                markers=True
            )

            fig1.update_layout(
                title_x=0.5,
                title_xanchor="center",
                height=320,
                margin=dict(l=10, r=10, t=50, b=10)
            )

            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            fig2 = px.bar(
                df,
                x=x_label,
                y=y_value,
                title = f"<span style='color:blue'>{x_label}</span> vs <span style='color:blue'>{', '.join(y_value)}</span>",
                
            )

            fig2.update_layout(
                title_x=0.5,
                title_xanchor="center",
                height=320,
                margin=dict(l=10, r=10, t=50, b=10)
            )

            st.plotly_chart(fig2, use_container_width=True)

    else:
        st.info("Please select at least one Y-axis column.",icon=":material/vertical_split:")


def show_excel_file():
    global excel_file_ref

    excel_file_ref = 0
    uploaded_file = None
    
    # Create two columns with fixed proportions
    xl_file, xl_sheet = st.columns(
        [1, 1],
        vertical_alignment="top",
        gap="small"
    )

    with xl_file:
        uploaded_file = st.file_uploader(
            "👇 :blue[Upload an Excel file to start data analysis:]",
            type=["xlsx"],
            key="excel_upload"
        )

        if uploaded_file is not None:
            st.success("Valid Excel file (.xlsx)")
            st.write(f":blue[Selected File:] {uploaded_file.name}")
            excel_file_ref = 1

    with xl_sheet:
        if uploaded_file is not None and excel_file_ref == 1:
            try:
                excel_file = pd.ExcelFile(uploaded_file)
                sheet_names = excel_file.sheet_names

                selected_sheet = st.selectbox(
                    "👇 :blue[Select Worksheet]",
                    options=sheet_names,
                    key="excel_sheet"
                )

                df = pd.read_excel(
                    uploaded_file,
                    sheet_name=selected_sheet
                )

                if df.empty:
                    st.warning("The selected worksheet contains no data.")
                    xl_sheet_ref=0
                else:
                    st.success(f"Worksheet loaded: {selected_sheet}")
                    xl_sheet_ref=1

            except Exception as e:
                st.error(f"Unable to read Excel file: {e}")
            
    try:
        if xl_sheet_ref==1:
            # Row 1: Both buttons stay on the same line
            #col1, col2 = st.columns([1, 1], vertical_alignment="center")
            st.markdown("""
            <style>
            div.stButton > button {
                background-color: #7B7B8F;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 14px;
            }

            div.stButton > button:hover {
                background-color: #0056b3;
                color: white;
                border: none;
            }
            </style>
            """, unsafe_allow_html=True)

            col1, col2, col3 = st.columns([3, 3, 4])

            with col1:
                if st.button("View the File Content", icon=":material/preview:"):
                    st.session_state["action"] = "view"

            with col2:
                if st.button("Analyse the Data", icon=":material/analytics:"):
                    st.session_state["action"] = "analysis"

            st.divider()#break

            # Display the output below both buttons
            if st.session_state.get("action") == "view":
                file_open_view(df)

            elif st.session_state.get("action") == "analysis":
                file_da_analytics_report(df)
    except:
        print()
   
# Create two columns: a tiny one for the image, and a larger one for the text
col1, col2 = st.columns([0.06, 0.94], vertical_alignment="center")

with col1:
    st.image("./images/ms_excel_1.png", width=40)  # Adjust width to match text size

with col2:
    st.markdown(
        '<p style="font-size:24px; font-weight:bold; margin-bottom:15px;">Excel Data Analytics</p>',
        unsafe_allow_html=True
    )

st.write(":orange[{ An Application Designed for Analyzing Data in Excel worksheets }]")
st.divider()

#Call the function
show_excel_file()

