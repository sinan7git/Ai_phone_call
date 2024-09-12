import streamlit as st
import requests

def make_api_call(phone_number):
    url = "https://api.bland.ai/v1/calls"
    
    payload = {
        "phone_number": phone_number,
        "task": "Your company name 'Servtech' act your hiring a software engineer position so act like a HR in That company . instructions: candidate should be be educated and experienced with django python"
    }
    headers = {
        "authorization": "sk-xeb9xarsovo6ftnbl0boioqvxfa71289pi91q8vuxtu6byaotvp0k7zm7a5ttu0x69",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.text

st.title("Bland.ai Integration")

phone_number = st.text_input("Enter phone number:")

if st.button("Make API Call"):
    if phone_number:
        result = make_api_call(phone_number)
        st.json(result)
    else:
        st.error("Please enter both phone number")
        
def list_calls():
    url = "https://api.bland.ai/v1/calls"
    headers = {"authorization": ""}
    response = requests.request("GET", url, headers=headers)
    return response.text

if st.button('list all call'):
    result = list_calls()
    st.json(result)