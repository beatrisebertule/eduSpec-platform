import streamlit as st
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as pxd

def set_page_conf(page_title_conf, page_title):
    st.set_page_config(page_title=page_title_conf, page_icon="", layout="wide")
    st.markdown(page_title)

def generate_data():
    # initialize session data if not present
    if 'data' not in st.session_state:
        last_rows = np.random.randn(1, 1)  # starting row
        for _ in range(20):  # generate multiple rows with cumulative sum
            new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
            last_rows = np.vstack([last_rows, new_rows])
        st.session_state.data = last_rows.flatten()  # store flattened data in session

    x_coords = np.arange(len(st.session_state.data))  # generate x coordinates
    y_coords = st.session_state.data  # y coordinates from session data
    return x_coords, y_coords  # return coordinates

def create_plot(x_coords, y_coords):
    fig = go.Figure()  # initialize figure

    # add scatter trace with lines and markers
    fig.add_trace(go.Scatter(
        x=x_coords,
        y=y_coords,
        mode='lines+markers',
        name='Clickable Data',
        line=dict(color='green', width=1),
        marker=dict(size=8, color='orange'),
        customdata=x_coords  # store x coordinates in custom data
    ))

    # update layout with axis titles and hover mode
    fig.update_layout(
        xaxis_title="X Values",
        yaxis_title="Y Values",
        hovermode="x unified",
        height=400
    )

    return fig  # return figure

def display_selected_point(event):
    st.subheader("Your Selected Point")  # display section header
    point_coordinates = ""  # initialize variable
    # check if a point was selected
    if event and event.selection and event.selection.points:
        clicked_point = event.selection.points[0]  # get first selected point
        point_coordinates = f"({clicked_point['x']}, {clicked_point['y']:.3f})"
        st.code(point_coordinates if point_coordinates else "No point coordinates available")  # show coordinates
    else:
        st.info("Select a point to retrieve its coordinates!")  # instruction if no point selected

def reset_data():
    last_rows = np.random.randn(1, 1)  # starting row for new data
    for _ in range(20):  # generate multiple rows with cumulative sum
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        last_rows = np.vstack([last_rows, new_rows])
    st.session_state.data = last_rows.flatten()  # store new data in session
    st.rerun()  # rerun app to reflect new data