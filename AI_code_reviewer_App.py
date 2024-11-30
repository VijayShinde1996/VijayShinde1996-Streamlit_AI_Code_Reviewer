import streamlit as st
import google.generativeai as genai

# Configure API key for Google Generative AI
genai.configure(api_key="XX")

# Initialize the LLM model and create a chatbot session
llm = genai.GenerativeModel("models/gemini-1.5-flash")
chatbot = llm.start_chat(history=[])

# Title of the application
st.title("AI Code Reviewer")

# Initial message
st.chat_message("ai").write("Hello! I am here to review your code. Please paste your code below for analysis.")

# Input area for the user to paste code
user_code = st.text_area("Paste your code here...")

# If there's code input, process it for review
if user_code:
    st.chat_message("human").write("Review this code snippet, please.")
    
    # Craft the prompt for code review
    review_prompt = f"Please review the following code:\n\n{user_code}\n\n"
    review_prompt += "Check for best practices, optimizations, and potential issues."

    # Send the code snippet to the chatbot for review
    response = chatbot.send_message(review_prompt)
    
    # Display the review from the AI
    st.chat_message("ai").write(response.text)
