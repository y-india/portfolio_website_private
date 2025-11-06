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
    font-size: 25px;
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

set_bg("PATH_TO_BACKGROUND_IMAGE")

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
st.title("PROJECT TITLE HERE")

st.markdown("<br>", unsafe_allow_html=True)

# ------------ OVERVIEW ------------
st.subheader("📘 Overview")
st.markdown("""
<div class="highlight-box">
Write 20–30 word overview describing what problem your project solves and how it helps users.
Focus on simplicity + outcome.
</div>
""", unsafe_allow_html=True)

st.image("IMAGE_PATH_1", caption="Final app / dashboard preview")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ LINKS ------------
st.subheader("🔗 Links")

st.write("""
<div class="highlight-box">
<b>GitHub Repository:</b>  
<a href="GITHUB_LINK" target="_blank">GITHUB_LINK</a>
</div>
""", unsafe_allow_html=True)

st.write("""
<div class="highlight-box">
<b>Live Application:</b>  
<a href="LIVE_APP_LINK" target="_blank">Open App (May take a few seconds)</a>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ PROBLEM ------------
st.subheader("🚨 Problem Statement")
st.markdown("""
<div class="highlight-box">
1. Problem point one<br>
2. Problem point two<br>
3. Problem point three<br>
4. Problem point four<br>
5. Problem point five<br><br>
Short sentence explaining real-world context and why this matters.
</div>
""", unsafe_allow_html=True)

st.image("IMAGE_PATH_2", caption="Dataset / real-world scenario")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ SOLUTION ------------
st.subheader("✅ Solution Overview")
st.markdown("""
<div class="highlight-box">
Explain your technical approach in 40–50 words. Include model / algorithm / workflow and why your approach is efficient and practical.
</div>
""", unsafe_allow_html=True)

st.image("IMAGE_PATH_3", caption="Architecture / workflow")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ RESULTS ------------
st.subheader("📊 Key Results")
st.markdown("""
<div class="highlight-box">
✅ Result or accuracy<br>
✅ Model choice brief<br>
✅ Performance note<br>
✅ Practical outcome for users
</div>
""", unsafe_allow_html=True)

st.image("IMAGE_PATH_4", caption="Model performance / charts")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ STRUCTURE ------------
st.subheader("🧱 Project Structure")
st.markdown("""
<div class="highlight-box">
Explain pipeline, folder structure, notebooks, modularity, and thought process.
</div>
""", unsafe_allow_html=True)

st.image("IMAGE_PATH_5", caption="Repository / pipeline diagram")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ SKILLS ------------
st.subheader("🛠 Skills & Tools Used")
st.image("IMAGE_PATH_6")

st.markdown("<br><br>", unsafe_allow_html=True)

# ------------ CONCLUSION ------------
st.subheader("🏁 Conclusion")
st.markdown("""
<div class="highlight-box">
Write 40–50 word conclusion. Mention learning, real-world impact,
future enhancements, and that full code + docs are available on GitHub.
</div>
""", unsafe_allow_html=True)

st.image("IMAGE_PATH_7", caption="Final output screenshot")

# ------------ FOOTER LINKS ------------
st.write("### 🔗 GitHub Repository")
st.write("GITHUB_LINK")

st.write("### 🚀 Live Application")
st.write("LIVE_APP_LINK")

# ------------ NAVIGATION BUTTONS ------------
if st.button("⬅️ Back to Home"):
    st.switch_page("portfolio_web.py")

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
