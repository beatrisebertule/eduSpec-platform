# eduSpec 3.0 Streamlit

## Run eduSpec Streamlit Locally

Run eduSpec app within a Python virtual environment on a Unix system (Linux/macOS).

0. Check Python version (>3.11):
```
python3 --version
``` 

1. Create a new virtual environment:
```
cd eduSpec-streamlit
python3 -m venv .venv
```

2. Activate the virtual environment:
```
source .venv/bin/activate
```

3. Install dependancies:
```
pip install --no-cache-dir -r requirements.txt
```

4. Launch the application:
```
streamlit run General_Information.py
```

5. Deactive the virtual environment once done:
```
deactivate
```

---

## Run eduSpec Streamlit on Docker

Run eduSpec on Docker:

```
cd eduSpec-Streamlit
docker compose up --build
```

---

## General Structure

```
.
├── pages/
|   ├── combination-exercises/            # JSON files for combination (multiple choice and open) exercises
|   |   └── ...
|   ├── molecule-exercises/               # JSON files for molecule structure exercises
|   |   └── ...
│   ├── 1_Molecule_Editor_Demo.py         # page logic for molecule editor exercises
|   ├── 2_Combination_Exercises_Demo.py   # page logic for combination exercises
│   ├── 3_Spectroscopy_Demo.py            # page logic for spectroscopy exercises
│   └── ...                
├──  General_Information.py               # main page 
└── ...

```

The core files that define the structure of the current web application are:

- `Gnereal_Information.py`
- `pages/1_Molecule_Editor_Demo.py`
- `pages/2_Combination_Exercises_Demo.py`
- `pages/3_Spectroscopy_Demo.py`


`1_General_Information.py` is the main page of the eduSpec 3.0 application. It provides an overall description of the platform.

All other pages are located under the `pages` directory. Currently, there are three pages:

- `pages/1_Molecule_Editor_Demo.py`
- `pages/2_Combination_Exercises_Demo.py`
- `pages/3_Spectroscopy_Demo.py`

**Note:**

- Page titles are derived from the filenames. For example, `1_Molecule_Editor_Demo.py` becomes **Molecule Editor Demo**.
- The numeric prefix determines the sequence in which pages are displayed. If removed, pages are sorted alphabetically.
- Each page contains all the logic for that page, including helper functions. For simplicity, helper functions are kept in the same file rather than separate modules.

---

## Exercise JSON File Structure

Exercise files are stored as follows:

- Multiple Choice Questions:

    `pages/combination-exercises/multiple-choice-questions/...`

- Open Questions Questions:

    `pages/combination-exercises/open-questions/...`

- Molecule Draw Questions:

    `pages/molecule-exercises/...`

All exercise files share a similar format:

```json
{
  "title": "title",
  "description": "description",
  "questions": [
    {
      "question": "question",
      "options": ["options"],
      "answer": "answer"
    }
  ]
}
```

The format includes the metadata of a particual exercise (title, description) and the questions (with options and/or answers).

---

## JSME Custom Component

The JSME respoitry was pulled from [JSME GitHub repository] https://github.com/jsme-editor/jsme-editor.github.io/tree/main/dist.  

### Custom Component Directory Structure

```
pages/
├── jsme_component/
│   └── __init__.py            # the custom component module
├── frontend/
│   ├── jsme/                  # all the necessary files to render JSME (pulled from GitHub)
│   ├── index.html             # render logic of the molecule editor
│   ├── index.js               # JS logic for the component
│   └── streamlit-comp-lib.js  # streamlit custom component wrapper
└── ...
```

---

## Other Custom Components
The directory `packages` contains some custom python packages. These packages contain helper function used for each page.

```
packages/
├── __init__.py
├── exercises.py.py
├── molecules.py
└── spectroscopy.py
```

For example, package `molecules.py` comntains all the helper fuinction used within page `1_Molecule_Editor_Demo.py`.

