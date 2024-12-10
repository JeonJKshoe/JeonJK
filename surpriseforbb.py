import streamlit as st
import time
from datetime import datetime

# Set the page configuration
st.set_page_config(page_title="A Surprise for You ❤️", page_icon="💌", layout="centered")

# Function to display a message with a typing effect
def type_message(message, delay=0.05):
    placeholder = st.empty()
    full_message = ""
    for char in message:
        full_message += char
        placeholder.markdown(full_message)
        time.sleep(delay)

# App Title and Header
st.title("💖 A Special Surprise 💖")
st.header("This is for you!")

# Display an image (you can replace the URL with any image link or local file path)
st.image("bb.jpg", caption="For the one I love",  use_container_width=True)

# Collect your partner's name
partner_name = st.text_input("What's your name?", placeholder="Enter your name here")

if partner_name:
    st.write(f"Hi {partner_name}! 💕")
    st.write("I have a little message for you...")

    # Button to reveal the surprise message
    if st.button("Reveal the Surprise 💌"):
        with st.spinner("Preparing your surprise..."):
            time.sleep(2)
        st.success("Here's something special for you!")

        # Heartfelt message with typing effect
        type_message(f"Dear Sayang,\n\n")
        type_message("Every day with you feels like a dream come true. 💖\n")
        type_message("You light up my life in ways words can't fully express.\n")
        type_message("Thank you for being the amazing person you are.\n\n")
        type_message("I love you so much bb. 💕")

        # Add a timestamp
        st.write(f"\n*Sent on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*")

        # Add some celebratory balloons
        st.balloons()
