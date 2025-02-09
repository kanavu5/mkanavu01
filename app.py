import streamlit as st
from home import home
from cutoff_page import cutoff

# Set the page layout to wide
st.set_page_config(layout="wide")

def main():
    # Add a sidebar for navigation
    page = st.sidebar.selectbox("Select a page", ["Home", "Collage", "Cutoff"])
  
    if page == "Home":
        home()
    elif page == "Collage":
        home()
    elif page == "Cutoff":
        cutoff()
    
if __name__ == "__main__":
    main()

