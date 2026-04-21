import streamlit as st
from agents.planner_agent import create_study_plan
from agents.tracker_agent import analyze_progress
from agents.revision_agent import generate_revision_plan

st.set_page_config(page_title="AI Study Planner", layout="wide")

st.title("📚 AI Study Planner & Tracker")

# --- SIDEBAR INPUT ---
st.sidebar.header("Enter Details")

subject = st.sidebar.text_input("Subject")
days = st.sidebar.number_input("Number of Days", min_value=1, step=1)

completed = st.sidebar.number_input("Topics Completed", min_value=0, step=1)
total = st.sidebar.number_input("Total Topics", min_value=1, step=1)

weak_topics = st.sidebar.text_input("Weak Topics (comma separated)")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📚 Planner", "📊 Tracker", "🔁 Revision"])

# ------------------ TAB 1: STUDY PLAN ------------------
with tab1:
    st.header("📚 Study Planner")

    if st.button("Generate Study Plan"):
        if subject and days:
            with st.spinner("Generating Study Plan..."):
                plan = create_study_plan(subject, days)
                st.write(plan)
        else:
            st.warning("Enter subject and days")

# ------------------ TAB 2: TRACKER ------------------
with tab2:
    st.header("📊 Progress Tracker")

    if st.button("Analyze Progress"):
        if total > 0:
            with st.spinner("Analyzing Progress..."):
                progress, analysis = analyze_progress(subject, completed, total, weak_topics)

                st.progress(int(progress))
                st.write(f"**Progress:** {progress:.2f}%")

                st.subheader("🤖 AI Feedback")
                st.write(analysis)
        else:
            st.warning("Enter valid topic values")

# ------------------ TAB 3: REVISION ------------------
with tab3:
    st.header("🔁 Revision Planner")

    if st.button("Generate Revision Plan"):
        if weak_topics:
            with st.spinner("Generating Revision Plan..."):
                revision = generate_revision_plan(subject, weak_topics)
                st.write(revision)
        else:
            st.warning("Enter weak topics")