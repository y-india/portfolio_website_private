import streamlit as st



BG_IMAGE_URL = "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=1920&q=80"
st.markdown(f"""
<style>
[data-testid="stAppViewContainer"] {{
    background-image: url("{BG_IMAGE_URL}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

[data-testid="stHeader"] {{
    background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
    right: 2rem;
}}

.main {{
    text-align: center;
}}

.big-title {{
    font-size: 70px;
    font-weight: 900;
    color: #11d9ff;
    text-align: center;
    margin-top: 10px;
    text-shadow: 0px 0px 15px rgba(0,255,255,0.4);
    -webkit-text-stroke: 2px #003344;
}}

.coming {{
    font-size: 60px;
    font-weight: bold;
    color: white;
    width: 100%;
    text-align: center;
    margin-top: 10px;
    text-shadow:
        0 0 5px #ffffff,
        0 0 10px #11d9ff,
        0 0 20px #11d9ff,
        0 0 40px #11d9ff;
    animation: glow 1s ease-in-out infinite alternate;
}}

@keyframes glow {{
    from {{
        text-shadow:
            0 0 5px #ffffff,
            0 0 10px #11d9ff,
            0 0 20px #11d9ff;
    }}
    to {{
        text-shadow:
            0 0 10px #ffffff,
            0 0 20px #11d9ff,
            0 0 40px #11d9ff,
            0 0 60px #11d9ff;
    }}
}}

.message {{
    font-size: 32px;
    color: #d7e3ea;
    margin-top: 10px;
    margin-bottom: 25px;
    font-weight: 700;
    width: 100%;
    display: flex;
    justify-content: flex-start;
    text-align: left;
    background: rgba(0, 0, 0, 0.45);
    padding: 18px 24px;
    border-radius: 16px;
    backdrop-filter: blur(6px);
    -webkit-text-stroke: 1px #02141a;
    text-shadow: 0px 2px 6px rgba(0,0,0,0.9);
    box-shadow: 0 0 20px rgba(0,0,0,0.5);
}}

.footer {{
    text-align: center;
    color: #aab7c4;
    margin-top: 100px;
    font-size: 14px;
}}

.stTextInput>div>div>input {{
    background-color: rgba(255,255,255,0.08);
    color: white;
    border: 1px solid #11d9ff;
    border-radius: 12px;
    padding: 12px;
}}

.stButton>button {{
    background: linear-gradient(90deg, #0077ff, #11d9ff);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 16px 40px;
    font-size: 20px;
    font-weight: bold;
    width: 100%;
    height: 45px;
}}

.stButton>button:hover {{
    opacity: 0.7;
}}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.stTextInput input {
    height: 15px;
    font-size: 22px;
    padding: 12px 20px;
    border-radius: 14px;
    border: 2px solid #11d9ff;
    background-color: rgba(255,255,255,0.08);
    color: white;
}
.stTextInput input::placeholder {
    font-size: 20px;
    color: #cfd8dc;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<style>

/* Main title */
h1{
    color:#FFFFFF !important;
    font-weight:800;
}

/* Section headings */
h2,h3{
    color:#FFFFFF !important;
    font-weight:700;
}

/* Paragraphs */
p{
    color:#F1F5F9 !important;
    font-size:18px;
    line-height:1.7;
}

/* Markdown lists */
li{
    color:#F1F5F9 !important;
    font-size:17px;
}

/* Captions */
[data-testid="stCaptionContainer"]{
    color:#D1D5DB !important;
}

/* Markdown */
[data-testid="stMarkdownContainer"]{
    color:#F1F5F9 !important;
}

/* Bold text */
strong{
    color:#FFFFFF !important;
}

/* Links */
a{
    color:#7DD3FC !important;
    font-weight:600;
}

a:hover{
    color:#38BDF8 !important;
}

/* Info, Success, Warning boxes */
[data-testid="stAlert"] *{
    color:white !important;
}

</style>
""", unsafe_allow_html=True)

st.title("✨ PromptPolish")
st.caption("A Chrome Extension for Converting Raw AI Prompts into Structured Prompts")

st.markdown("---")

st.header("📖 The Story")

st.write("""
I enjoy building products that solve problems I personally face.

While using AI tools like ChatGPT and Claude, I noticed that the quality of responses depended heavily on the quality of the prompt. Writing good prompts, however, took time and effort.

That frustration led me to build **PromptPolish**.
""")

st.header("🚀 The Idea")

st.write("""
PromptPolish is a Chrome extension that converts a raw prompt into a structured, high quality prompt before sending it to an AI chatbot.

The goal was simple:

> Spend less time writing prompts and more time getting useful AI responses.
""")

st.subheader("Key Features")

st.markdown("""
- ✨ Convert raw prompts into structured prompts
- ⚙️ Custom prompt engineering instructions defined by the user
- ⌨️ Keyboard shortcuts for instant prompt conversion
- 👤 Personal profile support (role, programming language, preferred AI chatbot)
- 🎨 Customizable popup theme
""")

st.header("🎯 Target Users")

st.markdown("""
- Beginner programmers
- College students who use AI while coding
- Freshers entering the software industry
- Anyone who frequently works with AI chatbots
""")

st.header("🧪 The Real Learning")

st.write("""
Building the extension was only half of the journey.

Initially, I interviewed around 10 developers after reading **The Mom Test**. Unfortunately, I made the classic beginner mistake: I pitched my solution instead of validating the problem.

People appreciated the idea, but I wasn't learning whether they actually had a painful problem worth solving.

After realizing my mistake, I revisited both **The Mom Test** and **The Right It**.

This time I focused on validating demand instead of collecting compliments.
""")

st.markdown("""
### What I did

- Built a landing page
- Collected emails of 100+ students
- Sent cold emails and follow-up emails
- Tried to get real user commitment instead of positive feedback
- Looked for genuine **skin in the game**
""")

st.header("📊 Outcome")

st.success("""
The validation revealed that although people liked the idea, they weren't willing to commit or show meaningful skin in the game.

Instead of continuing to build features, I decided to stop the project.
""")

st.write("""
While PromptPolish never became a product, it became one of my most valuable learning experiences.

It taught me that validating demand is far more important than writing code. Killing a weak idea early saved months of development time and allowed me to focus on stronger opportunities.
""")

st.header("💡 Key Takeaways")

st.markdown("""
- Build less. Validate more.
- Positive feedback is not product validation.
- Look for commitment, not compliments.
- It's better to kill a weak idea early than spend months building something nobody truly wants.
""")

st.subheader("🔗 Links")

st.write(
    """
    <div class="highlight-box">
        <b>GitHub Repository:</b><br>
        <a href="https://github.com/y-india/repo_for_PP_s_page" target="_blank">
            https://github.com/y-india/repo_for_PP_s_page
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.write(
    """
    <div class="highlight-box">
        <b>Live Demo:</b><br>
        <a href="https://promptpolish-soon.streamlit.app/" target="_blank">
            Try PromptPolish
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)

st.info("""
**Note:** The actual Chrome extension source code is private.

The live demo showcases the prompt transformation workflow and the core idea behind PromptPolish.
""")




st.markdown("<br><br>", unsafe_allow_html=True)

nav1, nav2, nav3 , nav4 , nav5 , nav6 , nav7 , nav8 , nav9 = st.columns(9)
with nav7:
    if st.button("👤"):
        st.switch_page("pages/1_👤_About_Me.py")
with nav8:
    if st.button("📂"):
        st.switch_page("pages/2_📂_My_Projects.py")
with nav9:
    if st.button("📞"):
        st.switch_page("pages/3_✉️_Contact_Me.py")

st.markdown("<br><br>", unsafe_allow_html=True)
# Footer
st.markdown("""
    <hr style='border: 0.5px solid #ccc;'>
    <p style='text-align:center; color:gray; font-size:0.9rem;'>
        © 2025 Yuvraj | Built with Streamlit HTML
    </p>
""", unsafe_allow_html=True)
