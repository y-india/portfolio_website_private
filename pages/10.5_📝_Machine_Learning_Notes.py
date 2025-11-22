import streamlit as st
import base64

from utils.theme import apply_theme



# ------------ REMOVE TOP SPACE (multi-version safe) ----------
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







# -----------------------------------------------------------
# Page Configuration
# -----------------------------------------------------------
st.set_page_config(page_title="Machine Learning Notes | Yuvraj", layout="wide")




apply_theme()
# ---------------------- BACKGROUND IMAGE ----------------------
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

set_bg("circuit-board-pattern-stockcake.jpg")

# -----
# -----------------------------------------------------------
# Title Section
# -----------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center; margin-top:40px;">
        <h1 style="color:white; font-weight:800;">🧠 Machine Learning Notes</h1>
        <p style="color:white; font-size:18px; opacity:0.85;">
            A collection of my personal learning notebooks covering end-to-end Machine Learning — 
            from data preprocessing to advanced ensemble and association rule learning techniques.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)



# -----------------------------------------------------------
# Overview Section
# -----------------------------------------------------------
st.markdown(
    """
    <div style="
        background-color: rgba(0,0,0,0.55);
        padding: 30px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 0 25px rgba(0,0,0,0.3);
        font-size:18px;
        line-height:1.7;
    ">
    <h2 style="font-weight:800;">📖 Overview</h2>
    <p>
        This repository serves as a structured collection of my Machine Learning learning journey.
        It includes a series of Jupyter notebooks where I explore, experiment, and visualize 
        key ML concepts in both theory and implementation.
    </p>
    <p>
        The goal of these notes is to document my hands-on practice while creating 
        reference material that’s easy to follow for learners and professionals alike.
    </p>
    <p>
        Each part focuses on progressively advanced topics — starting with 
        data handling and regression, moving towards clustering, hyperparameter optimization,
        ensemble methods, and association rule learning.
    </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)



# GitHub Link
# -----------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <a href="https://github.com/y-india/machine-learning-notes" target="_blank">
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



st.markdown("<br>", unsafe_allow_html=True)
# -----------------------------------------------------------
# Topics Section
# -----------------------------------------------------------
st.markdown(
    """
    <div style="
        background-color: rgba(0,0,0,0.55);
        padding: 30px;
        border-radius: 15px;
        color: white;
        box-shadow: 0 0 25px rgba(0,0,0,0.3);
        font-size:18px;
        line-height:1.7;
    ">
    <h2 style="font-weight:800;">⚡ Topics Covered</h2>

    <h4>📘 Part 1: Data Handling & Core ML Concepts</h4>
    <ul>
        <li>Data Cleaning: Outlier Detection (IQR, Z-Score), Missing Values, and Duplicates</li>
        <li>Feature Scaling: StandardScaler, MinMaxScaler</li>
        <li>Regression Models: Linear, Multiple, and Polynomial Regression</li>
        <li>Classification: Logistic Regression & Binary Classification</li>
        <li>Evaluation Metrics: Confusion Matrix, Accuracy, Precision, Recall, F1 Score</li>
        <li>Handling Imbalanced Datasets (SMOTE, RandomOverSampler)</li>
        <li>Practical Implementations on Real and Synthetic Datasets</li>
    </ul>

    <h4>📗 Part 2: Advanced ML Techniques</h4>
    <ul>
        <li>Model Optimization with GridSearchCV & RandomizedSearchCV</li>
        <li>Cross-Validation Techniques: K-Fold, Leave-One-Out (LOO), and Leave-P-Out (LPO)</li>
        <li>Unsupervised Learning: K-Means, Hierarchical, and DBSCAN Clustering</li>
        <li>Cluster Evaluation, Label Visualization, and Feature Transformation</li>
        <li>Dimensionality Reduction & Feature Engineering Insights</li>
    </ul>

    <h4>📙 Part 3: Association Rule & Ensemble Learning</h4>
    <ul>
        <li>Association Rule Learning: Apriori & FP-Growth Algorithms</li>
        <li>Ensemble Techniques: Bagging, Voting, and Stacking (Classification & Regression)</li>
        <li>Polynomial Regression and Feature Interaction Experiments</li>
        <li>Performance Comparison Across Multiple Models</li>
    </ul>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("<br>", unsafe_allow_html=True)

# -----------------------------------------------------------
# GitHub Link
# -----------------------------------------------------------
st.markdown(
    """
    <div style="text-align:center;">
        <a href="https://github.com/y-india/machine-learning-notes" target="_blank">
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

st.markdown("<br><br>", unsafe_allow_html=True)

# -----------------------------------------------------------
# Navigation Buttons (DO NOT CHANGE STRUCTURE)
# -----------------------------------------------------------
if st.button("⬅️ Back to Home"):
    st.switch_page("portfolio_web.py")

st.markdown("<br><br>", unsafe_allow_html=True)

nav1, nav2, nav3 , nav4 , nav5 , nav6 , nav7 , nav8 , nav9 = st.columns(9)
with nav7:
    if st.button("About Me"):
        st.switch_page("pages/1_👤_About_Me.py")
with nav8:
    if st.button("Projects"):
        st.switch_page("pages/2_📂_My_Projects.py")
with nav9:
    if st.button("📞 Contact"):
        st.switch_page("pages/3_✉️_Contact_Me.py")

st.markdown("<br><br>", unsafe_allow_html=True)
# Footer
st.markdown("""
    <hr style='border: 0.5px solid #ccc;'>
    <p style='text-align:center; color:gray; font-size:0.9rem;'>
        © 2025 Yuvraj | Built with Streamlit HTML
    </p>
""", unsafe_allow_html=True)
