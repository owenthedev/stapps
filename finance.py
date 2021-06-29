# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 18:32:32 2021
@author: owenn
"""
import numpy as np
import pandas as pd
import streamlit as st
st.title("This week on Stocks")
st.write("""
         ## Interest(ing): Simple vs Compound
         30 June, 2021
         
         Owen Nxumalo
         """)
st.image('https://images.unsplash.com/photo-1579621970795-87facc2f976d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mzd8fGZpbmFuY2V8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=700&q=60')
st.write('Not sure who it was, but someone said that compund interest is the 8th wonder of the world. This person said so because it has a powerful effect on growth as time goes on.')

st.write('')
st.write('# Sliding into your bank balance')
int_slider=st.slider('Interest rate %, Slide to choose your interest rate', min_value=1, max_value=20)
deposit=100
n=2
future_value=round((deposit*(1+(int_slider/100))**n),2)
st.write(f'Assuming a R{deposit} deposit into a savings account over {n} years, your money would grow to the value of:')
st.write(f'## R{future_value}')
#fp="https://raw.githubusercontent.com/owenthedev/stapps/main/applestock.csv"         
#df=pd.read_csv(filepath_or_buffer=fp)
