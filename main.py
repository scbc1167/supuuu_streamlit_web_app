import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

st.title("サプーアプリ")
st.caption("これはサプーの動画用のテストアプリです")

# 画像
image = Image.open("./data/raspberry_pi.jpg")
st.image(image, width=200)