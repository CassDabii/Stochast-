import streamlit as st
from PIL import Image
import random
st.set_page_config(layout='centered')

st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">STOCHAST</p>', unsafe_allow_html=True)
st.subheader('A STORY SUBJECT TO THE LAWS OF PROBABILITY')

pictures = st.container()
text = st.container()

def firstImage():
    one = Image.open('STOCHAST/IMG_1469-4.jpeg')
    with pictures:
        st.image(one, width=500)
    with text:
        st.write("""A twenty euro on the table to cover the meal, then emptied the rest of the contents of the purse on
the table. I had no more need for money and I want them to know.""")


def secondImage():
    two = Image.open('STOCHAST/IMG_1944-2.jpeg')
    with pictures:
        st.image(two, width=500)
    with text:
        st.write("""So this is revenge?. Im doing this for you. Whatever you may think of me I wouldn’t do something
that low. I cant trust them.""")


def thirdImage():
    three = Image.open('STOCHAST/IMG_1990-2.jpeg')
    with pictures:
        st.image(three, width=500)
    with text:
        st.write("""The eating grew to an end. He lowered his voice as though they could be heard over the din and
clatter. Ive been watchin him you know. I invite you to join me in the next room for entertainment.""")


def fourthImage():
    four = Image.open('STOCHAST/IMG_2061.jpeg')
    with pictures:
        st.image(four, width=500)
    with text:
        st.write("""Say Bermondsey and they wrinkle their noses. Still, it was the home before all homes. The river
lapped beneath us as we slept. Dark water heaved up an odd sullen grey.""")


def fiveImage():
    five = Image.open('STOCHAST/IMG_2191.jpeg')
    with pictures:
        st.image(five, width=500)
    with text:
        st.write("""Im all out of pop groups, was I wrong to be angry? You’ve done everything u could. I sighed heavily. I
just wanted to…. What was I thinking?.""")


function_list = [firstImage ,secondImage ,thirdImage, fourthImage, fiveImage]

# Shuffle the list of functions
random.shuffle(function_list)

# Call each function in the shuffled order
for function in function_list:
    function()

st.divider()

st.text('''Fine art installation by Dante McDonald
           In colaboration with CASSACORP''')
