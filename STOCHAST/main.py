import streamlit as st
from PIL import Image

st.set_page_config(layout='wide')

st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">STOCHAST</p>', unsafe_allow_html=True)
st.subheader('A STORY SUBJECT TO THE LAWS OF PROBABILITY')

# Create a list of containers
containers = [st.container() for _ in range(5)]

def firstImage(container):
    one = Image.open('STOCHAST/IMG_1469-4.jpeg')
    with container:
        st.image(one, width=200)
        st.markdown("""A twenty euro on the table to cover the meal, then emptied the rest of the contents of the purse on
the table. I had no more need for money and I want them to know.""")

def secondImage(container):
    two = Image.open('STOCHAST/IMG_1944-2.jpeg')
    with container:
        st.image(two, width=200)
        st.markdown("""So this is revenge?. Im doing this for you. Whatever you may think of me I wouldn’t do something
that low. I cant trust them.""")

def thirdImage(container):
    three = Image.open('STOCHAST/IMG_1990-2.jpeg')
    with container:
        st.image(three, width=200)
        st.markdown("""The eating grew to an end. He lowered his voice as though they could be heard over the din and
clatter. Ive been watchin him you know. I invite you to join me in the next room for entertainment.""")

def fourthImage(container):
    four = Image.open('STOCHAST/IMG_2061.jpeg')
    with container:
        st.image(four, width=200)
        st.markdown("""Say Bermondsey and they wrinkle their noses. Still, it was the home before all homes. The river
lapped beneath us as we slept. Dark water heaved up an odd sullen grey.""")

def fiveImage(container):
    five = Image.open('STOCHAST/IMG_2191.jpeg')
    with container:
        st.image(five, width=200)
        st.markdown("""Im all out of pop groups, was I wrong to be angry? You’ve done everything u could. I sighed heavily. I
just wanted to…. What was I thinking?.""")

# Shuffle the list of containers
import random
random.shuffle(containers)

# Call each function with the next available container
for fn, container in zip([firstImage, secondImage, thirdImage, fourthImage, fiveImage],
