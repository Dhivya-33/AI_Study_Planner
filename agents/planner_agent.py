from utils.groq_client import get_client

client = get_client()

def create_study_plan(subject, days):
    prompt = f"""
    Create a {days}-day structured study plan for {subject}.
    Include:
    - Daily topics
    - Time allocation
    - Revision schedule
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content