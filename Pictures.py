import streamlit as st
import requests as rq
from PIL import Image

st.title(":violet[Pictures]");

img1, img2, img3, img4 = st.columns(4, vertical_alignment="bottom")

with img1:
    st.image(Image.open('family.png'), caption="My family. I'm at the top in the center.")

with img2:
    st.image(Image.open('track.png'), caption="I've done track & field every year in high school")

with img3:
    st.image(Image.open('capitol.jpg'), caption="This is a picture of the U. S. Capitol from last summer.")

with img4:
    st.image(Image.open('museum.jpg'), caption="I also went to the Smithsonian National Museum of Natural History.")

st.page_link("Main_Page.py", label="Go back home", icon="🏠")