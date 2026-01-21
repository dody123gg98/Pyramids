import streamlit as st
import datetime

st.set_page_config(page_title="Check Out", layout="wide")

if "bookings" not in st.session_state:
    st.session_state.bookings = []

selected_sport = st.session_state.get("selected_sport", "Football")
selected_image = st.session_state.get("selected_image", "images/download.webp")

st.title(f"Book {selected_sport}")

col1, col2 = st.columns([1, 2])

with col1:
    st.image(selected_image, width=300)
    st.info(f"Booking for: {selected_sport}")

with col2:
    st.subheader("Booking Details")

    c1, c2 = st.columns(2)
    with c1:
        date = st.date_input("Date", min_value=datetime.date.today())
        start = st.number_input("Start Time (24h)", min_value=0, max_value=23, value=18)
    with c2:
        end = st.number_input("End Time (24h)", min_value=1, max_value=24, value=20)
        number_of_players = st.number_input("Number of players", min_value=1, value=10)

    # Validation
    if end <= start:
        st.error("End time must be after start time")
        duration = 0
    else:
        duration = end - start
        price = duration * 50  # Assuming 50 per hour like in profile example

        st.write(f"**Duration:** {duration} hours")
        st.write("**Price per hour:** $50")
        st.subheader(f"Total Price: ${price}")

        if st.button("Confirm Booking ✅", type="primary"):
            # Get stadium name from session state or use default
            stadium_name = st.session_state.get("selected_court_name", "Main Stadium")

            # Create booking object
            new_booking = {
                "stadium": stadium_name,
                "sport": selected_sport,
                "image": selected_image,
                "date": str(date),
                "time": f"{start}:00",
                "duration": duration,
                "price_per_hour": 50,
            }

            # Save to session state
            st.session_state.bookings.append(new_booking)

            st.success("Booking confirmed! Redirecting to profile...")
            st.switch_page("pages/profile.py")

if st.button("Cancel"):
    st.switch_page("pages/home.py")
