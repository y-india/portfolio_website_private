import streamlit as st
import base64

# ------------ STREAMLIT WIDE MODE ------------
st.set_page_config(layout="wide")

# ------------ REMOVE TOP SPACE ----------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] > .main,
.main > .block-container,
.block-container,
.css-18e3th9,
.css-1d391kg {
    padding-top: 0 !important;
    margin-top: 0 !important;
}
</style>
""", unsafe_allow_html=True)

# ------------ BACKGROUND IMAGE FUNCTION ------------
def set_bg(image_file):
    with open(image_file,"rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Replace with your background image path
set_bg("project_pictures/background_retail_project.png")

# ------------ HEADING STYLE ------------
st.markdown("""
<style>
h1 {
    color: #e6eef5 !important;
    text-shadow: 0px 0px 4px black;
    font-size: 48px !important;
    text-align: center;
}
.highlight-box {
    background-color: rgba(0,0,0,0.6);
    color: white !important;
    padding: 14px;
    border-radius: 8px;
    font-size: 20px;
    line-height: 1.5;
}
</style>
""", unsafe_allow_html=True)

# ------------ TITLE ------------
st.title("🛒 Retail Sales Analysis Project 🛒")

# ------------ UNDER DEVELOPMENT NOTE ------------
st.markdown("""
<div class="highlight-box">
⚠️ This project is currently under development and will be updated regularly.
All code and progress are available on GitHub.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------
# GitHub Link
# -----------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <a href="https://github.com/y-india/retail-sales-analysis-project" target="_blank">
            <button style="
                background-color:#00BFFF;
                border:none;
                color:white;
                padding:14px 28px;
                font-size:17px;
                font-weight:600;
                border-radius:12px;
                cursor:pointer;
                box-shadow: 0px 4px 10px rgba(0,0,0,0.3);
            ">
            🔗 View Repository on GitHub
            </button>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



# ------------ PROJECT DESCRIPTION ------------
st.subheader("📘 Project Overview")
st.markdown("""
<div class="highlight-box">
This project aims to analyze and forecast retail store sales using historical sales and store information datasets.<br>
Tech stack: Python (pandas, numpy, matplotlib, seaborn), Jupyter Notebook.<br>
Future updates will include exploratory data analysis, sales trend visualizations, predictive modeling and many many more.
</div>
""", unsafe_allow_html=True)

# ------------ NAVIGATION BUTTONS ------------
st.markdown("<br><br>", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)
with col7:
    if st.button("About Me"):
        st.switch_page("pages/1_👤_About_Me.py")
with col8:
    if st.button("Projects"):
        st.switch_page("pages/2_📂_My_Projects.py")
with col9:
    if st.button("📞 Contact"):
        st.switch_page("pages/3_✉️_Contact_Me.py")
