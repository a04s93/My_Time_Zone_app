import streamlit as st
from datetime import datetime
from pytz import timezone
import pandas as pd

st.title('United Kingdom イギリス')


gmt_bst = datetime.now(timezone('Europe/London')).strftime('%m月%d日 %H時%M分')
st.write(gmt_bst)

st.text("・ページを再読み込みすると時間が更新されます。")

d = {'lat': [51.47714310185956],
     'lon': [-0.0005058908240075378]}
df = pd.DataFrame(data=d)
zoom = 4
st.map(df,zoom)