import streamlit as st
import base64

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

# ------------ STREAMLIT WIDE MODE ------------
st.set_page_config(layout="wide")

# ------------ HIGHLIGHT BOX STYLE ------------
st.markdown("""
<style>
.highlight-box {
    background-color: black;
    color: white !important;
    padding: 14px;
    border-radius: 8px;
    font-size: 22px;
    line-height: 1.5;
    text-align: left;
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

set_bg("project_pictures/real_world_object_traker_project/Object tracking soft_background_blured.png")

# ------------ HEADING STYLE ------------
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

# ------------ TITLE ------------
st.title("Real Time Object Tracker -OpenCV")

st.markdown("<br>", unsafe_allow_html=True)

# ------------ OVERVIEW ------------
st.subheader("📘 Overview")
st.markdown("""
<div class="highlight-box">
Real-Time Object Tracker & Counter detects, tracks, and counts moving objects in real-time using OpenCV. Useful for traffic monitoring, retail analytics, factory automation, and security systems.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ LINKS ------------
st.subheader("🔗 Links")
st.write("""
<div class="highlight-box">
<b>GitHub Repository (Must Visit!):</b>  
<a href="https://github.com/y-india/project-RealTimeObjectTracker-opencv/tree/main" target="_blank">https://github.com/y-india/project-RealTimeObjectTracker-opencv/tree/main</a>
</div>
""", unsafe_allow_html=True)

st.write("""
<div class="highlight-box">
<b>Contact Me(if you want it for your organization):</b>  
<a href="mailto:y.india.main@gmail.com" target="_blank">y.india.main@gmail.com</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ PROBLEM ------------
st.subheader("🚨 Problem Statement")
st.markdown("""
<div class="highlight-box">
1. Manual object counting is slow and error-prone.<br>
2. Real-time monitoring is difficult.<br>
3. Industries like traffic, retail, factories need automated solutions.<br>
4. Security systems require accurate detection.<br>
5. Data collection for analytics is cumbersome.<br><br>
This project automates counting and monitoring accurately and efficiently in real-time.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/real_world_object_traker_project/problem_it_solve_realworld_project.png", caption="Problem solved in real-world scenario")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ SOLUTION ------------
st.subheader("✅ Solution Overview")
st.markdown("""
<div class="highlight-box">
The system uses OpenCV to capture video, detect objects via color and shape filters, track them across frames, and count objects crossing a predefined line. It supports multiple objects, logs data to CSV, and can be extended with ML models like YOLOv8.
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/real_world_object_traker_project/car_detetection_realworld_project.png", caption="Workflow & detection in action")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ RESULTS ------------
st.subheader("📊 Key Results")
st.markdown("""
<div class="highlight-box">
> ✅ Real-time detection and counting<br>
> ✅ Supports multiple shapes & colors<br>
> ✅ Accurate logs saved to CSV<br>
> ✅ Extensible to cars, bikes, people, etc.<br>
> ✅ Works with webcam or video files
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/real_world_object_traker_project/people_detected_realworld_project.png", caption="Results from live video feed")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ STRUCTURE ------------
st.subheader("🧱 Project Structure")
st.image("project_pictures/real_world_object_traker_project/project_struture_realworld_project.png", caption="Project repository & pipeline")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ SKILLS ------------
st.subheader("🛠 Skills & Tools Used")
st.image("project_pictures/real_world_object_traker_project/skills_used_realworld_project.png", caption="Skills & tools used")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ CONCLUSION ------------
st.subheader("🏁 Conclusion")
st.markdown("""
<div class="highlight-box">
This project automates object detection and counting for real-world applications, reduces manual effort, and provides accurate analytics. Future enhancements include ML integration, new object categories, and custom dashboards. Full code and documentation are on GitHub (must visit!).
</div>
""", unsafe_allow_html=True)

st.image("project_pictures/real_world_object_traker_project/code_examle_realworld_project.png", caption="code snippet preview")

# ------------ FOOTER LINKS ------------
st.write("### 🔗 GitHub Repository (Must Visit!)")
st.write("https://github.com/y-india/project-RealTimeObjectTracker-opencv/tree/main")


st.image("project_pictures/real_world_object_traker_project/Object tracking soft_background.png")

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
