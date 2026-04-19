from utils.groq_client import get_client

client = get_client()

def generate_revision_plan(subject, weak_topics):
    prompt = f"""
    Create a smart revision plan for {subject}.

    Focus more on weak topics: {weak_topics}

    Use:
    - Spaced repetition
    - Daily revision slots
    - Quick recall techniques

    Give a structured plan.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content