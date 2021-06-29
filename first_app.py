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
         ## We look into the king of fanboyism, Apple!
         29 June, 2021
         
         Owen Nxumalo
         """)
st.image('https://www.apple.com/newsroom/images/live-action/wwdc-2021/Apple_WWDC21-Apple-Design-Awards_061021_big.jpg.large_2x.jpg')
fp="https://raw.githubusercontent.com/owenthedev/stapps/main/applestock.csv"         
df=pd.read_csv(filepath_or_buffer=fp)
st.write("""
         # Apple
         ## Apple Stock over the past 5 years""")
st.write('')         
st.line_chart(df)
st.write('')
st.write("""
         The trend of the stock is an upward trend.
         However, we would benefit from additional information
         """)
st.write('')
st.write('# Stock Statistics:')

#Descriptive Statistics, mean ,variance, max , min
max=round(df['Open'].max(),2)
min=round(df['Open'].min(),2)
day_of_max=df['Open'].argmax()
day_of_min=df['Open'].argmin()
days_since_max=len(df)-day_of_max
days_since_min=len(df)-day_of_min
#This is a function that calculates the average. We could put this into its own file
def average(dataf):
    total=0
    n=len(dataf)
    for i in range(n):
        #df['Field'].iloc[0] gets the first record under the Field column in df DataFrame
        total=total+dataf['Open'].iloc[i]
    mean=round(total/n,2)
    return mean
def variance(dataf):
    total=0
    diff=0
    aver=dataf['Open'].mean()
    n=len(dataf)
    for i in range(n):
        diff=aver-dataf['Open'].iloc[i]
        total=total +diff*diff
    varr=round(total/(n-1),2)
    return varr
avg=average(df)
vary=variance(df)
st.write(f'The maximum share price was ${max} was reached {days_since_max} days ago')
st.markdown("""_max=round(df['Open'].max(),2)_""") # see *
st.markdown('_Markdown_') # see *
st.write('')
st.write(f'The minimum share price was ${min}, which was {days_since_min} days ago')
st.write('')
st.write(f'The average share price over the period was ${avg}')
st.write(f'The variance of the stock prices is {vary}')
st.video('https://www.youtube.com/watch?v=8w4qPUSG17Y')
st.audio('https://github.com/owenthedev/stapps/blob/main/TommyV%20%26%20Sam%20Mkhize%20-%20This%20Feeling%20(Original%20Mix).mp3')

