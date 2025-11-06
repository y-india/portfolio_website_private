import streamlit as st
import base64




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







# ---------- PAGE SETTINGS ----------
st.set_page_config(page_title="💼 My Portfolio Project", layout="wide")

# ---------- BACKGROUND ----------
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_img = img_to_base64("full_blur_background .PNG")

st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background: url("data:image/png;base64,{bg_img}");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}
[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}
[data-testid="stSidebar"] {{
    background-color: rgba(0,0,0,0.25);
}}
</style>
""", unsafe_allow_html=True)

# ---------- MAIN CONTENT ----------
st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown("""
<div style="
    text-align:center;
    color:white;
    background: rgba(0, 0, 0, 0.35);
    padding: 40px 30px;
    border-radius: 18px;
    backdrop-filter: blur(6px);
    box-shadow: 0 4px 20px rgba(0,0,0,0.2);
">
    <h1 style="font-size: 38px;">💼 My Portfolio Project</h1>
    <h3 style="font-weight: 400; margin-top: 10px; color: #d9d9d9;">
        This very website you are exploring — is itself a project built by me.
    </h3>
    <hr style="width:60%; margin:25px auto; border:1px solid rgba(255,255,255,0.3);">
    <p style="font-size: 18px; color: #f2f2f2; line-height: 1.8; max-width: 800px; margin:auto;">
        This portfolio is <b>completely self-made</b> — crafted from scratch using
        <b>Streamlit, HTML, CSS</b> and the help of <b>ChatGPT</b> for ideas and optimization.
        <br><br>
        I didn’t use any template or prebuilt design system.
        Every section — from the layout to buttons — is written and refined by me alone.
    </p>
    <br>
    <p style="font-size: 17px; color: #dddddd;">
        The codebase and repository are <b>private</b>, but I take pride in saying this portfolio
        reflects both my <b>skills and creativity</b>.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)





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
# ---------- FOOTER ----------
st.markdown("""
    <hr style='border: 0.5px solid #ccc;'>
    <p style='text-align:center; color:white; font-size:0.9rem;'>
        © 2025 Yuvraj | Built Entirely by Myself
    </p>
""", unsafe_allow_html=True)
