import streamlit as st 

st.title("Check Out")
st.set_page_config(page_title="Check Out", layout="wide")
col1, col2, col3 = st.columns(3)

with col1:
    start = st.number_input("from")
    
with col2:
    end = st.number_input("To")

with col3:
    st.radio("",["AM","PM"])
    
duration = end - start 

price = duration *5 
st.subheader(price)

number_of_players = st.number_input("Number of players")
