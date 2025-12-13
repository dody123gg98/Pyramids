import streamlit as st

st.set_page_config(layout="wide")


st.title("✨About us")

col1, col2 = st.columns(2)

with col1:
    st.image("https://img.icons8.com/clouds/256/000000/globe-earth.png", width=225)

with col2:
    st.header("Our Mission")
    st.write("Make an app for booking sports fields ")


st.header("🎇Why to choose us❓")

col3, col4, col5, col6 = st.columns(4)

with col3:
    st.subheader("⚽Easy booking")
    st.write("You can book any field you want effortlessly")

with col4:
    st.subheader("🏀Many sports")
    st.write("You can find any type of famous sports you want in this app")

with col5:
    st.subheader("💰Payment methods")
    st.write("You can pay by visa in the app or by cash when you go to the field")

with col6:
    st.subheader("⌚Flexible schedule")
    st.write(
        "All appointments  are available, but if someone has booked the appointments you want, it will be closed"
    )


if st.button("home", use_container_width=True):
    st.switch_page("./pages/home.py")


if st.button("contact-us", use_container_width=True):
    st.switch_page("./pages/contact_us.py")
