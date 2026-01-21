import streamlit as st
from data import courts_details


st.set_page_config(page_title="Details", layout="wide")

# Check if a court was selected
if "selected_court_index" not in st.session_state:
    st.warning("Please select a court from the home page first.")
    if st.button("← Go to Home"):
        st.switch_page("pages/home.py")
    st.stop()

court_index = st.session_state["selected_court_index"]
court = courts_details[court_index]

st.title("Court Details")
st.header(court["name"])

col1, col2 = st.columns([2, 1])

with col1:
    st.image(court["image 1"], width=700)

with col2:
    st.subheader("💰 Price")
    st.write(court["price"])
    st.subheader("⚽ Sport")
    st.write(court["sport"])
    st.subheader("📏 Dimension")
    st.write(court["dimension"])
    st.subheader("📐 Area")
    st.write(f"{court['area']} m²")


st.divider()

col3, col4 = st.columns([1, 2])

with col3:
    st.subheader("🏢 Club")
    st.write(court["club"])
    st.subheader("🏟️ Type")
    st.write(court["type"].capitalize())
    st.subheader("✨ Amenities")
    if "amenities" in court:
        for amenity in court["amenities"]:
            st.write(f"✓ {amenity}")
    else:
        st.write("Standard facilities")

with col4:
    st.image(court["image 2"], width=700)


st.divider()

c1, c2 = st.columns(2)

with c1:
    if st.button("← Back to Home", use_container_width=True):
        st.switch_page("pages/home.py")

with c2:
    if st.button("Book Now", type="primary", use_container_width=True):
        st.session_state["selected_sport"] = court["sport"]
        st.session_state["selected_image"] = court["image 1"]
        st.session_state["selected_court_name"] = court["name"]
        st.switch_page("pages/checkout.py")
