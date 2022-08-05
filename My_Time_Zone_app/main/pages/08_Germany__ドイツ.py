import streamlit as st
from datetime import datetime
from pytz import timezone
import pandas as pd

st.title('Germany ドイツ')

cet_dst = datetime.now(timezone('Europe/Berlin')).strftime('%m月%d日 %H時%M分')
st.write(cet_dst)

st.text("・ページを再読み込みすると時間が更新されます。")

d = {'lat': [52.51765309653922],
     'lon': [13.37801547866751]}
df = pd.DataFrame(data=d)
zoom = 4
st.map(df,zoom)