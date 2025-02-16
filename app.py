import streamlit as st
from home import home
from cutoff_page import cutoff
from collegelist import collagelist

# Set the page layout to wide
st.set_page_config(page_title='Snowflake', layout='wide')

def main():
    # Display the image and title side by side
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("./logo.png", width=150)
    with col2:
        st.title("Kanavu Meipada Vendum")
        st.markdown("""
                Let your dreams come true! 🌨️   
                 """)


    _, exp_col, _ = st.columns([1,3,1])
    with exp_col:
        with st.expander("**📖  About This Website**"):
            st.markdown("""
                        This website is designed to assist students by providing valuable admission-related information for medical colleges, including details on previous years’ cutoffs. The information presented here is gathered from various reliable sources to serve as a guidance tool for aspiring students.

                        While we strive to offer accurate and helpful insights, we strongly recommend that students verify the latest updates from official sources before making any decisions. Our goal is to simplify the admission process by making crucial data easily accessible, helping students make informed choices about their medical careers.

                        Stay informed, plan wisely, and achieve your dreams
                        """)
        

        # Add a sidebar for navigation
        page = st.sidebar.selectbox("Select a page", ["Home", "Collage", "Cutoff"])
  
    if page == "Home":
        home()
    elif page == "Collage":
        collagelist()
    elif page == "Cutoff":
        cutoff()
    
if __name__ == "__main__":
    main()

