import streamlit as st
import json
import os

def render_overview():
    """
        Display a brief introduction or overview of the test.
    """
    st.write("Test your knowledge!")


def show_test_metadata(test):
    """
        Render test metadata (title, description).
    """
    st.subheader(test.get("title", "N/A"))
    st.write(f"**Description:** {test.get('description', 'N/A')}")
    # st.write(f"**Difficulty:** {test.get('difficulty', 'N/A')}")
    st.markdown("---")


def list_exercises(folder_path):
    """
        Return a list of exercise names from a folder, formatted for display.
    """
    exercise_names = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith(".json")]
    return [name.replace("_", " ") for name in exercise_names]


def load_exercise(folder_path: str, name: str):
    """
        Load a JSON exercise file and return it as a Python dict.
    """
    with open(os.path.join(folder_path, f"{name}.json"), "r") as f:
        return json.load(f)


def reset_state(num_questions, key_prefix):
    """
        Reset Streamlit session state for answers and submission flags for a new test.
    """
    st.session_state[f"answers_{key_prefix}"] = [None] * num_questions
    st.session_state[f"submitted_{key_prefix}"] = False


def grade_test(questions, answers):
    """
        Evaluate user answers against the correct answers and display per-question feedback.
    """
    score = 0
    for i, q in enumerate(questions):
        correct = q["answer"]
        user = answers[i]
        if str(user).strip() == str(correct).strip():
            st.success(f"Q{i+1}: Correct! {correct}.")
            score += 1
        else:
            st.error(f"Q{i+1}: Incorrect. The correct answer: {correct}.")
    return score


def display_mc_questions(questions, answers, key_prefix):
    """
        Render multiple-choice questions using Streamlit selectboxes.
    """
    for i, q in enumerate(questions):
        with st.container():
            st.markdown(f"### Q{i+1}: {q['question']}")
            answers[i] = st.selectbox(
                "Select the correct answer!",
                options=q["options"],
                index=None,
                key=f"{key_prefix}_{i}",
            )
        st.markdown("---")


def display_open_questions(questions, answers, key_prefix):
    """
        Render open-ended questions using Streamlit number input fields.
    """
    for i, q in enumerate(questions):
        with st.container():
            st.markdown(f"### Q{i+1}: {q['question']}")
            answers[i] = st.number_input(
                "Enter an integer:",
                step=1,
                format="%d",   # ensures integer format
                key=f"{key_prefix}_{i}",
            )
        st.markdown("---")