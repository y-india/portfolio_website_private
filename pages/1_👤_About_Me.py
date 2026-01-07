import streamlit as st
import base64
from utils.theme import apply_theme  # <- this should now resolve



# https://media.githubusercontent.com/media/y-india/portfolio_website_private/refs/heads/main/assets/full_blur_background.PNG
# Page settings
st.set_page_config(page_title="About | Yuvraj", layout="wide")
 

apply_theme()

st.markdown(
    """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url('https://media.githubusercontent.com/media/y-india/portfolio_website_private/refs/heads/main/assets/SELECTED_background_blur_for_portfolio.PNG');
        background-size: cover;          /* makes it full screen */
        background-position: center;     /* centers the image */
        background-repeat: no-repeat;    /* prevents tiling */
        background-attachment: fixed;    /* stays in place while scrolling */
    }
    </style>
    """,
    unsafe_allow_html=True
)


# # ---------------------- BACKGROUND IMAGE ----------------------
# def set_bg(image_file):
#     with open(image_file,"rb") as f:
#         b64 = base64.b64encode(f.read()).decode()
#     st.markdown(
#         f"""
#         <style>
#         [data-testid="stAppViewContainer"] {{
#             background: url("data:image/png;base64,{b64}");
#             background-size: cover;
#             background-attachment: fixed;
#         }}
#         </style>
# """
#         ,
#         unsafe_allow_html=True
#     )

# set_bg("assets/SELECTED_background_blur_for_portfolio.PNG")


# Set about page background


# ---- ABOUT SECTION ----

# Use columns for picture + text
col1, col2 = st.columns([1,2])

# Styling for circular image
st.markdown("""
<style>
.profile-pic {
    width: 420px;
    border-radius: 50%;
    border: 3px solid rgba(255,255,255,0.7);
}

</style>
""", unsafe_allow_html=True)

# Place new transparent profile picture
with col1:
    st.markdown(
        f"""
        <img src="data:image/png;base64,{base64.b64encode(open("SELECTED_PROFILE_IMG.jpg","rb").read()).decode()}"
        class="profile-pic">
        """,
        unsafe_allow_html=True
    )


# ---- About text ----
with col2:
    st.markdown("""
    <div style="
        background-color: rgba(0,0,0,0.55);
        padding: 25px;
        border-radius: 12px;
        color: white;
        box-shadow: 0 0 20px rgba(0,0,0,0.3);
        font-size:18px;
        line-height:1.6;
    ">
    <h2 style="font-weight:800;">About Me</h2>

    <p>Hello, I’m <b>Yuvraj Rana</b>. I come from a small town near Ambala, Haryana, and I love exploring how technology can solve real problems. I’m a self-taught Python and Machine Learning developer who learns by building, documenting, and iterating.</p>

    <p>Right now, my focus is on creating systems that guide learning, career decisions, and practical problem-solving. Every project I do is an experiment in thinking, coding, and understanding the real world.</p>

    <p>My approach is simple: I take ideas, test them through code and data, learn from mistakes, and document what works. I often use AI tools like ChatGPT to accelerate my learning, get inspiration, and refine my solutions — always keeping the process my own.</p>

    <p><b>Current experiments:</b></p>
    <ul>
        <li>AI-driven career guidance systems</li>
        <li>Stage-based decision support for applications</li>
        <li>Long-term memory design for AI-driven projects</li>
        <li>Data-driven automation tools for real-world problems</li>
    </ul>

    <p>Every day, I build, test, document, and reflect — creating a growing body of work that will compound over time and open doors to new ideas and opportunities.</p>
    </div>
    """, unsafe_allow_html=True)


st.markdown("<br>", unsafe_allow_html=True)

# Back button
if st.button("⬅️ Back to Home"):
    st.switch_page("portfolio_web.py")

st.markdown("<br><br>", unsafe_allow_html=True)

nav1, nav2, nav3 , nav4 , nav5 , nav6 , nav7 , nav8 , nav9= st.columns(9)

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
    <p style='text-align:center; color:black; font-size:0.9rem;'>
        © 2025 Yuvraj | Built with Streamlit HTML
    </p>
""", unsafe_allow_html=True)

