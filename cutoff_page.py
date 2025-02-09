import streamlit as st
import pandas as pd
import json
import requests
import sys
import os
from cryptography.fernet import Fernet

def cutoff():
    st.title("Cutoff Page")
    st.write("This is the Cutoff page.")
    # Add more content and functionality for the Cutoff page here

    try:
        # Load JSON data
        url = st.secrets["data"]["data_url_ENC"]
        response = requests.get(url)
        # data = response.json()

        with open("data.json.enc", "rb") as f:
            encrypted_data = f.read()

        print(response.content)


        print("New Data ------------------------------------------------------------------------------------------------")

        print(encrypted_data)

        encrypted_data_str = response.content


        """Decrypt a file."""
        key = open("secret.key", "rb").read()
        #print(key)
        fernet = Fernet(key)
        
        #encrypted_data = response.content
        #print(encrypted_data)
        #encrypted_data_str = encrypted_data.decode('utf-8')
        #print(encrypted_data_str)
        decrypted_data = fernet.decrypt(encrypted_data_str)


       
        data = json.loads(decrypted_data)
  
        # Convert JSON data to DataFrame
        df = pd.DataFrame(data)
        
        # Capitalize column titles
        df.columns = [col.upper() for col in df.columns]

        # Add three columns for filtering
        col1, col2, col3 = st.columns(3)
        with col1:
            district_filter = st.selectbox("Filter by District", options=["All"] + df["DISTRICT"].unique().tolist())
        with col2:
            type_filter = st.selectbox("Filter by Type", options=["All"] + df["TYPE"].unique().tolist())
        with col3:
            category_filter = st.selectbox("Filter by Category", options=["All"] + df["CATEGORY"].unique().tolist())

        # Apply filters
        if district_filter != "All":
            df = df[df["DISTRICT"] == district_filter]
        if type_filter != "All":
            df = df[df["TYPE"] == type_filter]
        if category_filter != "All":
            df = df[df["CATEGORY"] == category_filter]
        
        # Search and sort functionality in the same row
        col1, col2 = st.columns(2)
        with col1:
            search_query = st.text_input("Search")
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
