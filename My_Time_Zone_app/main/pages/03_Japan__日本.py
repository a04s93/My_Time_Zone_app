import streamlit as st
from datetime import datetime
from pytz import timezone
import pandas as pd



st.title('Japan 日本')

jst = datetime.now(timezone('Asia/Tokyo')).strftime('%m月%d日 %H時%M分')
st.write(jst)

st.text("・ページを再読み込みすると時間が更新されます。")


d = {'lat': [35.65869374085077],
     'lon': [139.7454650710934]}
df = pd.DataFrame(data=d)
zoom = 3.5
st.map(df,zoom)
