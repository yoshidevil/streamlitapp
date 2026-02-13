import streamlit as st
import pandas as pd
import numpy as np
import time

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="App Biography",
    page_icon="🌟",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM STYLE — LAKERS GRADIENT THEME
# ---------------------------------------------------
st.markdown("""
    <style>

    /* Main background */
    .stApp {
        background: linear-gradient(
            135deg,
            #552583 0%,
            #FDB927 100%
        );
        color: white;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(
            180deg,
            #3C1A5B,
            #552583
        );
        color: white;
    }

    /* Text */
    h1, h2, h3, h4, h5, h6, p, label, span {
        color: white !important;
    }

    /* Buttons */
    .stButton>button {
        background-color: #FDB927;
        color: black;
        border-radius: 8px;
        border: none;
        font-weight: bold;
    }

    .stButton>button:hover {
        background-color: #FFCE4B;
        color: black;
    }

    /* Containers */
    .stMetric, .stDataFrame, .stTable {
        background-color: rgba(0,0,0,0.25);
        border-radius: 10px;
        padding: 10px;
    }

    </style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR NAVIGATION
# ---------------------------------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "Go to:",
    ["🏠 Home", "👤 About Me", "📂 Portfolio", "📊 Skills Dashboard", "📬 Contact"]
)

st.sidebar.markdown("---")
st.sidebar.success("Streamlit Portfolio App")

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------
if page == "🏠 Home":

    st.title("🌟 Welcome to My Digital Portfolio")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("05 Yoshi.jpg", caption="Your Photo")

    with col2:
        st.header("Hello! I'm Nikolai Javier Jr. 👋")
        st.write("""
        I am a passionate student who enjoys building applications, analyzing data,
        and learning new technologies.

        This interactive website showcases:
        - My background
        - My projects
        - My technical skills
        - How to contact me
        """)

    st.markdown("---")

    st.subheader("🚀 Quick Highlights")

    c1, c2, c3 = st.columns(3)
    c1.metric("Projects Completed", "12", "+2")
    c2.metric("Technologies Learned", "8", "+1")
    c3.metric("Years Coding", "3")

    st.info("Use the sidebar to explore more!")

# ---------------------------------------------------
# ABOUT ME
# ---------------------------------------------------
elif page == "👤 About Me":

    st.title("👤 About Me")

    st.header("📖 My Story")
    with st.expander("Click to read my full autobiography"):
        st.write("""
        My journey into technology started with curiosity about how apps and websites work.
        Over time, I developed skills in programming, data analysis, and problem solving.

        I enjoy building projects that make life easier and more efficient.
        """)

    st.header("🎓 Education")
    education = st.selectbox(
        "Highest Level of Education",
        ["High School", "College Undergraduate", "College Graduate"]
    )
    st.write("Selected:", education)

    st.header("🎯 Interests")
    interests = st.multiselect(
        "Select my interests",
        ["Programming", "Web Development", "AI", "Data Science", "Gaming", "Music"],
        default=["Programming", "Web Development"]
    )
    st.write("My interests:", interests)

    st.header("📅 Daily Productivity")
    hours = st.slider("Hours I code per day", 0, 12, 4)
    st.write("Coding hours:", hours)

# ---------------------------------------------------
# PORTFOLIO
# ---------------------------------------------------
elif page == "📂 Portfolio":

    st.title("📂 My Projects")

    tab1, tab2, tab3 = st.tabs(["🌐 Web App", "📊 Data Analysis", "🤖 Machine Learning"])

    with tab1:
        st.subheader("Full Stack Website")
        st.write("A responsive website with login system and database.")
        if st.button("Show Details", key="web"):
            st.success("Built using HTML, CSS, JavaScript, and Python.")

    with tab2:
        st.subheader("Sales Data Dashboard")
        st.write("Interactive data visualization project.")
        if st.button("Show Details", key="data"):
            st.success("Used Pandas, Matplotlib, and Streamlit.")

    with tab3:
        st.subheader("Prediction Model")
        st.write("Machine learning classification model.")
        if st.button("Show Details", key="ml"):
            st.success("Built using Scikit-learn.")

    st.markdown("---")

    st.subheader("📁 Upload Project File")
    uploaded = st.file_uploader("Upload documentation or screenshots")
    if uploaded:
        st.success("File uploaded successfully!")

# ---------------------------------------------------
# SKILLS DASHBOARD
# ---------------------------------------------------
elif page == "📊 Skills Dashboard":

    st.title("📊 Skills Dashboard")

    data = pd.DataFrame({
        "Skill": ["Python", "Streamlit", "SQL", "Machine Learning", "HTML/CSS"],
        "Level (%)": [90, 85, 75, 80, 70]
    })

    st.subheader("Skill Levels")
    st.dataframe(data)
    st.bar_chart(data.set_index("Skill"))

    st.subheader("📈 Random Performance Simulation")
    chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["Coding", "Learning", "Projects"])
    st.line_chart(chart_data)

    st.subheader("⚡ Productivity Simulation")
    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        progress.progress(i + 1)
    st.success("Task Completed!")

# ---------------------------------------------------
# CONTACT
# ---------------------------------------------------
elif page == "📬 Contact":

    st.title("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")

        submit = st.form_submit_button("Send Message")

        if submit:
            st.success("Message sent successfully!")

    st.subheader("⭐ Rate This Portfolio")
    rating = st.slider("Rating", 1, 5, 3)
    st.write("You rated:", rating, "⭐")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("© 2025 My Portfolio | Built with Streamlit")
