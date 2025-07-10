import streamlit as st

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app.")

# Text input
user_input = st.text_input("Type something:")

if user_input:
    st.write(f"You typed: {user_input}")
    
st.write("By Dheemanth Projects")
