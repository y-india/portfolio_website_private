import streamlit as st

def toggle_dark_mode():
    st.session_state.dark_mode = not st.session_state.get("dark_mode", False)

def apply_theme():
    # Initialize only once (never reset)
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    # Sidebar toggle WITHOUT linking directly to state
    st.sidebar.button(
        "🌙 Dark Mode" if not st.session_state.dark_mode else "☀️ Light Mode",
        on_click=toggle_dark_mode
    )

    # Light CSS
    light_css = """
    <style>
        .stApp { background-color: white; color: black; }
    </style>
    """
    dark_css = """
<style>
/* Dark mode background */
.stApp {
    background-color: #0E1117 !important;
    color: #E6E6E6 !important;
    background-blend-mode: darken !important;
    filter: brightness(0.85);
}

/* Sidebar background */
[data-testid="stSidebar"] {
    background-color: #C0C0C0 !important;
}

/* 🔥 Sidebar page text red */
[data-testid="stSidebarNav"] a {
    color: black !important;
    font-weight: 600 !important;
}

/* Buttons */
.stButton > button {
    background-color: #000 !important;
    color: white !important;
    border: 1px solid #444 !important;
    border-radius: 8px !important;
}
</style>
"""


    # Apply theme
    if st.session_state.dark_mode:
        st.markdown(dark_css, unsafe_allow_html=True)
    else:
        st.markdown(light_css, unsafe_allow_html=True)