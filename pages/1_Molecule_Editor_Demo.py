import streamlit as st
import json
import os

# load the Streanlit Custom Component JSME 
from pages.jsme_component import jsme_component
# custom helper function
from pages.packages.molecules import *

# -----------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------

# def set_page_conf(page_title_conf, page_title):
#     """
#         Configure the Streamlit page (title, layout, sidebar label).
#     """
#     st.set_page_config(page_title=page_title_conf, page_icon="", layout="wide")
#     st.markdown(page_title)

# def load_exercises(path):
#     """
#         Load a JSON exercise file and return it as a Python dict.
#     """
#     script_dir = os.path.dirname(os.path.abspath(__file__))
#     json_path = os.path.join(script_dir, path)
#     with open(json_path, "r") as file:
#         return json.load(file)

# def show_test_metadata(test):
#     """
#         Render general test metadata (title, description).
#     """
#     st.subheader(test.get("title", "N/A"))
#     st.write(f"**Description:** {test.get('description', 'N/A')}")
#     st.markdown("---")

# def display_questions(test):
#     """
#         Display the questions from the test and return its data dict.
#     """
#     question_data = test["questions"][0]  # show only the 1st question for now
#     st.write(f"{question_data['question']}")
#     return question_data

# def set_sidebar_conf(seed):
#     """
#         Render sidebar configuration and return the default SMILES input value.
#     """
#     st.sidebar.header("Configuration")
#     default_smiles = st.sidebar.text_input(
#         "Default SMILES",
#         value=seed,
#         help="Enter a SMILES string to load initially"
#     )
#     return default_smiles

# def render_smiles(molecule_data):
#     """
#         Display the SMILES string from the molecule editor and return it.
#     """
#     smiles = ""
#     if molecule_data:
#         smiles = molecule_data.get("smiles", "")
#         st.subheader("Your Drawn SMILES")
#         st.code(smiles if smiles else "No SMILES available")
#     else:
#         st.info("Draw a molecule in the editor above to see its SMILES code here!")
#     return smiles

# def grade_test(smiles, test):
#     """
#         Compare the submitted SMILES against the correct answer and display feedback.
#     """
#     question_data = test["questions"][0]
#     correct_answer = question_data["answer"].strip()
#     if smiles.strip() == correct_answer:
#         st.success(f"Correct! The answer is {correct_answer}.")
#     else:
#         st.error(f"Incorrect. The correct answer is {correct_answer}.")

# -----------------------------------------------------------
# Main Application Logic
# -----------------------------------------------------------

def main():
    page_title_conf = "JSME Molecule Editor" # page title
    page_title = "# JSME Molecule Editor" # markdown header

    set_page_conf(page_title_conf, page_title)

    # Load exercises from JSON
    exercise_file = "../molecule-exercises/molecule-question.json"
    test = load_exercises(exercise_file)

    # Show metadata of the test
    # show_test_metadata(test)

    # Display questions
    display_questions(test)

    # Set sidebar configurations
    seed = "N[CH](C)C(=O)O"
    default_smiles = set_sidebar_conf(seed)

    # Load the JSME molecule editor, pass default (seed) SMILES
    molecule_data = jsme_component(default_smiles=default_smiles, key="jsme_editor")

    # Show SMILES
    smiles = render_smiles(molecule_data)

    # Grade only when a SMILES code non-empty and an answer submitted
    if smiles and st.button("Submit Answer"):
        grade_test(smiles, test)

# -----------------------------------------------------------
# Entry Point
# -----------------------------------------------------------

if __name__ == "__main__":
    main()
