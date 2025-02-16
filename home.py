import streamlit as st
import pandas as pd
import json
import requests

def home():
    # Add a banner image
   
    st.page_link("https://neet.nta.nic.in/", label="All About NEET", icon="🌎")
    st.page_link("https://cetonline.karnataka.gov.in/kea/", label="All About KEA", icon="📚")
    