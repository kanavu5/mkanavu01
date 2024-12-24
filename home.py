import streamlit as st
import pandas as pd
import json

def home():
    # Add a banner image
    st.title("Kanavu Meipada Vendum")
    
    try:
        # Load JSON data
        url = 'https://raw.githubusercontent.com/kanavu5/mkanavu01/refs/heads/main/university.json'
        response = requests.get(url)
        data = response.json()
        
        # Convert JSON data to DataFrame
        df = pd.DataFrame(data)
        
        # Capitalize column titles
        df.columns = [col.upper() for col in df.columns]
        
        # Search and sort functionality in the same row
        col1, col2 = st.columns(2)
        with col1:
            search_query = st.text_input("Search by country name")
        with col2:
            sort_by = st.selectbox("Sort by", options=df.columns)
            sort_order = st.radio("Sort order", options=["Ascending", "Descending"], horizontal=True)
        
        if search_query:
            df = df[df['COUNTRY'].str.contains(search_query, case=False, na=False)]
        
        df = df.sort_values(by=sort_by, ascending=(sort_order == "Ascending"))
        
        # Pagination
        records_per_page = 10
        total_pages = (len(df) - 1) // records_per_page + 1
        page = st.number_input('Page', min_value=1, max_value=total_pages, step=1)
        
        start_idx = (page - 1) * records_per_page
        end_idx = start_idx + records_per_page
        df_page = df.iloc[start_idx:end_idx]
        
        # Display DataFrame as a table without row numbers
        st.table(df_page.reset_index(drop=True))
    except FileNotFoundError:
        st.error("The file 'data.json' was not found.")
    except json.JSONDecodeError:
        st.error("Error decoding JSON from the file 'data.json'.")
    except ValueError:
        st.error("Error converting JSON data to DataFrame.")
