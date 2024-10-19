import streamlit as st

# Custom CSS to make the Streamlit app take up the entire page
page_bg_full = """
<style>
[data-testid="stAppViewContainer"] {
    padding: 0;
    margin: 0;
    width: 100%;
}

[data-testid="stHeader"] {
    display: none;
}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stVerticalBlock"] {
    padding-top: 0;
    padding-bottom: 0;
}

[data-testid="stAppViewContainer"] {
    background-color: #F5F5F5;
    margin: 0;
    padding: 0;
    width: 100vw;
    height: 100vh;
}

[data-testid="stSidebar"] {
    display: none;
}
</style>
"""

st.markdown(page_bg_full, unsafe_allow_html=True)

# Streamlit App: Chatbot UI

# Add title with an icon
st.markdown("<h1 style='text-align: center; color: #2E8B57; font-family: Arial, sans-serif;'>🩺 Medical Chatbot for Symptom Diagnosis</h1>", unsafe_allow_html=True)

# Store user's name in session state to keep track
if "name" not in st.session_state:
    st.session_state["name"] = ""

# Check if the user has already submitted their name
if st.session_state["name"]:
    # Step 2: Once the name is entered, welcome the user by name and ask for symptoms
    st.markdown(f"<h3 style='text-align: center; color: #333;'>👋 Hi {st.session_state['name']}! Let's discuss your symptoms.</h3>", unsafe_allow_html=True)
    
    # Create a clean input box for symptoms
    st.markdown("""
        <div style='margin-bottom: 20px;'>
            <label style="font-size: 18px; color: #333; font-family: Arial, sans-serif;'>📝 Describe the symptoms you are feeling below:</label>
        </div>
    """, unsafe_allow_html=True)
    
    # A stylish text area input with increased font size
    symptoms = st.text_area("", placeholder="e.g., fever, sore throat, headache", height=150)
    
    # Custom styled button with hover effect and larger, modern design
    button_html = """
        <style>
        div.stButton > button:first-child {
            background-color: #2E8B57;
            color: white;
            padding: 12px 28px;
            font-size: 18px;
            border-radius: 12px;
            border: none;
            font-family: Arial, sans-serif;
            font-weight: bold;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }
        div.stButton > button:first-child:hover {
            background-color: #45a049;
            color: white;
            box-shadow: 0px 6px 12px rgba(0, 0, 0, 0.3);
        }
        </style>
    """
    st.markdown(button_html, unsafe_allow_html=True)
    
    # Submit button (without model logic)
    if st.button("Submit Symptoms"):
        if symptoms:
            st.markdown(f"""
                <div style='background-color: #FFF; border-radius: 10px; padding: 20px; margin-top: 20px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);'>
                    <p style='text-align: center; font-size: 20px; color: #333; font-family: Arial, sans-serif;'>🤔 {st.session_state['name']}, we're processing your symptoms... (Model coming soon!)</p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.warning(f"{st.session_state['name']}, please enter symptoms before clicking submit.")
else:
    # Step 1: Ask for the user's name if it has not been provided yet
    st.markdown("""
        <div style='background-color: #FFF; border-radius: 10px; padding: 20px; box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);'>
            <p style='text-align: center; font-size: 18px; color: #333; font-family: Arial, sans-serif;'>Please enter your name to begin:</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Input for name
    name_input = st.text_input("👤 Your Name:", placeholder="Enter your name")
    
    # Button to confirm the name
    if st.button("Submit Name"):
        if name_input:
            st.session_state["name"] = name_input
