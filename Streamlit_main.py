import streamlit as st
from RAG_core import RAG_main
import requests

st.set_page_config(page_title="Aarini App", layout="wide")
rag = RAG_main()
st.title("Aarini Question Answer App")

with st.form(key="query_form"):
    query = st.text_input("Enter Your question here")
    submit_button = st.form_submit_button(label="Submit")   
    
if submit_button and query:
    with st.spinner("Fetching response..."):
        #response = rag.RAG_function(query)
        response = requests.post("http://127.0.0.1:8000/rag/query", 
                                 json={"query":query})
        if response.ok:
            st.markdown("### Answer:")
            st.write(response.json().get("response"))
        else:
            st.error("Error fetching response. Please try again later.")
        
        #st.write(response)
