import streamlit as st


st.set_page_config(page_title="Sports Booking", layout="wide")

st.title("🏟️ Sports Booking")

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
            st.session_state["selected_court_index"] = 0
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
            st.session_state["selected_court_index"] = 1
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
            st.session_state["selected_court_index"] = 2
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
            st.session_state["selected_court_index"] = 3
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
            st.session_state["selected_court_index"] = 5
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
            st.session_state["selected_court_index"] = 4
            st.switch_page("pages/checkout.py")
