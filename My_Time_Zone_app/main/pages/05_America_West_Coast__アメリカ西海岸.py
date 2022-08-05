import streamlit as st
from datetime import datetime
from pytz import timezone
import pandas as pd

st.title('America West Coast アメリカ西海岸')

pst = datetime.now(timezone('America/Los_Angeles')).strftime('%m月%d日 %H時%M分')
st.write(pst)

st.text("・ページを再読み込みすると時間が更新されます。")

d = {'lat': [34.14527532917487],
     'lon': [-118.30464665504766]}
df = pd.DataFrame(data=d)
zoom = 3.5
st.map(df,zoom)