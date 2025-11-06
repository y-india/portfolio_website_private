import streamlit as st
import base64

# Page setup
st.set_page_config(page_title="Yuvraj | Portfolio", layout="wide")

# Custom top header bar
st.markdown("""
<style>
.header-title {
    font-size: 22px; /* decreased size */
    font-weight: 700;
    color: white; /* white text */
    background: rgba(0, 0, 0, 0.55); /* black transparent background */
    padding: 6px 12px; /* some spacing around text */
    border-radius: 6px; /* smooth corners */
    position: fixed;
    top: 10px;
    left: 20px;
    z-index: 999;
}
</style>

<div class="header-title">
    Yuvraj Rana <span style="font-weight:400;">Portfolio</span>
</div>
""", unsafe_allow_html=True)
import os

def set_background(image_path):
    full_path = os.path.join(os.path.dirname(__file__), image_path)
    with open(full_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}
        [data-testid="stHeader"] {{background: rgba(0,0,0,0);}}
        [data-testid="stToolbar"] {{right: 2rem;}}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply background
set_background("assets/SELECTED_background_blur_for_portfolio.PNG")

# ⬇️ tweak: adjust padding to center text more naturally on most screens
st.markdown("""
<style>
/* full-viewport wrapper that centers content exactly in middle */
.hero-wrapper {
    position: fixed;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
    pointer-events: none;
}

/* force viewport height for Streamlit container */
body, [data-testid="stAppViewContainer"] {
    height: 100vh;
    overflow: hidden;
}

.hero-inner {
    width: 90%;
    max-width: 1100px;
    pointer-events: auto;
}

.css-1v3fvcr.e16nr0p30 {padding-top:0px;}
</style>

<div class="hero-wrapper">
<div class="hero-inner" style="text-align:center;">
""", unsafe_allow_html=True)

# Headline (slightly darker gray for better contrast)
st.markdown(
    "<h1 style='color:black; text-shadow: 2px 2px 8px rgba(255,255,255,0.3); font-size:56px; font-weight:800; text-decoration:underline; text-underline-offset:10px;'>HI ! I'm YUVRAJ</h1>",
    unsafe_allow_html=True,
)

# Highlighted text box (subtle dark overlay)
st.markdown("""
<div style="
    display:inline-block;
    background-color: rgba(0,0,0,0.55);
    padding: 20px 28px;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
    max-width: 850px;
    margin:auto;">
<p style="color:white; font-size:20px; line-height:1.5;">
I specialize in transforming data into intelligent and interactive solutions through advanced Python development,
machine learning, and computer vision. With hands-on experience in Pandas, NumPy, Matplotlib, Seaborn, scikit-learn,
OpenCV, and Streamlit, I engineer predictive systems and automation tools that solve practical problems,
improve efficiency, and drive measurable outcomes in real-world environments.
</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""</div></div>""", unsafe_allow_html=True)

import streamlit as st

slide = """
<script>
function slideOut(){
    document.body.style.transition = "transform 0.5s ease-in-out";
    document.body.style.transform = "translateX(-100%)";
}
</script>
"""
st.markdown(slide, unsafe_allow_html=True)

# Buttons below text
col1, col2, col3 = st.columns([1,1,1])
with col1:
    if st.button("👤_About"):
        st.switch_page("pages/1_👤_About_Me.py")

with col2:
    if st.button("📂_Projects"):
        st.switch_page("pages/2_📂_My_Projects.py")

with col3:
    if st.button("✉️_Contact"):
        st.switch_page("pages/3_✉️_Contact_Me.py")


