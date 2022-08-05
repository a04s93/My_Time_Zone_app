import streamlit as st
from datetime import datetime
from pytz import timezone
import pandas as pd

st.title('India インド')

ist = datetime.now(timezone('Asia/Kolkata')).strftime('%m月%d日 %H時%M分')
st.write(ist)

st.text("・ページを再読み込みすると時間が更新されます。")

d = {'lat': [28.62200652896512],
     'lon': [77.19765342686347]}
df = pd.DataFrame(data=d)
zoom = 5
st.map(df,zoom)