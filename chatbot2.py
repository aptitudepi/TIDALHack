#!/usr/bin/env python3
# Your Name

import streamlit as st
from joblib import load

def main():
    # Set page layout to "centered"
    st.set_page_config(layout="wide")

    """
    # Medical Chatbot for Symptom Diagnosis

    This medical chatbot is designed to assist users in diagnosing their symptoms. It provides a user-friendly interface for inputting symptoms and receiving preliminary diagnostic information. The chatbot utilizes advanced natural language processing and machine learning algorithms to analyze the provided symptoms and generate potential diagnoses.

    Our goal is to make preliminary medical information more accessible to users, helping them make informed decisions about seeking professional medical care. However, it's important to note that this chatbot is not a substitute for professional medical advice, diagnosis, or treatment. Always consult with a qualified healthcare provider for any medical concerns.

    """

    # Store user's name in session state to keep track
    if "name" not in st.session_state:
        st.session_state["name"] = ""

    # Check if the user has already submitted their name
    if st.session_state["name"]:
        st.markdown(f"## Welcome, {st.session_state['name']}!")
        st.markdown("Please describe your symptoms below:")

        symptoms = st.text_area("", placeholder="e.g., fever, sore throat, headache", height=150)

        if st.button("Submit Symptoms"):
            if symptoms:
                st.markdown(f"Processing symptoms for {st.session_state['name']}... (Model coming soon!)")
                model = load("20241019-DiseasePredictionModelDump.joblib")
                process(symptoms)
                
            else:
                st.warning(f"{st.session_state['name']}, please enter symptoms before clicking submit.")
    else:
        st.markdown("## Please enter your name to begin:")
        name_input = st.text_input("Your Name:", placeholder="Enter your name")

        if st.button("Submit Name"):
            if name_input:
                st.session_state["name"] = name_input



    
if __name__ == "__main__":
    main()