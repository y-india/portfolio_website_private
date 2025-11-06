# https://github.com/y-india/project-Smart-Attendance-System-opencv/tree/main



import streamlit as st
import base64









# ------------ SECTION HEADER STYLE (RED BOX) ------------
st.markdown("""
<style>
.section-header-box {
    background-color: #ff4b4b;
    color: #white !important;
    padding: 10px 16px;
    border-radius: 6px;
    font-size: 25px !important;
    font-weight: 600;
    display: inline-block;
}
</style>
""", unsafe_allow_html=True)






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

# ------------ STREAMLIT WIDE MODE ------------
st.set_page_config(layout="wide")

# ------------ HIGHLIGHT BOX STYLE ------------
st.markdown("""
<style>
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

/* Title style */
h1 {
    color: #e6eef5 !important;
    text-shadow: 0px 0px 6px rgba(0,0,0,0.6);
    font-size: 48px !important;
    text-align: center;
    margin-bottom: 6px;
}

/* Keep subheaders left aligned */
h2, h3 {
    text-align: left;
}

/* Responsive */
@media (max-width: 800px) {
  .highlight-box { font-size: 18px; padding: 12px; }
  h1 { font-size: 36px !important; }
}
</style>
""", unsafe_allow_html=True)

# ------------ BACKGROUND IMAGE FUNCTION ------------
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








# use your provided blurred background
set_bg("project_pictures/opencv_project/Smart Attendance_ So_background_needed.jpg")

# ------------ TITLE STYLE (white BOX title) ------------
st.markdown("""
<style>
.red-header-box {
    background-color: white;
    background-opacity: 0.05;
    color: black!important;
    padding: 20px;
    border-radius: 10px;
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    text-shadow: 0px 0px 0px black;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="red-header-box">Smart Attendance System For Organizations</div>', unsafe_allow_html=True)

# ------------ OVERVIEW ------------
st.markdown('<div class="section-header-box">📘 Overview</div>', unsafe_allow_html=True)


st.markdown("""
<div class="highlight-box">
A real-time Smart Attendance System using face, eye, and mask detection. Built with OpenCV and LBPH face recognition to automatically log attendance (name, time, confidence) and create daily attendance files — ideal for schools, offices, and organizations.
</div>
""", unsafe_allow_html=True)

# image: final app / preview (webcam snapshot)
st.image("project_pictures/opencv_project/attandnace_marked_correct_attandancesystem.png")
st.markdown('<div class="img-caption">Final preview — attendance saved successfully</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ LINKS ------------
st.markdown('<div class="section-header-box">🔗 Links </div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<b>GitHub Repository:</b>  
<a href="https://github.com/y-india/project-Smart-Attendance-System-opencv/tree/main" target="_blank">GITHUB_LINK</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
<b>Want to get your own:</b>  
<a href="mail to : y.india.main@gmail.com" target="_blank">mail to : y.india.main@gmail.com</a>  
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ PROBLEM STATEMENT ------------
st.markdown('<div class="section-header-box">🚨 Problem Statement </div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
1. Manual attendance is time-consuming and error-prone. <br>
2. Paper-based or manual systems are easy to manipulate. <br>
3. Organizations need automated daily logs for compliance and reporting. <br>
4. Multi-entry and duplicate logging must be prevented. <br>
5. A lightweight solution is required that runs on standard webcams/CCTV.
</div>
""", unsafe_allow_html=True)

# dataset / real-world snapshot
st.image("project_pictures/opencv_project/green_imagee_while_saving_attandancesystem.png")
st.markdown('<div class="img-caption">50 Image Capturing for Training</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ SOLUTION OVERVIEW ------------
st.markdown('<div class="section-header-box">✅ Solution Overview</div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
The system uses OpenCV for face, eye, and mask detection and LBPH for face recognition. It captures frames from a webcam/CCTV stream, recognizes known users, logs attendance once per day, and stores daily CSV logs. Lightweight design allows easy training with custom images.
</div>
""", unsafe_allow_html=True)

# architecture / detection examples (webcam images)
st.image("project_pictures/opencv_project/blur_detection_red_attandancesystem.png")
st.markdown('<div class="img-caption">Detection example — blurry frame flagged</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ KEY RESULTS ------------
st.markdown('<div class="section-header-box">📊 Key Results</div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
- Real-time detection of face, eyes, and mask with reliable LBPH recognition.<br>
- Automatic daily CSV logs stored in `/attendance_records` with timestamp and confidence.<br>
- Prevents duplicate entries for the same person per day and saves snapshots when configured.<br>
- Runs on standard laptops/desktops without heavy hardware.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/opencv_project/eye_not_visible_red_attandnacesystem.png")
st.markdown('<div class="img-caption">Edge case: eye not visible — entry flagged for review</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ IMPLEMENTATION SNIPPET ------------
st.markdown('<div class="section-header-box">🧩 Implementation Snippet</div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
1. Capture frames from camera. <br>
2. Run cascade detectors for face and eye/mask checks. <br>
3. Use LBPH recognizer to identify known users (trained model stored in `/trainer`). <br>
4. On confident match, append name, date, time, and confidence to daily CSV. <br>
5. Prevent double logging and optionally save snapshot images.
</div>
""", unsafe_allow_html=True)


st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ PROJECT STRUCTURE ------------
st.markdown('<div class="section-header-box">🧱 Project Structure</div>', unsafe_allow_html=True)

st.markdown("""
<div class="highlight-box">
Folders include:<br> `/trainer` (trained model files),<br> `/datasets` (user face images),<br> `/attendance_records` (daily CSVs),<br> and `/snapshots`. <br>Core scripts: `#1dataset_creator.py`,<br> `#2train_recognizer.py`,<br> `#3main.py`.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ SKILLS & TOOLS ------------
st.markdown('<div class="section-header-box">🛠 Skills & Tools</div>', unsafe_allow_html=True)
st.image("project_pictures/opencv_project/skills_used_opencv_attandancesystem.png")
st.markdown('<div class="img-caption">Libraries and tools used</div>', unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ CONCLUSION & RECOMMENDATIONS ------------
st.markdown('<div class="section-header-box">🏁 Conclusion & Recommendations</div>', unsafe_allow_html=True)
st.markdown("""
<div class="highlight-box">
This Smart Attendance System delivers a lightweight, reliable solution for automated attendance using face recognition and OpenCV. The repository contains dataset creation scripts, training code, and the live detection script so reviewers get full clarity on setup and operation.<br><br>

Recommended next steps for production deployment: integrate with organization directory services, add secured access control for logs, implement model retraining pipelines, and deploy on an edge device or local server for continuous operation.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ FOOTER LINKS & CONTACT ------------
st.markdown('<div class="section-header-box">🔗 Github link</div>', unsafe_allow_html=True)

st.code("https://github.com/y-india/project-Smart-Attendance-System-opencv/tree/main")


st.markdown('<div class="section-header-box">📞 Contact</div>', unsafe_allow_html=True)
st.code("For installations and demo setup, email: y.india.main@gmail.com")
st.image("project_pictures/opencv_project/Smart Attendance_ So_background_needed.jpg")

# ------------ NAVIGATION BUTTONS ------------
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
