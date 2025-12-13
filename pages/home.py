import streamlit as st


st.set_page_config(layout="wide")


st.title("title")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Football")
    st.image("C:/Users/IT/Desktop/project/images/download.webp", width=300)
    st.button("Details 1")

    st.subheader("Basketball")
    st.image("C:/Users/IT/Desktop/project/images/1.webp", width=300)
    st.button("Details 2")


with col2:
    st.subheader("Padel")
    st.image("C:/Users/IT/Desktop/project/images/download (1).webp", width=300)
    st.button("Details 3")

    st.subheader("Tennis")
    st.image("C:/Users/IT/Desktop/project/images/OIP (3).webp", width=300)
    st.button("Details 4")

with col3:
    st.subheader("Handball")
    st.image("C:/Users/IT/Desktop/project/images/OIP (4).webp", width=300)
    st.button("Details 5")

    st.subheader("Volleyball")
    st.image("C:/Users/IT/Desktop/project/images/download (2).webp", width=300)
    st.button("Details 6")
