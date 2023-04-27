
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
    one = Image.open('STOCHAST/1.jpg')
    with pictures:
        st.image(one, width=500)
    with text:
        st.text("1111111111111111111111111111111111111")


def secondImage():
    two = Image.open('STOCHAST/2.jpg')
    with pictures:
        st.image(two, width=500)
    with text:
        st.text("222222222222222222222")


def thirdImage():
    three = Image.open('STOCHAST/3.jpg')
    with pictures:
        st.image(three, width=500)
    with text:
        st.text("33333333333333333333333333333")


def fourthImage():
    four = Image.open('STOCHAST/4.jpg')
    with pictures:
        st.image(four, width=500)
    with text:
        st.text("4444444444444444444444444444444")


def fiveImage():
    five = Image.open('STOCHAST/5.jpg')
    with pictures:
        st.image(five, width=500)
    with text:
        st.text("555555555555555555555555555555")


function_list = [firstImage ,secondImage ,thirdImage, fourthImage, fiveImage]

# Shuffle the list of functions
random.shuffle(function_list)

# Call each function in the shuffled order
for function in function_list:
    function()

st.divider()

st.text('''Fine art installation by Dante McDonald
           In colaboration with CASSACORP''')
