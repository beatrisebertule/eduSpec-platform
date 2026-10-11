import streamlit as st

def main():
    st.set_page_config(
        page_title="General Information",
        page_icon="",
        layout="wide",
    )

    st.write("# General Information")

    st.sidebar.success("Select a subcategory above!")

    st.markdown(
        """
        Infromation of how to use and navigate through the edcuation platform.
        """
    )

if __name__=="__main__":
    main()