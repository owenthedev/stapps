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
st.write("""# Sliding into your bank balance
 """)
st.write('## Compound Interest')
st.write('')
int_slider=st.slider('Interest rate %, Slide to choose your interest rate', min_value=1, max_value=20,key=1)
deposit=100
n=2
future_value=round((deposit*(1+(int_slider/100))**n),2)
st.write('your money would grow to the value of:')
st.write(f'## R{future_value}')
st.write(f'Assuming a R{deposit} deposit into a savings account over {n} years.')

st.write('')
st.write('')
st.write("## Simple Interest")
st.write('')
int_slidertwo=st.slider('Interest rate %, Slide to choose your interest rate', min_value=1, max_value=20,key=2)
future_valuetwo=deposit*(1+(int_slidertwo*n/100))

st.write('your money would grow to the value of:')
st.write(f'## R{future_valuetwo}')
st.write(f'Assuming a R{deposit} deposit into a savings account over {n} years')
st.write('')
st.write("""
Interesting Conclusion 
""")
st.write('Comparing the final result between the two types of interest we can see that, given the same initial deposit, time period and rate,compound interest is superior. Even though the standard is to offer compound interest rates, banks have tried to lure depositors by using a high simple interest rate to make it appear that their offer is better.')
#fp="https://raw.githubusercontent.com/owenthedev/stapps/main/applestock.csv"         
#df=pd.read_csv(filepath_or_buffer=fp)
