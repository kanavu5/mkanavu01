import streamlit as st

def main():
   
 
    # Add a sidebar for navigation
    page = st.sidebar.selectbox("Select a page", ["Home", "Collage"])
  

    

   

if __name__ == "__main__":
    main()
  
st.title("Hello, World!")
st.write("This is a simple Streamlit app showing Hello, World!")
