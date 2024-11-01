import os
import streamlit as st
# from dotenv import load_dotenv

# load_dotenv()

# passcode = os.getenv("PASSCODE")
passcode = st.secrets["general"]["PASSCODE"]

if "access_granted" not in st.session_state:
    st.session_state.access_granted = False
if "current_riddle" not in st.session_state:
    st.session_state.current_riddle = 0

if not st.session_state.access_granted:
    st.title("Birthday Riddle Challenge 🎉")
    entered_passcode = st.text_input("Enter the passcode to get the first riddle:")

    if entered_passcode == passcode:
        st.session_state.access_granted = True
        st.success("Access granted! Let's start the challenge!")

    elif entered_passcode:
        st.error("Incorrect passcode. Please try again.")


if st.session_state.access_granted:
    agenda = [
        {
            "riddle": "I'm known for my wool, though I'm not quite a sheep. In fields or mountains, I often leap. Friendly and furry, I'll make you smile. Who am I?",
            "answer": "alpaca",
            "activity": "Alpaca Experience (Meet and Greet)",
            "image": "https://media.istockphoto.com/id/532529153/photo/alpacas.jpg?s=612x612&w=0&k=20&c=aVBIqadOqFHh_CsUUtF5C70KPib880X8bNawv2l7Ni8="
        },
        {
            "riddle": "To test your aim and give you a thrill, you'll toss me at a target, just for the skill. Held by a handle, with a blade at one end, I'm thrown for sport or defense. What am I?",
            "answer": "axe",
            "activity": "Boom Battle Bar (Axe Throwing)",
            "image": "https://s40091.pcdn.co/uk/london-oxford-street/wp-content/uploads/sites/30/2022/10/AR-AxeThrowing_Boom-Games-Hero.jpg"
        },
        {
            "riddle": "Around obstacles, you'll aim and you'll swing. This game has clubs, not the dancing kind, and holes to bring. Smaller than standard, but just as much fun, a ball game indoors, it's hole-in-one!",
            "answer": "golf",
            "activity": "Boom Battle Bar (Crazier Golf)",
            "image": "https://s40091.pcdn.co/uk/ipswich/wp-content/uploads/sites/17/2022/04/Crazier-Golf_Boom-Games-Hero.jpg"
        },
        {
            "riddle": "A place with flavors both old and new, with food that is savory, spicy, and true. In London, high above the streets below, we dined at this restaurant on a special day in 2019. Where are you going?",
            "answer": "tattu",
            "activity": "Tattu Chinese Restaurant",
            "image": "https://tattu.co.uk/wp-content/uploads/2024/03/P10655-350-Cherry-blossom-pink-1500x900.jpg"
        },
    ]

    current_riddle = agenda[st.session_state.current_riddle]

    st.title("Birthday Riddle Challenge 🎉")

    st.write("Solve this riddle to unlock the next part of the agenda!")
    st.write(f"Riddle: {current_riddle['riddle']}")
    user_answer = st.text_input("Enter your answer here:")

    if user_answer.lower() == current_riddle["answer"]:
        st.success("Correct! 🎉")
        st.write(f"You've unlocked the next activity: **{current_riddle['activity']}**")
        st.image(current_riddle["image"], caption=current_riddle["activity"], use_column_width=True)
        
        if st.session_state.current_riddle < len(agenda) - 1:
            if st.button("Go to the Next Riddle"):
                st.session_state.current_riddle += 1
        else:
            st.write("Congratulations! You've unlocked the full agenda!")
            st.success("🎉 Happy Birthday on your special day! 🎉")
    else:
        if user_answer:
            st.error("Oops! Try again.")
