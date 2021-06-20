# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:32:32 2021

@author: owenn
"""

import numpy as np
import pandas as pd
import streamlit as st
st.write("""
         # This week on Stocks
         We look into the king of fanboyism, Apple!
         
         """)

fp="C:/Users/owenn/data/datasets/applestock.csv"         
df=pd.read_csv(filepath_or_buffer=fp)
st.write('')
st.write('-    Apple Stock over the past 5 years')
st.line_chart(df)