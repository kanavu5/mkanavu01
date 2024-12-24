import streamlit as st

def main():
   
    st.sidebar.image("banner.jpg", use_column_width=True)
    # Add a sidebar for navigation
    page = st.sidebar.selectbox("Select a page", ["Home", "Collage"])
  

    

    if page == "Home":
        home_page()
    elif page == "Collage":
        collage_page()

if __name__ == "__main__":
    main()
  
st.title("Hello, World!")
st.write("This is a simple Streamlit app showing Hello, World!")
