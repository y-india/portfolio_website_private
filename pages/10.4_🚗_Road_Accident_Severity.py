# https://project-road-accident-severity-prediction-system-jwjbruwbaroal.streamlit.app/
# https://github.com/y-india/project-Road-Accident-Severity-Prediction-System/tree/main

from utils.theme import apply_theme



import streamlit as st
import base64

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(layout="wide")
apply_theme()
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

# ---------------------- STYLES: HIGHLIGHT BOX, SECTION HEADERS, TITLE, CAPTIONS ----------------------
st.markdown("""
<style>
/* Highlight box used for overview, problem, solution, results, etc. */
.highlight-box {
    background-color: #000000;
    color: #e6eef5 !important;
    padding: 14px;
    border-radius: 10px;
    font-size: 20px;
    line-height: 1.45;
    text-align: left;
    margin-bottom: 10px;
}

/* Section header red box */
.section-header-box {
    background-color: #FF4200;
    color: white !important;
    padding: 8px 14px;
    border-radius: 8px;
    font-size: 24px !important;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 12px;
}


/* Image caption badge */
.img-caption {
    color: #ff9f1c;
    font-weight: 600;
    margin-top: 8px;
    display: inline-block;
    background: rgba(0,0,0,0.55);
    padding: 6px 10px;
    border-radius: 6px;
}

/* Keep subheaders left aligned */
h2, h3 {
    text-align: left;
}

/* Responsive adjustments */
@media (max-width: 800px) {
  .highlight-box { font-size: 18px; padding: 12px; }
  .section-header-box { font-size: 20px !important; }
  .red-header-box { font-size: 30px; padding: 14px; }
}
</style>
""", unsafe_allow_html=True)

# ---------------------- BACKGROUND IMAGE FUNCTION ----------------------
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

# provided background
set_bg("project_pictures/road_accident_project/ROAD TRAFFIC and ACC_background.png")

# ---------------------- TITLE (red box) ----------------------
st.markdown("""
<style>
h1 {
    color: #ffd700 !important;  
    font-weight: 800 !important;
    text-shadow: 0px 0px 6px rgba(0,0,0,0.6);
}

/* Gold title inside a border box */
.bordered-text {
    border: 3px solid #ffd700;  
    padding: 8px 20px;
    border-radius: 8px;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="bordered-text">Road Accident Severity Intelligence System</h1>', unsafe_allow_html=True)

st.markdown("Data-driven accident risk prediction for safer roads in India")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------- OVERVIEW ----------------------
st.markdown('<div class="section-header-box">📘 Overview</div>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight-box">
Real-time and batch ML workflows to estimate accident severity (Slight / Serious / Fatal) using vehicle, driver, and environmental attributes. The system helps authorities prioritize interventions and focus on high-risk conditions and locations.
</div>
""", unsafe_allow_html=True)

# main preview image

st.image("project_pictures/road_accident_project/app_preview.png")
st.markdown('<div class="img-caption">Dashboard(App) preview</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- LINKS ----------------------
st.markdown('<div class="section-header-box">🔗 Links</div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<b>GitHub Repository:</b>  
<a href="https://github.com/y-india/project-Road-Accident-Severity-Prediction-System/tree/main " target="_blank">      https://github.com/y-india/project-Road-Accident-Severity-Prediction-System/tree/main          </a>
</div>
""", unsafe_allow_html=True)
st.image("project_pictures/road_accident_project/smoothe_project_roaf.png")
st.markdown("""
<div class="highlight-box">
<b>APP:</b>  
<a href="https://project-road-accident-severity-prediction-system-jwjbruwbaroal.streamlit.app/" target="https://project-road-accident-severity-prediction-system-jwjbruwbaroal.streamlit.app/">    https://project-road-accident-severity-prediction-system-jwjbruwbaroal.streamlit.app/   </a> (may need to wake up the app)
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- PROBLEM STATEMENT ----------------------
st.markdown('<div class="section-header-box">🚨 Problem Statement</div>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight-box">
1. Road accidents cause significant loss of life and property across India.<br>
2. There is limited predictive tooling for pre-emptive risk identification.<br>
3. Rapid, data-driven severity assessment is needed for faster emergency response.<br>
4. High-risk zones and conditions remain poorly prioritized.<br>
5. Authorities need actionable, interpretable insights to reduce fatalities.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/road_accident_project/red_orange_signs_project_road.png")
st.markdown('<div class="img-caption">Real-world road scene / signage example</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- SOLUTION OVERVIEW ----------------------
st.markdown('<div class="section-header-box">✅ Solution Overview</div>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight-box">
Preprocessed and encoded a real Indian accident dataset, engineered features, and trained multiple classifiers (Random Forest, XGBoost, SVM). Performed hyperparameter tuning and model comparison, then selected Random Forest for deployment based on balanced performance and interpretability. Streamlit UI exposes encoded dropdowns and returns color-coded severity predictions.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/road_accident_project/xbg_confusion_matrix_project_road.png")
st.markdown('<div class="img-caption">XGBoost confusion matrix — model diagnostics</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- KEY RESULTS ----------------------
st.markdown('<div class="section-header-box">📊 Key Results</div>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight-box">
✅ Trained and compared multiple classifiers with visual evaluation.<br>
✅ Random Forest selected for balanced accuracy and explainability.<br>
✅ Severity classification mapped to clear actionable labels (Slight / Serious / Fatal).<br>
✅ Saved model artifact (`random_forest_model_of_accident_project.pkl`) and inference pipeline for reproducible predictions.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/road_accident_project/random_forest_confusion_matrix_project_road.png")
st.markdown('<div class="img-caption">Random Forest confusion matrix — selected model</div>', unsafe_allow_html=True)

st.image("project_pictures/road_accident_project/poor_confusion_martrics_project_road.png")
st.markdown('<div class="img-caption">Additional model confusion diagnostics</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- PROJECT STRUCTURE ----------------------
st.markdown('<div class="section-header-box">🧱 Project Structure</div>', unsafe_allow_html=True)

st.image("project_pictures/road_accident_project/structure_project_road.png")
st.markdown('<div class="img-caption">Repository & pipeline structure</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- SKILLS & TOOLS ----------------------
st.markdown('<div class="section-header-box">🛠 Skills & Tools Used</div>', unsafe_allow_html=True)

st.image("project_pictures/road_accident_project/skills_used_project_road.png")
st.markdown('<div class="img-caption">Technologies & libraries used</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- ADDITIONAL VISUAL ----------------------
st.markdown('<div class="section-header-box">🔎 Additional Visual</div>', unsafe_allow_html=True)
st.image("project_pictures/road_accident_project/smoothe_project_roaf.png", caption="Dashboard detail / smoothing visualization")

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- CONCLUSION & RECOMMENDATIONS ----------------------
st.markdown('<div class="section-header-box">🏁 Conclusion & Recommendations</div>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight-box">
This project delivers a complete ML workflow for predicting road accident severity and provides interpretable outputs for decision-makers. The repository contains all notebooks, model artifacts, and the Streamlit app so reviewers gain full clarity on the steps taken and reasoning. <br><br>

Recommendation:
For complete project details, step-by-step workflows, and all code artifacts, visiting the GitHub repository is essential. It provides full clarity on the dataset, preprocessing, model training, evaluation, and deployment. This ensures you fully understand the project and can replicate or extend it confidently.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)



st.image("project_pictures/road_accident_project/ROAD TRAFFIC and ACC.png")

# ---------------------- FOOTER LINKS & CONTACT ----------------------
st.write("### 🔗 GitHub Repository")
st.write("https://github.com/y-india/project-Road-Accident-Severity-Prediction-System/tree/main")

st.write("### 🚀 Live Application / Demo")
st.write("https://project-road-accident-severity-prediction-system-jwjbruwbaroal.streamlit.app/  \n*(May need to wakeup)*")

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------------- NAVIGATION BUTTONS ----------------------
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
