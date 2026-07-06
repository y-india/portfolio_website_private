import streamlit as st



# https://github.com/y-india/images_hosting/blob/main/Gemini_Generated_Image_tif7gotif7gotif7.png?raw=true


BG_IMAGE_URL = "https://github.com/y-india/images_hosting/blob/main/Gemini_Generated_Image_tif7gotif7gotif7.png?raw=true"

st.markdown(f"""
<style>

/* Background */
[data-testid="stAppViewContainer"] {{
    background:
        linear-gradient(rgba(0,0,0,0.65), rgba(0,0,0,0.65)),
        url("{BG_IMAGE_URL}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Transparent Header */
[data-testid="stHeader"] {{
    background: transparent;
}}

/* Global Text Color */
html, body, [class*="css"], .stMarkdown, p, li, h1, h2, h3, h4, h5, h6 {{
    color: white !important;
}}

</style>
""", unsafe_allow_html=True)

st.title("🚀 My Product Journey")

st.caption(
    "A timeline of how my approach to building products has evolved through client work, validation, and continuous learning."
)

st.divider()

st.header("August 2025 • Freelancing")

st.write("""
I began my journey as a freelancer, working with clients across different domains.

During this period I worked with **10-13 clients** on projects involving:

- Data Analysis
- Spreadsheet Automation
- Tutoring
- Python Development

Freelancing gave me exposure to real users, real deadlines, changing requirements,
and the importance of delivering solutions that actually solve someone's problem.

As my academic workload increased, I decided to pause freelancing and focus on
improving my technical skills while exploring product building.
""")

st.success("""
**Key takeaway**

Building software is valuable, but building something people truly need is even more important.
""")

st.divider()

st.header("Career Companion")

st.subheader("The Problem")

st.write("""
Many students receive interview assignments, coding assessments, or interview
calls but struggle to understand what companies actually expect from them.

I wanted to build an AI companion that could guide students throughout the
entire hiring journey by understanding their profile, application stage,
assignments, and interview progress.
""")

st.subheader("Validation")

st.write("""
Before committing to development, I wanted to understand whether the problem
was important enough to solve.

To validate it, I:

- Connected with potential users through LinkedIn and email.
- Conducted one-to-one conversations with around 10 students and fresh graduates.
- Collected 133 email contacts for a broader validation round.
- Designed a survey focused on users' experiences and behaviors.
- Received around 30 responses.
""")

st.warning("""
The validation showed that the problem wasn't painful enough for most users,
and the evidence wasn't strong enough to justify building the product.

Instead of continuing based on assumptions, I decided to move on.
""")

st.divider()

st.header("PromptPolish")

st.subheader("The Problem")

st.write("""
PromptPolish was designed as a Chrome extension that converts raw prompts into
well-structured prompts using user preferences, shortcuts, and personalized context.

The goal was to help beginner developers, college students, and fresh graduates
communicate more effectively with AI coding assistants.
""")

st.subheader("Validation")

st.write("""
This time I focused on validating before investing significant development time.

The process included:

- Speaking with more than 20 potential users.
- Creating a fake landing page.
- Sharing it with my LinkedIn connections.
- Testing messaging and interest before building the product.
""")

st.info("""
The validation approach inspired by **The Right It** helped me avoid spending
months building a product that people ultimately didn't want.

Although the idea initially appeared promising, I later realized that many of my
conversations unintentionally focused on presenting the solution instead of
deeply understanding users' existing problems.

Recognizing this early saved significant time and effort.
""")

st.divider()

st.header("What I'm Focused On Today")

st.write("""
Today my focus is understanding people before thinking about products.

I'm connecting with students, fresh graduates, career switchers, founders,
and working professionals through LinkedIn, email, and WhatsApp.

Instead of discussing product ideas, I focus on understanding their day-to-day
frustrations, workflows, challenges, and recurring problems.

My goal is to discover meaningful patterns first and allow product ideas to
emerge naturally from those conversations.
""")

st.divider()

st.header("How My Thinking Has Evolved")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Earlier**

- Start with an idea.
- Build quickly.
- Validate later.
- Focus on the solution.
""")

with col2:
    st.markdown("""
**Today**

- Start with people.
- Understand their work.
- Identify recurring problems.
- Validate before building.
- and more!
""")

st.divider()

st.header("Principles I Follow")

st.markdown("""
- Build evidence before writing code.
- Validate assumptions early.
- Learn from users instead of convincing them.
- Save months by testing ideas before building.
- Measure progress through learning, not just shipping.
""")

st.divider()

st.caption(
    "This journey is still evolving, and every conversation helps me become a better engineer, product thinker, and problem solver."
)




if st.button("⬅ Back to Projects"):
    st.switch_page("pages/2_📂_My_Projects.py")
