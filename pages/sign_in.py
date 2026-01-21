import streamlit as st
from data import users_accounts

st.set_page_config(page_title="Sign In", layout="wide")

st.title("🔐 Sign In")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login", type="primary", use_container_width=True):
    found = False

    for user in users_accounts:
        if user["email"] == email and user["password"] == password:
            st.session_state.user_name = user["username"]
            st.session_state.email = user["email"]
            st.session_state.phone = user["phone"]
            st.success("Welcome back, " + user["username"] + "!")
            found = True
            st.switch_page("pages/profile.py")
            break

    if not found:
        st.error("Invalid email or password")

st.divider()

col1, col2 = st.columns(2)

with col1:
    if st.button("← Back to Home", use_container_width=True):
        st.switch_page("pages/home.py")

with col2:
    if st.button("Sign Up →", use_container_width=True):
        st.switch_page("pages/signup.py")
