import streamlit as st
from PIL import Image
import random
import base64


st.set_page_config(layout='wide')

st.markdown("""
<style>
.big-font {
    font-size:80px !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
.left-image {
    float: left;
    margin-right: 20px;
}
.next-to-image {
    margin-left: 220px;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">STOCHAST</p>', unsafe_allow_html=True)
st.subheader('A STORY SUBJECT TO THE LAWS OF PROBABILITY')

row1 = st.container()
row2 = st.container()
row3 = st.container()
row4 = st.container()
row5 = st.container()

containers = [row1, row2, row3, row4, row5]

col1, col2 = st.columns(2)

def firstImage():
    one = Image.open('STOCHAST/IMG_1469-4.jpeg')
    with containers.pop(random.randrange(len(containers))):
            st.markdown(f'''
            <img class="left-image" src="data:image/jpeg;base64,{base64.b64encode(open(one, "rb").read()).decode()}>''', unsafe_allow_html=True)
            st.markdown('<p class="next-to-image">A twenty euro on the table to cover the meal, then emptied the rest of the contents of the purse on the table. I had no more need for money and I want them to know.</p>', unsafe_allow_html=True)



def secondImage():
    two = Image.open('STOCHAST/IMG_1944-2.jpeg')
    with containers.pop(random.randrange(len(containers))):
            st.image(two, width=400)
            st.write("""So this is revenge?. Im doing this for you. Whatever you may think of me I wouldn’t do something
that low. I cant trust them.""")


def thirdImage():
    three = Image.open('STOCHAST/IMG_1990-2.jpeg')
    with containers.pop(random.randrange(len(containers))):
            st.image(three, width=400)
            st.write("""The eating grew to an end. He lowered his voice as though they could be heard over the din and
clatter. Ive been watchin him you know. I invite you to join me in the next room for entertainment.""")


def fourthImage():
    four = Image.open('STOCHAST/IMG_2061.jpeg')
    with containers.pop(random.randrange(len(containers))):
            st.image(four, width=400)
            st.write("""Say Bermondsey and they wrinkle their noses. Still, it was the home before all homes. The river
lapped beneath us as we slept. Dark water heaved up an odd sullen grey.""")


def fiveImage():
    five = Image.open('STOCHAST/IMG_2191.jpeg')
    with containers.pop(random.randrange(len(containers))):
            st.image(five, width=400)
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
