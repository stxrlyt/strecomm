from pathlib import Path
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import subprocess

THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

HOME_PAGE = ""
CART_PAGE = ""
PROFILE_PAGE = ""
CONTACT_PAGE = ""

PRODUCT_NAME = "Fresh Apples"
PROD_PRICE = "Rp25.000/kg"
PROD_DESC = "Lorem Ipsum blabalabalalghsldkghdklshgklghsdlhgslgskghnvcxmgewoi"
PROD_DATA = {'Head': ['Stock', 'printer', 'tablet', 'desk', 'chair'],'Feet':[200, 150, 300, 450, 200]}

st.set_page_config(
    page_title=PRODUCT_NAME+" - ToBuy",
    page_icon =":apple:",
    layout = "centered",
    initial_sidebar_state = "expanded",
)

# Side Panel
st.sidebar.title("ToBuy")
if st.sidebar.button("🏠 Home"):
    subprocess.run(["streamlit", "run", "index.py"])
if st.sidebar.button("🛒 Cart"):
    subprocess.run(["streamlit", "run", "cart.py"])
if st.sidebar.button("🙋 Profile"):
    subprocess.run(["streamlit", "run", "profile.py"])

# Main topic - the apple
st.markdown("[Back to home](./index.py)")
st.header(PRODUCT_NAME)
st.subheader(PROD_PRICE)
st.write("__")
left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(PROD_DESC)
    st.table(PROD_DATA)
with right_col:
    product_image = Image.open(ASSETS_DIR / "apple.png")
    st.image(product_image, width = 200)
    st.link_button("🛒 Add into cart", "#")

# Rating
RATING = st.slider('How do you want to rate it?', 1, 5)
REVIEW_TEXT = st.text_area("What's your thoughts?")
st.link_button("Submit", "#")

#Recommended Products
st.header('Recommended Products')
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
    st.write("Chicken")
    st.write("Rp35.000/kg")
with col2:
    st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
    st.write("Chicken")
    st.write("Rp35.000/kg")
with col3:
    st.markdown("[![Foo](http://www.google.com.au/images/nav_logo7.png)](http://google.com.au/)")
    st.write("Chicken")
    st.write("Rp35.000/kg")