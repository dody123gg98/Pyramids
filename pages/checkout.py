import streamlit as st
import datetime
from data import courts_details

st.set_page_config(page_title="Check Out", layout="wide")


if "is_signed_in" not in st.session_state or st.session_state.is_signed_in == False:
    st.session_state.is_signed_in = False
    st.warning("Please sign in first.")
    if st.button("Sign In", use_container_width=True):
        st.switch_page("pages/sign_in.py")
    st.stop()

if "bookings" not in st.session_state:
    st.session_state.bookings = []

if "selected_court_index" not in st.session_state:
    st.warning("Please select a court first.")
    st.switch_page("pages/home.py")

court_index = st.session_state.selected_court_index
selected_court = courts_details[court_index]

st.title(f"Book {selected_court['sport']}")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(selected_court["image 1"], width=300)
    st.info(f"Booking for: {selected_court['sport']}")

with col2:
    st.subheader("Booking Details")

    c1, c2 = st.columns(2)
    with c1:
        date = st.date_input("Date", min_value=datetime.date.today())
        number_of_players = st.number_input("Number of players", min_value=1, value=4)

    with c2:
        start_time = st.number_input(
            "Start Time (24h)",
            min_value=0,
            max_value=23,
        )
        end_time = st.number_input(
            "End Time (24h)", min_value=1, max_value=24, value=20
        )

    if end_time <= start_time:
        st.error("End time must be after start time")
        duration = 0
    else:
        duration = end_time - start_time
        total_price = selected_court["price"] * duration

        st.write(f"**Duration:** {duration} hours")
        st.write(f"**Price per hour:** {selected_court['price']}")
        st.subheader(f"Total Price: {total_price}")

        if st.button("Confirm Booking ✅", type="primary"):
            stadium_name = st.session_state.get("selected_court_name", "Main Stadium")

            new_booking = {
                "stadium": stadium_name,
                "sport": selected_court["sport"],
                "image": selected_court["image 1"],
                "date": str(date),
                "time": f"{start_time}:00",
                "duration": duration,
                "price_per_hour": selected_court["price"],
            }

            st.session_state.bookings.append(new_booking)

            st.success("Booking confirmed! Redirecting to profile...")
            st.switch_page("pages/profile.py")

if st.button("Cancel"):
    st.switch_page("pages/home.py")
