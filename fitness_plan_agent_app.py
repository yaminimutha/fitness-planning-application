"""
Personalized Fitness-Plan Generation Agent — starter prototype
Student: Mutha Bhavani | ID: 23ME1A5492

This is a transparent, rule-based prototype demonstrating the agent workflow:
input validation -> goal analysis -> plan drafting -> constraint checks -> display.
It does NOT connect to a Generative AI model yet and does not provide medical advice.
Replace the plan_draft() function with a selected model/provider integration only after
documenting the model, prompts, safety checks, and API configuration.
Run:
    pip install streamlit
    streamlit run fitness_plan_agent_app.py
"""
import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Personal Fitness Plan Agent", page_icon="🏃", layout="centered")
st.title("Personalized Fitness-Plan Generation Agent")
st.caption("General wellness planning prototype — not medical advice.")

GOAL_OPTIONS = ["Build consistency", "Improve general fitness", "Increase daily activity", "Improve strength"]
ACTIVITY_OPTIONS = ["Walking", "Bodyweight exercise", "Cycling", "Yoga / mobility", "Light cardio"]

def validate_input(goal, days, duration, experience, equipment):
    errors = []
    if not goal:
        errors.append("Please select a goal.")
    if not days:
        errors.append("Choose at least one available day.")
    if not 10 <= duration <= 90:
        errors.append("Session duration must be between 10 and 90 minutes.")
    if not experience:
        errors.append("Select an experience level.")
    if not equipment:
        errors.append("Choose at least one activity or equipment preference.")
    return errors

def analyze_goal(goal, experience, days, duration, equipment):
    return {
        "goal": goal,
        "experience": experience,
        "days": list(days),
        "duration": int(duration),
        "preferences": list(equipment),
    }

def plan_draft(profile):
    """Simple deterministic baseline. Replace with a model-backed generator later."""
    preferred = profile["preferences"]
    schedule = {}
    session_pool = {
        "Build consistency": ["Walking", "Bodyweight exercise", "Yoga / mobility"],
        "Improve general fitness": ["Walking", "Light cardio", "Bodyweight exercise"],
        "Increase daily activity": ["Walking", "Cycling", "Yoga / mobility"],
        "Improve strength": ["Bodyweight exercise", "Walking", "Yoga / mobility"],
    }
    pool = [item for item in session_pool.get(profile["goal"], []) if item in preferred]
    if not pool:
        pool = preferred
    for idx, day in enumerate(profile["days"]):
        activity = pool[idx % len(pool)]
        schedule[day] = {
            "activity": activity,
            "duration_minutes": profile["duration"],
            "notes": "Keep the effort comfortable; stop if you feel pain, dizziness, or unusual shortness of breath."
        }
    all_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in all_days:
        if day not in schedule:
            schedule[day] = {
                "activity": "Rest / optional gentle movement",
                "duration_minutes": 0,
                "notes": "Rest day; optional easy movement only if comfortable."
            }
    return schedule

def validate_plan(schedule, profile):
    problems = []
    if set(profile["days"]) - set(schedule.keys()):
        problems.append("One or more selected days are missing.")
    for day, item in schedule.items():
        if item["duration_minutes"] > profile["duration"]:
            problems.append(f"{day} exceeds the requested session duration.")
        if not item["activity"]:
            problems.append(f"{day} has no activity label.")
    return problems

with st.form("fitness_profile"):
    st.subheader("1. Your preferences")
    goal = st.selectbox("Main goal", GOAL_OPTIONS)
    experience = st.selectbox("Experience level", ["Beginner", "Returning after a break", "Regularly active"])
    days = st.multiselect(
        "Days available",
        ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        default=["Monday", "Wednesday", "Friday"]
    )
    duration = st.slider("Preferred session duration (minutes)", 10, 90, 30, step=5)
    equipment = st.multiselect("Preferred activities / available options", ACTIVITY_OPTIONS,
                               default=["Walking", "Bodyweight exercise"])
    submitted = st.form_submit_button("Generate weekly plan")

if submitted:
    errors = validate_input(goal, days, duration, experience, equipment)
    if errors:
        st.error("Please correct the following:")
        for err in errors:
            st.write(f"- {err}")
    else:
        profile = analyze_goal(goal, experience, days, duration, equipment)
        with st.spinner("Preparing and checking your plan..."):
            draft = plan_draft(profile)
            problems = validate_plan(draft, profile)
        st.subheader("2. Weekly plan")
        if problems:
            st.warning("The plan needs review:")
            for problem in problems:
                st.write(f"- {problem}")
        else:
            st.success("Basic application checks passed. This does not establish medical suitability.")
        st.write(f"**Goal:** {profile['goal']}  |  **Experience:** {profile['experience']}")
        st.write(f"**Generated at:** {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]:
            item = draft[day]
            with st.expander(f"{day}: {item['activity']} ({item['duration_minutes']} min)", expanded=True):
                st.write(item["notes"])
        st.info("This prototype uses deterministic rules, not a Generative AI model. It is for project demonstration only.")
        st.caption("If you have a medical condition, injury, or special dietary need, consult a qualified professional.")
