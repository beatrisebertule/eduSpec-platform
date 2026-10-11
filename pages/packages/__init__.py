from .molecules import (
    set_page_conf as molecules_page_conf,
    load_exercises,
    show_test_metadata as molecules_metadata,
    display_questions,
    set_sidebar_conf,
    render_smiles,
    grade_test as molecules_grade_test,
)

from .exercises import (
    render_overview,
    list_exercises,
    load_exercise,
    reset_state,
    display_mc_questions,
    display_open_questions,
    grade_test as exercises_grade_test,
    show_test_metadata as exercises_metadata,
)

from .spectroscopy import (
    set_page_conf as spectroscopy_page_conf,
    generate_data,
    create_plot,
    display_selected_point,
    reset_data,
)

__all__ = [
    # molecules
    "molecules_page_conf",
    "load_exercises",
    "molecules_metadata",
    "display_questions",
    "set_sidebar_conf",
    "render_smiles",
    "molecules_grade_test",

    # exercises
    "render_overview",
    "list_exercises",
    "load_exercise",
    "reset_state",
    "display_mc_questions",
    "display_open_questions",
    "exercises_grade_test",
    "exercises_metadata",

    # spectroscopy
    "spectroscopy_page_conf",
    "generate_data",
    "create_plot",
    "display_selected_point",
    "reset_data",
]
