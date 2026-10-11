import streamlit as st
import json
import os

# custom helper functions
from pages.packages.exercises import *

# from pages.packages.exercises import render_overview
# from pages.packages.exercises import show_test_metadata
# from pages.packages.exercises import list_exercises
# from pages.packages.exercises import load_exercise
# from pages.packages.exercises import reset_state
# from pages.packages.exercises import grade_test
# from pages.packages.exercises import display_mc_questions
# from pages.packages.exercises import display_open_questions

# -----------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------

# def render_overview():
#     """
#         Display a brief introduction or overview of the test.
#     """
#     st.write("Test your knowledge!")


# def show_test_metadata(test):
#     """
#         Render test metadata (title, description).
#     """
#     st.subheader(test.get("title", "N/A"))
#     st.write(f"**Description:** {test.get('description', 'N/A')}")
#     # st.write(f"**Difficulty:** {test.get('difficulty', 'N/A')}")
#     st.markdown("---")


# def list_exercises(folder_path):
#     """
#         Return a list of exercise names from a folder, formatted for display.
#     """
#     exercise_names = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith(".json")]
#     return [name.replace("_", " ") for name in exercise_names]


# def load_exercise(folder_path: str, name: str):
#     """
#         Load a JSON exercise file and return it as a Python dict.
#     """
#     with open(os.path.join(folder_path, f"{name}.json"), "r") as f:
#         return json.load(f)


# def reset_state(num_questions, key_prefix):
#     """
#         Reset Streamlit session state for answers and submission flags for a new test.
#     """
#     st.session_state[f"answers_{key_prefix}"] = [None] * num_questions
#     st.session_state[f"submitted_{key_prefix}"] = False


# def grade_test(questions, answers):
#     """
#         Evaluate user answers against the correct answers and display per-question feedback.
#     """
#     score = 0
#     for i, q in enumerate(questions):
#         correct = q["answer"]
#         user = answers[i]
#         if str(user).strip() == str(correct).strip():
#             st.success(f"Q{i+1}: Correct! {correct}.")
#             score += 1
#         else:
#             st.error(f"Q{i+1}: Incorrect. The correct answer: {correct}.")
#     return score


# def display_mc_questions(questions, answers, key_prefix):
#     """
#         Render multiple-choice questions using Streamlit selectboxes.
#     """
#     for i, q in enumerate(questions):
#         with st.container():
#             st.markdown(f"### Q{i+1}: {q['question']}")
#             answers[i] = st.selectbox(
#                 "Select the correct answer!",
#                 options=q["options"],
#                 index=None,
#                 key=f"{key_prefix}_{i}",
#             )
#         st.markdown("---")


# def display_open_questions(questions, answers, key_prefix):
#     """
#         Render open-ended questions using Streamlit number input fields.
#     """
#     for i, q in enumerate(questions):
#         with st.container():
#             st.markdown(f"### Q{i+1}: {q['question']}")
#             answers[i] = st.number_input(
#                 "Enter an integer:",
#                 step=1,
#                 format="%d",   # ensures integer format
#                 key=f"{key_prefix}_{i}",
#             )
#         st.markdown("---")

# -----------------------------------------------------------
# Multiple Choice Question Logic
# -----------------------------------------------------------

def render_multiple_choice(script_dir):
    # Path to the folder containing multiple-choice exercises
    exercise_file = "combination-exercises/multiple-choice-questions"
    exercises_dir = os.path.join(script_dir, exercise_file)

    # List all exercises in the folder
    exercises = list_exercises(exercises_dir)

    # Let user select an exercise from a dropdown
    selected_exercise = st.selectbox(
        "Exercises:", exercises, index=None, placeholder="Select an exercise"
    )

    if not selected_exercise:
        return  # exit if no exercise is selected

    # Load the selected exercise as a Python dictionary
    test = load_exercise(exercises_dir, selected_exercise)
    questions = test["questions"]

    # Display test metadata (title, description, difficulty)
    show_test_metadata(test)

    # Unique key prefix for Streamlit session state variables
    key_prefix = f"mc_{selected_exercise}"

    # Initialize session state for answers if not already set
    if f"answers_{key_prefix}" not in st.session_state:
        reset_state(len(questions), key_prefix)

    # Retrieve answers from session state
    answers = st.session_state[f"answers_{key_prefix}"]

    # Render multiple-choice questions
    display_mc_questions(questions, answers, key_prefix)

    # Handle answer submission
    if st.button("Submit Your Answers", key=f"submit_mc_{key_prefix}"):
        st.session_state[f"submitted_{key_prefix}"] = True

    # Grade answers and display final score if submitted
    if st.session_state[f"submitted_{key_prefix}"]:
        score = grade_test(questions, answers)
        st.markdown(f"## Your Score: **{score}/{len(questions)}**")


# -----------------------------------------------------------
# Open Question Logic
# -----------------------------------------------------------

def render_open_questions(script_dir):
    # Path to the folder containing open-ended exercises
    exercise_file = "combination-exercises/open-questions"
    exercises_dir = os.path.join(script_dir, exercise_file)

    # List all exercises in the folder
    exercises = list_exercises(exercises_dir)

    # Let user select an exercise from a dropdown
    selected_exercise = st.selectbox(
        "Exercises:", exercises, index=None, placeholder="Select an exercise"
    )

    if not selected_exercise:
        return  # exit if no exercise is selected

    # Load the selected exercise as a Python dictionary
    test = load_exercise(exercises_dir, selected_exercise)
    questions = test["questions"]

    # Display test metadata (title, description, difficulty)
    show_test_metadata(test)

    # Unique key prefix for Streamlit session state variables
    key_prefix = f"open_{selected_exercise}"

    # Initialize session state for answers if not already set
    if f"answers_{key_prefix}" not in st.session_state:
        reset_state(len(questions), key_prefix)
    
    # Retrieve answers from session state
    answers = st.session_state[f"answers_{key_prefix}"]

    # Render open-ended questions
    display_open_questions(questions, answers, key_prefix)

    # Handle answer submission
    if st.button("Submit Your Answers", key=f"submit_open_{key_prefix}"):
        st.session_state[f"submitted_{key_prefix}"] = True

    # Grade answers and display final score if submitted
    if st.session_state[f"submitted_{key_prefix}"]:
        score = grade_test(questions, answers)
        st.markdown(f"## Your Score: **{score}/{len(questions)}**")


# -----------------------------------------------------------
# Main Application Logic
# -----------------------------------------------------------

def main():
    st.set_page_config(page_title="Combination Exercises", page_icon="", layout="wide")
    st.markdown("# Combination Exercises")

    tab1, tab2, tab3 = st.tabs(["Overview", "Multiple Choice Questions", "Open Questions"])
    script_dir = os.path.dirname(os.path.abspath(__file__))

    ### Combination Exercise tab: Overwview ###
    with tab1:
        render_overview()

    ### Combination Exercise tab: Multiple Choice Questions ###
    with tab2:
        render_multiple_choice(script_dir)
        
    ### Combination Exercise tab: Open Questions ###
    with tab3:
        render_open_questions(script_dir)

# -----------------------------------------------------------
# Entry Point
# -----------------------------------------------------------

if __name__=="__main__":
    main()



# import streamlit as st
# import json
# import os

# st.set_page_config(page_title="Combination Exercises", page_icon="⚗️", layout="wide")

# st.markdown("# Combination Exercises")

# tab1, tab2, tab3 = st.tabs(["Overview", "Multiple Choice Questions", "Open Questions"])

# with tab1:
#     st.write("Test your knowledge!")

# with tab2:
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     exercises_dir = os.path.join(script_dir, "combination-exercises/multiple-choice-questions")
#     exercise_files = [f for f in os.listdir(exercises_dir) if f.endswith(".json")]
#     exercise_names = [os.path.splitext(f)[0] for f in exercise_files]

#     selected_exercise = st.selectbox("Exercises:", exercise_names, index=None, placeholder="Select an exercise")

#     if selected_exercise:
#         json_path = os.path.join(exercises_dir, f"{selected_exercise}.json")
#         with open(json_path, "r") as file:
#             quiz = json.load(file)

#         st.subheader(quiz.get("title", "Untitled Quiz"))
#         st.write(f"**Description:** {quiz.get('description', '')}")
#         st.write(f"**Difficulty:** {quiz.get('difficulty', 'N/A')}")
#         st.markdown("---")

#         questions = quiz["questions"]

#         if "answers" not in st.session_state or st.session_state.get("exercise_loaded") != selected_exercise:
#             st.session_state.answers = [None] * len(questions)
#             st.session_state.submitted = False
#             st.session_state.exercise_loaded = selected_exercise

#         for i, q in enumerate(questions):
#             with st.container():
#                 st.markdown(f"### Q{i+1}: {q['question']}")
#                 st.session_state.answers[i] = st.selectbox(
#                     "Select the correct answer:",
#                     options=q["options"],
#                     index=None,
#                     key=f"q{i}_{selected_exercise}"
#                 )
#             st.markdown("---")

#         if st.button("Submit Quiz"):
#             st.session_state.submitted = True

#         if st.session_state.submitted:
#             score = 0
#             for i, q in enumerate(questions):
#                 user_answer = st.session_state.answers[i]
#                 correct_answer = q["answer"]

#                 if user_answer == correct_answer:
#                     st.success(f"Q{i+1}: Correct! {correct_answer}.")
#                     score += 1
#                 else:
#                     st.error(f"Q{i+1}: Incorrect. The correct answer is {correct_answer}.")

#             st.markdown(f"## Your Score: **{score} / {len(questions)}**")

# with tab3:
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     exercises_dir = os.path.join(script_dir, "combination-exercises/open-questions")
#     exercise_files = [f for f in os.listdir(exercises_dir) if f.endswith(".json")]
#     exercise_names = [os.path.splitext(f)[0] for f in exercise_files]

#     selected_exercise = st.selectbox("Exercises:", exercise_names, index=None, placeholder="Select an exercise", key="open_ex")

#     if selected_exercise:
#         json_path = os.path.join(exercises_dir, f"{selected_exercise}.json")
#         with open(json_path, "r") as file:
#             quiz = json.load(file)

#         st.subheader(quiz.get("title", "Untitled Quiz"))
#         st.markdown(f"**Description:** {quiz.get('description', '')}")
#         st.markdown(f"**Difficulty:** {quiz.get('difficulty', 'N/A')}")
#         st.markdown("---")

#         questions = quiz["questions"]

#         if "answers_open" not in st.session_state or st.session_state.get("exercise_loaded_open") != selected_exercise:
#             st.session_state.answers_open = [None] * len(questions)
#             st.session_state.submitted_open = False
#             st.session_state.exercise_loaded_open = selected_exercise

#         for i, q in enumerate(questions):
#             with st.container():
#                 st.markdown(f"### Q{i+1}: {q['question']}")
#                 st.session_state.answers_open[i] = st.text_area(
#                     "Your Answer:",
#                     value="",
#                     key=f"open_q{i}_{selected_exercise}"
#                 )
#             st.markdown("---")

#         if st.button("Submit Open Questions"):
#             st.session_state.submitted_open = True

#         if st.session_state.submitted_open:
#             score = 0
#             for i, q in enumerate(questions):
#                 user_answer = st.session_state.answers_open[i]
#                 correct_answer = q["answer"]

#                 if user_answer == str(correct_answer):
#                     st.success(f"Q{i+1}: Correct! {correct_answer}.")
#                     score += 1
#                 else:
#                     st.error(f"Q{i+1}: Incorrect. The correct answer is {correct_answer}.")

#             st.markdown(f"## Your Score: **{score} / {len(questions)}**")
