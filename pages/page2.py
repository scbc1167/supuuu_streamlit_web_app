import streamlit as st
from PIL import Image
import datetime
import pandas as pd
import matplotlib.pyplot as plt

with st.form(key="profile_form"):
    # テキストボックス
    name = st.text_input("名前")
    address = st.text_input("住所")
    
    # # セレクトボックス
    # age_category = st.selectbox("年齢層", ("子供(18歳未満)", "大人(18歳以上)"))
    
    # ラジオボタン
    age_category = st.radio("年齢層", 
                            ("子供(18歳未満)", "大人(18歳以上)"))
    
    # チェックボックス
    mail_subscribe = st.checkbox("メールマガジンを購読する")
    
    # スライダー
    height = st.slider("身長", min_value=110, max_value=210)
    
    # 複数選択
    hobby = st.multiselect(
        "趣味", 
        ("スポーツ", "読書", "プログラミング", "アニメ・映画", "釣り", "料理"))
    
    # 日付
    start_date = st.date_input("開始日", datetime.date(2022, 7, 1))
    
    # カラーピッカー
    color = st.color_picker("テーマカラー", "#00f900")
    
    # ボタン
    submit_btn = st.form_submit_button("送信")
    cancel_btn = st.form_submit_button("キャンセル")
    
if submit_btn:
    st.text("ようこそ!%sさん%sに書籍を送りました!!"%(name, address))