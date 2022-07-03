import datetime
import streamlit_authenticator as sth
import streamlit as st
import pandas as pd
import numpy as np
from my_code import df

st.title('Where I have been')
date=st.sidebar.date_input('Date', datetime.date(2022,6,1), min_value=datetime.date(2022,6,1), max_value=datetime.date(2022,7,1))
st.table(df.loc[date.strftime('%Y-%m-%d')][['Date', 'Day', 'Time', 'Place']])
