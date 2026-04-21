import streamlit as st
import os

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="AI Study Copilot", layout="wide")

# ---------- STYLE ----------
st.markdown("""
<style>
body {
    background-color: #0f172a;
}
.card {
    background: #1e293b;
    padding: 18px;
    border-radius: 14px;
    margin-bottom: 12px;
    color: white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.3);
}
.title {
    font-size: 36px;
    font-weight: bold;
}
.subtitle {
    color: gray;
    margin-bottom: 20px;
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
st.sidebar.write(f"🔥 Progress: {int(progress*100)}%")

weak_topics = st.sidebar.text_input("Weak Topics (comma separated)")

# ---------- HEADER ----------
st.markdown("<div class='title'>🚀 AI Study Copilot</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Plan smarter. Study better.</div>", unsafe_allow_html=True)

# ---------- GENERATE BUTTON ----------
if "plan_generated" not in st.session_state:
    st.session_state.plan_generated = False

if st.button("Generate Study Plan"):
    st.session_state.plan_generated = True

# ---------- STUDY CARDS ----------
def study_card(time, title, desc, key):
    st.markdown(f"""
    <div class="card">
        <h4>⏰ {time}</h4>
        <h5>{title}</h5>
        <p>{desc}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(f"✅ Mark Done ({time})", key=key):
        st.success(f"{title} completed!")

# ---------- PLAN DISPLAY ----------
if st.session_state.plan_generated:

    st.subheader("📅 Today's Plan")

    study_card("9:00 - 9:30", "Introduction", "Overview of DBMS concepts", "c1")
    study_card("9:30 - 12:00", "Deep Study", "ER models, Keys, Normalization", "c2")
    study_card("1:00 - 2:00", "Practice", "Solve SQL queries", "c3")
    study_card("2:30 - 4:00", "Revision", "Revise weak topics", "c4")
    study_card("4:00 - 5:00", "Final Review", "Mock test", "c5")

# ---------- CHAT SECTION ----------
st.markdown("---")
st.subheader("💬 Ask AI")

user_input = st.text_input("Ask something...")

def get_ai_response(prompt):
    try:
        from groq import Groq
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return "⚠️ Error: Check API key or connection"

if user_input:
    reply = get_ai_response(user_input)
    st.markdown(f"**🤖 AI:** {reply}")