import streamlit as st
from datetime import datetime
from pytz import timezone
import pandas as pd

st.title('America East coast アメリカ東海岸')

est = datetime.now(timezone('America/New_York')).strftime('%m月%d日 %H時%M分')
st.write(est)

st.text("・ページを再読み込みすると時間が更新されます。")

d = {'lat': [40.761405224863346],
     'lon': [-73.98586793142317]}
df = pd.DataFrame(data=d)
zoom = 3.5
st.map(df,zoom)