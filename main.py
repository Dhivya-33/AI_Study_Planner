from agents.planner_agent import create_study_plan
from agents.tracker_agent import analyze_progress
from agents.revision_agent import generate_revision_plan

def main():
    subject = input("Enter subject: ")
    days = int(input("Enter number of days: "))

    plan = create_study_plan(subject, days)
    print("\n📚 STUDY PLAN:\n", plan)

    completed = int(input("\nTopics completed: "))
    total = int(input("Total topics: "))
    weak_topics = input("Enter weak topics (comma separated): ")

    progress, analysis = analyze_progress(subject, completed, total, weak_topics)

    print(f"\n Progress: {progress:.2f}%")
    print("\n AI FEEDBACK:\n", analysis)

    revision = generate_revision_plan(subject, weak_topics)

    print("\n🔁 REVISION PLAN:\n", revision)

if __name__ == "__main__":
    main()