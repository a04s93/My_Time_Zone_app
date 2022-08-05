import streamlit as st
from datetime import datetime
from pytz import timezone
import pandas as pd

st.title('Turkey トルコ')

eet = datetime.now(timezone('Europe/Istanbul')).strftime('%m月%d日 %H時%M分')
st.write(eet)

st.text("・ページを再読み込みすると時間が更新されます。")

d = {'lat': [41.067695332205204],
     'lon': [28.978759561392064]}
df = pd.DataFrame(data=d)
zoom = 5
st.map(df,zoom)