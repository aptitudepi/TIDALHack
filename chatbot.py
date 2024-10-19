import streamlit as st

# Streamlit App: Chatbot UI

# Add title with an icon
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🩺 Medical Chatbot for Symptom Diagnosis</h1>", unsafe_allow_html=True)

# Add a welcome message and instructions
st.markdown("""
    <div style='text-align: center;'>
        <p style='font-size: 18px;'>This chatbot will guide you through describing your symptoms, and it will predict the likely disease you may be dealing with.</p>
        <p style='font-size: 18px;'>Please enter the symptoms you're experiencing, and we'll provide you with a possible diagnosis.</p>
    </div>
    <hr style="border: none; height: 2px; background-color: #4CAF50;">
""", unsafe_allow_html=True)

# Create a clean input box for symptoms
symptoms = st.text_area("📝 Describe the symptoms you are feeling below:", placeholder="e.g., fever, sore throat, headache", height=150)

# Custom styled button
button_html = """
    <style>
    div.stButton > button:first-child {
        background-color: #4CAF50;
        color: white;
        padding: 10px 24px;
        font-size: 18px;
        border-radius: 12px;
        border: none;
    }
    div.stButton > button:first-child:hover {
        background-color: #45a049;
        color: white;
    }
    </style>
"""
st.markdown(button_html, unsafe_allow_html=True)

# Submit button (without model logic)
if st.button("Submit Symptoms"):
    if symptoms:
        st.write("🤔 Processing your symptoms... (Model coming soon!)")
    else:
        st.warning("Please enter symptoms before clicking submit.")
