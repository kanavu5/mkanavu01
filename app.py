import streamlit as st
from home import home


def main():
   
 
    # Add a sidebar for navigation
    page = st.sidebar.selectbox("Select a page", ["Home", "Collage"])
  
    

    if page == "Home":
        home()
    elif page == "Collage":
        home()
    

   

if __name__ == "__main__":
    main()
  
st.title("Hello, World!")
st.write("This is a simple Streamlit app showing Hello, World!")
