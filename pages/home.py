import streamlit as st


st.set_page_config(page_title="Sports Booking", layout="wide")

# Navigation bar
nav_col1, nav_col2, nav_col3, nav_col4 = st.columns([3, 1, 1, 1])
with nav_col1:
    st.title("🏟️ Sports Booking")
with nav_col2:
    if st.button("ℹ️ About Us"):
        st.switch_page("pages/about-us.py")
with nav_col3:
    if st.button("👤 Profile"):
        st.switch_page("pages/profile.py")
with nav_col4:
    if st.button("🔐 Sign In"):
        st.switch_page("pages/sign_in.py")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("Football")
    st.image("images/download.webp", width=300)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("View Details", key="details_football"):
            st.session_state["selected_court_index"] = 0
            st.switch_page("pages/details.py")
    with c2:
        if st.button("Quick Book", key="book_football", type="primary"):
            st.session_state["selected_sport"] = "Football"
            st.session_state["selected_image"] = "images/download.webp"
            st.switch_page("pages/checkout.py")

    st.subheader("Basketball")
    st.image("images/1.webp", width=300)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("View Details", key="details_basketball"):
            st.session_state["selected_court_index"] = 1
            st.switch_page("pages/details.py")
    with c2:
        if st.button("Quick Book", key="book_basketball", type="primary"):
            st.session_state["selected_sport"] = "Basketball"
            st.session_state["selected_image"] = "images/1.webp"
            st.switch_page("pages/checkout.py")


with col2:
    st.subheader("Padel")
    st.image("images/download (1).webp", width=300)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("View Details", key="details_padel"):
            st.session_state["selected_court_index"] = 2
            st.switch_page("pages/details.py")
    with c2:
        if st.button("Quick Book", key="book_padel", type="primary"):
            st.session_state["selected_sport"] = "Padel"
            st.session_state["selected_image"] = "images/download (1).webp"
            st.switch_page("pages/checkout.py")

    st.subheader("Tennis")
    st.image("images/OIP (3).webp", width=300)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("View Details", key="details_tennis"):
            st.session_state["selected_court_index"] = 3
            st.switch_page("pages/details.py")
    with c2:
        if st.button("Quick Book", key="book_tennis", type="primary"):
            st.session_state["selected_sport"] = "Tennis"
            st.session_state["selected_image"] = "images/OIP (3).webp"
            st.switch_page("pages/checkout.py")

with col3:
    st.subheader("Handball")
    st.image("images/OIP (4).webp", width=300)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("View Details", key="details_handball"):
            st.session_state["selected_court_index"] = 5
            st.switch_page("pages/details.py")
    with c2:
        if st.button("Quick Book", key="book_handball", type="primary"):
            st.session_state["selected_sport"] = "Handball"
            st.session_state["selected_image"] = "images/OIP (4).webp"
            st.switch_page("pages/checkout.py")

    st.subheader("Volleyball")
    st.image("images/download (2).webp", width=300)
    c1, c2 = st.columns(2)
    with c1:
        if st.button("View Details", key="details_volleyball"):
            st.session_state["selected_court_index"] = 4
            st.switch_page("pages/details.py")
    with c2:
        if st.button("Quick Book", key="book_volleyball", type="primary"):
            st.session_state["selected_sport"] = "Volleyball"
            st.session_state["selected_image"] = "images/download (2).webp"
            st.switch_page("pages/checkout.py")
