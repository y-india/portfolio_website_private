import streamlit as st


st.set_page_config(page_title="Tutoring", layout="wide")






import base64
def set_bg_url(image_url):
    st.markdown(
        f"""
        <style>
        [data-testid="stAppViewContainer"] {{
            background-image: url("{image_url}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg_url(
    "https://raw.githubusercontent.com/y-india/images_hosting/main/background_for_tutoring_page.jpg"
)










st.markdown("""
<div style="text-align:center; margin-top:-20px;">
    <h1>🎓 Tutoring and Project Walkthroughs</h1>
    <p style="font-size:17px;">
    Clear explanations and complete implementations
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div style="
        background:white;
        padding:20px;
        border-radius:18px;
        box-shadow:0 8px 25px rgba(0,0,0,0.25);
    ">
    <h3>Python if else elif</h3>
    <iframe
        src="https://drive.google.com/file/d/1278WxSfw4kW1f18oFMZAbMtlwXEAUKbF/preview"
        width="100%"
        height="240">
    </iframe>
    <p>Core decision making logic explained with examples</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="
        background:white;
        padding:20px;
        border-radius:18px;
        box-shadow:0 8px 25px rgba(0,0,0,0.25);
    ">
    <h3>Basic ML Project</h3>
    <iframe
        src="https://drive.google.com/file/d/1slaGLRZqsyZUU1SzLuHkwyUHGT4Nr094/preview"
        width="100%"
        height="240">
    </iframe>
    <p>End to end machine learning pipeline walkthrough</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div style="
        background:white;
        padding:20px;
        border-radius:18px;
        box-shadow:0 8px 25px rgba(0,0,0,0.25);
    ">
    <h3>ML Project to API to UI</h3>
    <iframe
        src="https://www.youtube.com/embed/dQw4w9WgXcQ"
        width="100%"
        height="240">
    </iframe>
    <p>Model deployment using API and UI integration</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

if st.button("⬅ Back to Projects"):
    st.switch_page("pages/2_📂_My_Projects.py")
