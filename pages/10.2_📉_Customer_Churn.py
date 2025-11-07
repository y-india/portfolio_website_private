import streamlit as st
import base64

# ---------------------- REMOVE TOP SPACE (multi-version safe) ----------------------
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

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(layout="wide")

# ---------------------- STYLES: HIGHLIGHT BOX + IMG CAPTIONS + TITLE ----------------------
st.markdown("""
<style>
/* Highlight box used for overview, problem, solution, results, etc. */
.highlight-box {
    background-color: rgba(0,0,0,0.92);
    color: #e6eef5 !important;
    padding: 14px;
    border-radius: 10px;
    font-size: 20px;
    line-height: 1.45;
    text-align: left;
    margin-bottom: 10px;
}

/* Image caption styled as an inline badge */
.img-caption {
    color: #ff9f1c;
    font-weight: 600;
    margin-top: 8px;
    display: inline-block;
    background: rgba(0,0,0,0.55);
    padding: 6px 10px;
    border-radius: 6px;
}

/* Page title style */
h1 {
    color: #e6eef5 !important;
    text-shadow: 0px 0px 6px rgba(0,0,0,0.6);
    font-size: 48px !important;
    text-align: center;
    margin-bottom: 6px;
}

/* Subheaders keep default but align left */
h2, h3 {
    text-align: left;
}

/* Small responsive tweaks */
@media (max-width: 800px) {
  .highlight-box { font-size: 18px; padding: 12px; }
  h1 { font-size: 36px !important; }
}
</style>
""", unsafe_allow_html=True)

# ---------------------- BACKGROUND IMAGE (PROJECT-SPECIFIC) ----------------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("project_pictures/churn_detection_project/background_churn_project_selected_blured.png")

# ---------------------- TITLE ----------------------
st.title("Customer Churn Prediction System")

st.markdown("<br>", unsafe_allow_html=True)
# ---------------------- OVERVIEW ----------------------
st.subheader("📘 Overview")
st.markdown("""
<div class="highlight-box">
A machine learning system to predict customer churn so businesses can proactively retain users. 
            The project includes EDA, preprocessing, model training, model saving, and a Streamlit inference app for real-time predictions.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/churn_detection_project/app_image_customer_curn.png")
st.markdown('<div class="img-caption">Final app / dashboard preview </div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- LINKS ----------------------
st.subheader("🔗 Links")

st.markdown("""
<div class="highlight-box">
<b>GitHub Repository:</b>  
<a href="https://github.com/y-india/project-Customer-churn-prediction" target="_blank">https://github.com/y-india/project-Customer-churn-prediction</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<b>Live Application:</b>  
<a href="https://project-customer-churn-prediction-fgtjdu9mp8afy9mqsxqp9m.streamlit.app/" target="_blank">Open App (may take a few mins(may need to wake up))</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- PROBLEM STATEMENT ----------------------
st.subheader("🚨 Problem Statement")
st.markdown("""
<div class="highlight-box">
Churn causes direct revenue loss. This project addresses:<br>
1. Identifying high-risk customers  <br>
2. Enabling personalized retention actions  <br>
3. Reducing re-acquisition costs  <br>
4. Improving lifetime value forecasting  <br>
5. Allowing data-driven retention strategy
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/churn_detection_project/confusion_matrix_churnproject.png")
st.markdown('<div class="img-caption">Confusion matrix — classification performance</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- SOLUTION OVERVIEW ----------------------
st.subheader("✅ Solution Overview")
st.markdown("""
<div class="highlight-box">
Built a full ML pipeline: EDA, <br>preprocessing (encoding & scaling), <br>feature selection, <br>and model training.<br> Trained multiple classifiers and selected Random Forest for deployment. <br>Created an inference pipeline (model + scaler + feature list) and <br>a Streamlit UI for predictions.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/churn_detection_project/importance_by_column_ml_churnproject.png")
st.markdown('<div class="img-caption">Feature importance — top drivers of churn</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- KEY RESULTS ----------------------
st.subheader("📊 Key Results")
st.markdown("""
<div class="highlight-box">
- Trained and validated classification pipeline (Random Forest selected).  <br>
- Evaluation using Accuracy, ROC-AUC, Confusion Matrix, Precision/Recall/F1.  <br>
- Model and preprocessing artifacts saved for production (joblib).
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/churn_detection_project/model_testing_scores_churnproject.png")
st.markdown('<div class="img-caption">Model testing scores — comparison across candidate models</div>', unsafe_allow_html=True)

st.image("project_pictures/churn_detection_project/roc_curve_churnproject.png")
st.markdown('<div class="img-caption">ROC curve — classifier discrimination power</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- IMPLEMENTATION NOTE ----------------------
st.subheader("🧩 Implementation & Deliverables")
st.markdown("""
<div class="highlight-box">
Deliverables include EDA & training notebooks, <br>saved model files (churn_model.pkl, scaler.pkl, model_features.pkl), <br>a `predict.py` inference script, and <br>a Streamlit app for real-time prediction. <br>The repository contains data, notebooks, and instructions to reproduce results.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/churn_detection_project/loop_code_project_churnproject.png")
st.markdown('<div class="img-caption">Training & evaluation loop (notebook snippet)</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- PROJECT STRUCTURE ----------------------
st.subheader("🧱 Project Structure")
st.markdown("""
<div class="highlight-box">
Standard project layout: <br>`data/`, <br>`notebooks/`, <br>`models/`, <br>`predict.py`, <br>`app/streamlit_app.py`, and <br>`requirements.txt`. <br>Models saved with joblib for reproducible inference.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- SKILLS & TOOLS ----------------------
st.subheader("🛠 Skills & Tools Used")

st.image("project_pictures/churn_detection_project/skills_used_in_churnproject.png")
st.markdown('<div class="img-caption">Tools & libraries used in this project</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- CONCLUSION ----------------------
st.subheader("🏁 Conclusion")
st.markdown("""
<div class="highlight-box">
This project successfully builds an end-to-end churn prediction system capable of identifying high-risk customers with strong accuracy and explainability. The trained model, preprocessing pipeline, and deployment script work together to turn raw customer data into actionable retention insights.<br><br>

The repository includes the full workflow — EDA, model training, feature engineering, performance evaluation, and deployment pipeline — so anyone reviewing it will get 100% clarity on the process and implementation. <br><br>

Future improvements include cost-based decision thresholds, advanced calibration techniques, and A/B testing to optimize retention strategies in production environments.
</div>
""", unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- FOOTER LINKS ----------------------
st.write("### 🔗 GitHub Repository")
st.write("https://github.com/y-india/project-Customer-churn-prediction")

st.write("### 🚀 Live Application")
st.write("https://project-customer-churn-prediction-fgtjdu9mp8afy9mqsxqp9m.streamlit.app/  \n*(May take a few seconds to load)*")

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
