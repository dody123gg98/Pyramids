import streamlit as st 
import time
import os 
from pathlib import Path

st.set_page_config(page_title="My Website", layout="wide")
st.sidebar.title("Digital Ink")


username_input = st.text_input("First Name")
email_input = st.text_input("Enter your email✉")
password_input = st.text_input("Enter your password🔑", type="password")
confirm_password = st.text_input("Confirm your password", type="password")
phone_input = st.text_input("Enter your mobile phone📱")
date_input = st.date_input("Enter your date of birth📆")
age_input = st.number_input("Enter your age🎂", min_value=0, max_value=120, step=1)
gender = st.radio("Choose your gender",("Male", "Female"))

uploaded_file = st.file_uploader("Upload your profile picture", type=["jpg", "jpeg", "png"])

if st.button("Submit ✅"):
    if uploaded_file:
        upload_dir = Path("uploads") 
        upload_dir.mkdir(exist_ok=True)
        
        file_path = upload_dir / f"{int(time.time())}_{uploaded_file.name}"
        file_path.write_bytes(uploaded_file.read())
        
        st.success(f"Uploaded {uploaded_file.name} successfully! ✅")
        
    if email_input and password_input and phone_input and age_input:
        if password_input != confirm_password:
            st.error("Passwords don't match! Please try again.")
            
        st.success("Account created successfully🎉!")
        st.write("Here's the information you entered:")
        st.write(f"-**Email:** {email_input}")
        st.write(f"-**Phone:** {phone_input}")
        st.write(f"-**Date of birth:** {date_input} ")
        st.write(f"-**Age:** {age_input}")
        
        st.session_state.user_name = username_input
        st.session_state.email = email_input
        st.session_state.phone = phone_input
        st.session_state.date_input = date_input
        st.session_state.age_input = age_input
        st.session_state.image_path = (
                uploaded_file.getvalue() if uploaded_file else None)
        
        
        
        
        
        time.sleep(3)
        st.switch_page("pages/profile.py")
        
    else:
     st.error("Please fill in all fields❌❗")
     
     
    


     



           