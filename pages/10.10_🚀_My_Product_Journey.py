import streamlit as st

st.set_page_config(
    page_title="Product Journey",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 My Product Journey")
st.caption(
    "From freelancing to product discovery. "
    "This page documents how my thinking about building startups has evolved."
)

st.divider()

st.header("August 2025 • Freelancing")

st.write("""
I started my software development journey as a freelancer.

Over the next few months I worked with **10-13 clients**, building real projects
and learning how software is delivered in production environments.

Freelancing taught me:

- Writing maintainable code
- Working with deadlines
- Communicating with clients
- Turning requirements into working products

I eventually paused freelancing to focus on my studies and long-term product building.
""")

st.info("Biggest lesson: Building software is one skill. Building the right software is another.")

st.divider()

st.header("February - March 2026 • Startup Experiment #1")

st.subheader("The Idea")

st.write("""
I wanted to build an AI career companion for students and fresh graduates.

The idea was to guide users throughout the hiring process by remembering their
profile, understanding their interview stage, helping with assignments,
interview preparation, and reducing uncertainty during job applications.
""")

st.subheader("Before Building")

st.write("""
Instead of immediately building the product, I started reading books on
product management and customer discovery.

Some books that changed my thinking were:

- The Mom Test
- Competing Against Luck
""")

st.subheader("Validation")

st.write("""
My validation process included:

- Collecting potential users through LinkedIn and email
- Interviewing around 10 target users
- Running another validation round with 133 collected emails
- Receiving approximately 30 survey responses
""")

st.subheader("Outcome")

st.error("""
The evidence was weak.

People didn't experience the problem strongly enough for the solution to become valuable.

I decided not to build the product.
""")

st.success("""
What I learned

• Don't fall in love with ideas.
• Validate assumptions before writing code.
• Interviews are more valuable than opinions from friends.
""")

st.divider()

st.header("Startup Experiment #2 • PromptPolish")

st.subheader("The Idea")

st.write("""
PromptPolish was a Chrome extension designed for developers.

Instead of manually improving prompts for AI coding assistants,
users could highlight a prompt and instantly convert it into a structured,
high-quality prompt using keyboard shortcuts.

The extension also supported:

- Custom prompt styles
- User preferences
- Coding language context
- Theme customization
""")

st.subheader("Validation")

st.write("""
This time I wanted to validate before building.

I:

- Interviewed more than 20 potential users
- Created a fake landing page
- Shared it with LinkedIn connections
- Used messaging experiments inspired by The Right It
""")

st.subheader("What Went Wrong")

st.warning("""
Although I believed I was following The Mom Test,
I later realized I had been pitching my solution instead of exploring users'
existing behavior and problems.

The interviews were biased because I focused on my idea instead of their experiences.
""")

st.success("""
This failure saved months of development.

I learned that a bad validation process can make a weak idea appear strong.
""")

st.divider()

st.header("What I'm Doing Today")

st.write("""
Today I don't start with startup ideas.

Instead, I start with people.

I'm conducting open-ended interviews with:

- Fresh graduates
- Career switchers
- Job seekers

My goal is to identify recurring problems before thinking about solutions.

Only after finding a meaningful pattern will I begin validating a product idea.
""")

st.divider()

st.header("Books That Changed My Thinking")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
**Product & Startups**

- The Mom Test
- The Right It
- Competing Against Luck
    """)

with col2:
    st.markdown("""
**Other Topics**

- Psychology
- Business
- Decision Making

(20+ books read so far.)
    """)

st.divider()

st.header("My Product Principles")

principles = [
    "Build evidence before code.",
    "Interview people before designing solutions.",
    "Validate assumptions early.",
    "Kill weak ideas quickly.",
    "Learning is progress, even when a product isn't built."
]

for p in principles:
    st.markdown(f"✅ {p}")

st.divider()

st.caption(
    "This journey is ongoing. Every interview, experiment, and failed assumption "
    "helps me become a better engineer and product builder."
)










if st.button("⬅ Back to Projects"):
    st.switch_page("pages/2_📂_My_Projects.py")