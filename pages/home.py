import streamlit as st


st.set_page_config(layout="wide")


st.title("title")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Football")
    st.image("images/download.webp", width=300)
    st.button("Details 1")

    st.subheader("Basketball")
    st.image("images/1.webp", width=300)
    st.button("Details 2")


with col2:
    st.subheader("Padel")
    st.image("images/download (1).webp", width=300)
    st.button("Details 3")

    st.subheader("Tennis")
    st.image("images/OIP (3).webp", width=300)
    st.button("Details 4")

with col3:
    st.subheader("Handball")
    st.image("images/OIP (4).webp", width=300)
    st.button("Details 5")

    st.subheader("Volleyball")
    st.image("images/download (2).webp", width=300)
    st.button("Details 6")
