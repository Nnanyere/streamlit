import streamlit as st
import requests as rq

st.title('Welcome')

st.markdown(''':green[Welcome] to :rainbow[Amanze's website!]  
My favorite color is `#10A810`, a shade of :green-background[green]. :rainbow-background[What's yours?]''')

st.header(':violet[The images, as requested.]')
st.page_link("pages/Pictures.py", label="See them here", icon="🖼️")

response = rq.get("https://www.youtube.com/watch?v=rkxqt9SVO4E")
r = rq.head('https://www.youtube.com/watch?v=rkxqt9SVO4E')

if response.status_code == 200:
    st.text('Header of 1st video: ' + str(r))
    st.text(response.url)
    st.video(response.url)

if st.button("Watch basketball"):
    st.button("Stop watching", type="primary")
    st.video("https://www.shutterstock.com/shutterstock/videos/3513537983/preview/stock-footage-vertical-screen-aerial-view-of-basketball-game-on-green-outdoor-court-with-players-in-motion-shot.webm")
