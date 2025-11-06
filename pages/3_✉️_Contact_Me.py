import streamlit as st

import base64

def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


st.set_page_config(page_title="Contact Me", layout="centered")

import os
def set_bg(image_file):
    with open(image_file, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background: url("data:image/png;base64,{b64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        [data-testid="stHeader"] {{background: rgba(0,0,0,0);}}
        [data-testid="stToolbar"] {{right: 2rem;}}
        </style>
        """,
        unsafe_allow_html=True
    )

# Apply background
set_bg("assets/SELECTED_background_for_portfolio.PNG")  # no spaces

# Background
page_bg_img = """
<style>
[data-testid="stAppViewContainer"] {
    
}
.contact-box, .logo-box {
    background-color: rgba(0,0,0,0.75);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    width: 380px;
    margin: auto;
}
.contact-box {
    margin-top: 10vh;
}
.contact-links p {
    font-size: 18px;
    margin: 10px 0;
}
.contact-links a {
    color: #4EC8F4;
    font-weight: bold;
    text-decoration: none;
}
.logo-box img {
    width: 50px;
    margin: 0 15px;
    filter: brightness(0) invert(1);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Contact Info Box
st.markdown("""
<div class="contact-box">
    <h2>📬 Contact Me</h2>
    <div class="contact-links">
        <p><b>Email:</b> <a href="mailto:y.india.main@gmail.com">y.india.main@gmail.com</a></p>
        <p><b>GitHub:</b> <a href="https://github.com/y-india" target="_blank">github.com/y-india</a></p>
        <p><b>LinkedIn:</b> Coming soon...</p>
        <p><b>Streamlit Cloud:</b> <a href = "https://share.streamlit.io/" target="_blank">https://share.streamlit.io/</a></p>
    </div>
</div>
""", unsafe_allow_html=True)
# Start Platforms box
st.markdown("""
<div class="logo-box">


<img src="https://cdn.simpleicons.org/gmail/ffffff" width="32">
<img src="https://cdn.simpleicons.org/github/ffffff" width="32">
<img src="https://cdn.jsdelivr.net/npm/simple-icons@v9/icons/linkedin.svg"
        width="34" style="filter: invert(1);">
<img src="https://cdn.simpleicons.org/streamlit/ffffff" width="32">
""", unsafe_allow_html=True)




# Back button
if st.toggle("⬅️ Back to Home"):
    st.switch_page("portfolio_web.py")

nav1, nav2, nav3 , nav4 , nav5= st.columns(5)

with nav4:
    if st.button("about Me"):
        st.switch_page("pages/1_👤_About_Me.py")
       
with nav5:
    if st.button("my Projects"):
        st.switch_page("pages/2_📂_My_Projects.py")
   



st.markdown("<br><br>", unsafe_allow_html=True)
# Footer
st.markdown("""
    <hr style='border: 0.5px solid #ccc;'>
    <p style='text-align:center; color:black; font-size:0.9rem;'>
        © 2025 Yuvraj | Built with Streamlit
    </p>
""", unsafe_allow_html=True)

