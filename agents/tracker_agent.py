from utils.groq_client import get_client

client = get_client()

def analyze_progress(subject, completed, total, weak_topics):
    progress = (completed / total) * 100

    prompt = f"""
    Subject: {subject}

    Progress: {progress:.2f}%
    Weak topics: {weak_topics}

    Analyze the student's progress and give:
    - Performance feedback
    - What to improve
    - Study strategy for next days
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return progress, response.choices[0].message.content