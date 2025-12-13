import streamlit as st


if "bookings" not in st.session_state:
    st.session_state.bookings = [
        {"stadium": "Stadium A", "sport": "Football", "image": "https://imgresizer.tntsports.io/unsafe/2560x1440/filters:format(jpeg)/origin-imgresizer.tntsports.io/2025/03/11/image-2c33751b-72bd-4b98-9cc2-8873bbd18247-85-2560-1440.jpeg" , "date": "2025-12-05", "time": "18:00", "duration": 2, "price_per_hour": 50},
        {"stadium": "Stadium B", "sport": "Basketball", "image": "https://imgresizer.tntsports.io/unsafe/2560x1440/filters:format(jpeg)/origin-imgresizer.tntsports.io/2025/03/11/image-2c33751b-72bd-4b98-9cc2-8873bbd18247-85-2560-1440.jpe", "date": "2025-12-07", "time": "15:00", "duration": 1, "price_per_hour": 40}
    ]


if "user_name" not in st.session_state :  
    st.session_state.user_name = "username"
    
if "phone" not in st.session_state :
    st.session_state.phone = "01**********"

if "email" not in st.session_state :
    st.session_state.email = "username@gmail.com"
    
if "image_path" not in st.session_state : 
    st.session_state.image_path = "C:/Users/RAM/Desktop/techno/images/profilepicture.jpeg"

st.set_page_config(page_title="Profile", layout="wide")

st.sidebar.title("🏟️ Sports Gallery")

if len(st.session_state.bookings) == 0:
    st.sidebar.image("https://images.unsplash.com/photo-1599058917210-d3a5b414d9b4?fit=crop&w=300&q=80", caption="Book your favorite sport", width=200)
    st.sidebar.image("https://images.unsplash.com/photo-1521412644187-c49fa049e84d?fit=crop&w=300&q=80", caption="Play, Have Fun!", width=200)






user_name = st.session_state.user_name
email = st.session_state.email
phone = st.session_state.phone
image_path = st.session_state.image_path

st.title("User Profile")

col1, col2 = st.columns([1,2])      

with col1:
    st.image(image_path, width=200)

with col2:
    st.subheader(f"Welcome, {user_name}")
    st.write(f"**Email:** {email}")
    st.write(f"**Phone:** {phone}")
    st.markdown("---------------------")



st.divider()

st.header("My Bookings")

if len(st.session_state.bookings) == 0:
        st.info("You have no bookings yet.")
else:
    for idx, booking in enumerate(st.session_state.bookings):
        c1, c2 = st.columns(2)
        
        with c1 :     
            st.subheader(f"Booking {idx+1}")
            st.write("**Stadium:**", booking["stadium"])
            st.write("**Sport:**", booking["sport"])
            st.write("**Date:**", booking["date"])
            st.write("**Time:**", booking["time"])
            st.write("**Duration:**", f"{booking['duration']} hour(s)")
            total_price = booking["duration"] * booking["price_per_hour"]
            st.write("**Total Price:** $", total_price)
            
            if st.button("Cancel Booking", key=f"cancel_{idx}"):
                st.session_state.bookings.pop(idx)
                st.rerun()
        with c2 :
            st.image(booking["image"])
