import streamlit as st

st.set_page_config(page_title="AI Study Copilot", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
body {background-color: #0f172a;}
.card {
    background: #1e293b;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
    color: white;
}
.title {
    font-size: 28px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
st.sidebar.title("📘 Study Setup")

subject = st.sidebar.text_input("Subject", "DBMS")
days = st.sidebar.number_input("Days", 1)
completed = st.sidebar.number_input("Completed Topics", 0)
total = st.sidebar.number_input("Total Topics", 5)

progress = completed / total if total else 0
st.sidebar.progress(progress)
st.sidebar.write(f"Progress: {int(progress*100)}%")

# ---------- HEADER ----------
st.markdown("<div class='title'>🚀 AI Study Copilot</div>", unsafe_allow_html=True)
st.write("Plan smarter. Study better.")

# ---------- GENERATE ----------
if st.button("Generate Study Plan"):

    st.subheader("📅 Today's Plan")

    def card(time, title, desc):
        st.markdown(f"""
        <div class="card">
            <h4>⏰ {time}</h4>
            <b>{title}</b>
            <p>{desc}</p>
        </div>
        """, unsafe_allow_html=True)

    card("9:00 - 9:30", "Introduction", "Overview of DBMS concepts")
    card("9:30 - 12:00", "Deep Study", "ER models, Keys, Normalization")
    card("1:00 - 2:00", "Practice", "Solve SQL queries")
    card("2:30 - 4:00", "Revision", "Revise weak topics")
    card("4:00 - 5:00", "Final Review", "Mock test")

# ---------- CHAT ----------
st.subheader("💬 Ask AI")

user_input = st.text_input("Ask something...")

if user_input:
    st.write("🤖 AI:", "This is where Groq response will come")