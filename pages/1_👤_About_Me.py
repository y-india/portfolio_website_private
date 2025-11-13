import streamlit as st
import base64
# https://media.githubusercontent.com/media/y-india/portfolio_website_private/refs/heads/main/assets/full_blur_background.PNG
# Page settings
st.set_page_config(page_title="About | Yuvraj", layout="wide")
import streamlit as st

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


with col2:
    st.markdown(
        """
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

        Helloo, age is 17 ,I’m <b>Yuvraj Rana</b>, a beginner Python and Machine Learning developer from a 
        village near Ambala, Haryana. I’m a self-taught learner who enjoys exploring technology 
        and building things that make life easier.

        <br><br>

        I started coding out of curiosity, learning step by step through practice, online resources, 
        and experimentation. Over time, I discovered my interest in data, machine learning, and 
        computer vision — and I’ve been learning and creating projects ever since.

        <br><br>

        <b>My skills include:</b><br>
        > Python, NumPy, Pandas (and related libraries)<br>
        > Machine Learning with Scikit-learn<br>
        > Computer Vision with OpenCV<br>
        > Data Analytics: cleaning, preprocessing, visualization, and analysis<br>
        > Streamlit App Development<br>
        > Automation and data-driven solutions<br>
        <br>

        I like working on projects from start to finish — understanding the problem, 
        writing clean code, and turning ideas into working results.

        <br><br>

        I come from a place where tech opportunities are limited, but I’m creating my own 
        path through consistent learning and real-world practice. I often use 
        <b>AI tools and chatbots like ChatGPT</b> to learn faster, get ideas, and improve 
        my code — using them as part of my growth process.

        <br><br>

        Right now, I’m building my portfolio, 
        and I’m working on machine learning and data analytics projects, 
        and starting freelancing to gain real experience and help others with data-driven solutions. 
        Every day I learn something new, and I’m excited to keep growing.
        </div>
        """,
        unsafe_allow_html=True
    )

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

