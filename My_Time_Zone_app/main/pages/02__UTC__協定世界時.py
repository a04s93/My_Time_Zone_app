import streamlit as st
from datetime import datetime
from pytz import timezone

st.title('UTC 世界協定時')

st.text("・ページを再読み込みすると時間が更新されます。")
utc = datetime.now(timezone('UTC')).strftime('%m月%d日 %H時%M分')
st.write(utc)


