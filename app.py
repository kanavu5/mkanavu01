import streamlit as st

def main():
   
 
    # Add a sidebar for navigation
    page = st.sidebar.selectbox("Select a page", ["Home", "Collage"])
  
    

    if page == "Home":
        home_page()
    elif page == "Collage":
        home_page()
    

   

if __name__ == "__main__":
    main()
  
st.title("Hello, World!")
st.write("This is a simple Streamlit app showing Hello, World!")
