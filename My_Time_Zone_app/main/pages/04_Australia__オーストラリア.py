import streamlit as st
from datetime import datetime
from pytz import timezone
import pandas as pd

st.title('Australia オーストラリア')

aest_aedt = datetime.now(timezone('Australia/Sydney')).strftime('%m月%d日 %H時%M分')
st.write(aest_aedt)

st.text("・ページを再読み込みすると時間が更新されます。")

d = {'lat': [-33.82967634319072],
     'lon': [151.2175920962482]}
df = pd.DataFrame(data=d)
zoom = 2.5
st.map(df,zoom)