import streamlit as st
import base64
from utils.theme import apply_theme





st.markdown("""
<style>

/* catch multiple Streamlit container names across versions */
[data-testid="stAppViewContainer"] > .main,
.main > .block-container,
.block-container,
.css-18e3th9,   /* older/newer auto-generated class names */
.css-1d391kg {   /* another commonly seen class */
    padding-top: 0 !important;
    margin-top: 0 !important;
}

/* if you still want a tiny gap, change 0 -> 8px */
</style>
""", unsafe_allow_html=True)


st.set_page_config(layout="wide")
apply_theme()
# ✅ CSS for black text highlight boxes
st.markdown("""
<style>
.highlight-box {
    background-color: black;
    color: white !important;
    padding: 14px;
    border-radius: 8px;
    font-size: 25px;
    line-height: 1.5;
    text-align: left;
}

</style>
""", unsafe_allow_html=True)

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

set_bg("project_pictures/ai-based-crop-recomand-project/PremiumAIImageCrop_updated.png")

# ---------------------- TITLE ----------------------
st.markdown("""
<style>
h1 {
    color: #e6eef5 !important;
    text-shadow: 0px 0px 4px black;
    font-size: 48px !important;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

st.title("AI-Based Crop Predictor for Haryana Farmers")


st.markdown("<br>", unsafe_allow_html=True)
# ---------------------- OVERVIEW ----------------------
st.subheader("📘 Overview")
st.markdown("""
<div class="highlight-box">
AI system built to assist farmers in Haryana by recommending the most suitable crop based on real-world factors like district, date, temperature, rainfall, soil type, and previous crop. Designed to provide simple, actionable insights without requiring scientific knowledge.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/ai-based-crop-recomand-project/app_image_of_aicrop_project.png", caption="Final crop recommendation interface")


st.markdown("<br><br>", unsafe_allow_html=True)
# ---------------------- GITHUB + LIVE APP ----------------------
st.subheader("🔗 Links")

st.write(
    """
    <div class="highlight-box">
        <b>GitHub Repository:</b>
        <a href="https://github.com/y-india/project-AI-Based-Crop-Predictor-for-Haryana-Farmerss" target="_blank">
            https://github.com/y-india/project-AI-Based-Crop-Predictor-for-Haryana-Farmerss
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

st.write(
    """
    <div class="highlight-box">
        <b>Live Application:</b>
        <a href="https://project-ai-based-crop-predictor-for-haryana-farmerss-wcwauffdt.streamlit.app/" target="_blank">
            Open App (First load may take a few mins)
        </a>
    </div>
    """,
    unsafe_allow_html=True
)



st.markdown("<br><br>", unsafe_allow_html=True)
# ---------------------- PROBLEM STATEMENT ----------------------
st.subheader("🚨 Problem Statement")
st.markdown("""
<div class="highlight-box">
1. Lack of scientific soil & weather knowledge<br>
2. Difficulty estimating soil moisture<br>
3. Climate-aware crop selection needed<br>
4. Users require a simple prediction tool<br>
5. Changing climate demands data-based guidance<br><br>
This solution connects rural farming with accessible AI guidance.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/ai-based-crop-recomand-project/dataset_image_aicrop_project.png", caption="Real Haryana agricultural data sample")



st.markdown("<br><br>", unsafe_allow_html=True)
# ---------------------- SOLUTION OVERVIEW ----------------------
st.subheader("✅ Solution Overview")
st.markdown("""
<div class="highlight-box">
Two-stage AI pipeline built. First predicts soil moisture using climatic inputs. Second recommends best crop using farmer-friendly fields like district, soil type, weather, and previous crop. Removes complex inputs like NPK or pH to ensure usability in rural scenarios.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/ai-based-crop-recomand-project/avg_smlvl_graph_aicrop_project.png")
st.image("project_pictures/ai-based-crop-recomand-project/2nd_avg_smlvl_aicrop_project.png")


st.markdown("<br><br>", unsafe_allow_html=True)
# ---------------------- KEY RESULTS ----------------------
st.subheader("📊 Key Results")
st.markdown("""
<div class="highlight-box">
✅ Moisture model accuracy: 96.28%<br>
✅ LightGBM with tuning<br>
✅ No lab values required<br>
✅ Built for real rural deployment
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/ai-based-crop-recomand-project/predictedvsctual_aicrop_project.png", caption="Predicted vs Actual Soil Moisture")



st.markdown("<br><br>", unsafe_allow_html=True)
# ---------------------- PROJECT STRUCTURE ----------------------
st.subheader("🧱 Project Structure")
st.markdown("""
<div class="highlight-box">
Step-by-step process including data cleaning, feature engineering, synthetic data creation, cyclical month encoding, soil type integration, and final crop prediction modeling. All notebooks separate for clarity.
</div>
""", unsafe_allow_html=True)





st.markdown("<br><br>", unsafe_allow_html=True)
# ---------------------- SKILLS ----------------------
st.subheader("🛠 Skills & Tools Used")
st.image("project_pictures/ai-based-crop-recomand-project/skills_used_aicrop_project.png")



st.markdown("<br><br>", unsafe_allow_html=True)
# ---------------------- CONCLUSION ----------------------
st.subheader("🏁 Conclusion")
st.markdown("""
<div class="highlight-box">
Developed a rural-focused AI crop advisory system delivering accurate crop recommendations without lab tests. Future plans include map-based soil support and voice-enabled Hindi interface. Full code, datasets, and notebooks on GitHub.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/ai-based-crop-recomand-project/PremiumAIImageCrop.png")

# ---------------------- LINKS REPEATED ----------------------
st.write("### 🔗 GitHub Repository")
st.write("https://github.com/y-india/project-AI-Based-Crop-Predictor-for-Haryana-Farmerss")

st.write("### 🚀 Live Application")
st.write("https://project-ai-based-crop-predictor-for-haryana-farmerss-wcwauffdt.streamlit.app/  \n*(May take a few seconds to load)*")

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
