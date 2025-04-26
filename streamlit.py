import streamlit as st
import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
import seaborn as sns

import yfinance as yf

st.title('A financial advisor with sentiment analysis')
st.header('This is gonna be a awesome project')
st.subheader('Steps to monetize this project')
st.write('Here is the plan to execute the project:')

# let's see the example of widgets

if st.checkbox('Show widgets'):
    st.write('This is a checkbox')
    st.write('This is a radio button')
    st.write('This is a select box')
    st.write('This is a multiselect box')
    st.write('This is a slider')
    st.write('This is a text input')
    st.write('This is a number input')
    st.write('This is a date input')
    st.write('This is a time input')
    st.write('This is a file uploader')
    

start_date = st.date_input('Start date', pd.to_datetime('2020-01-01'))
end_date = st.date_input('End date', pd.to_datetime('2023-01-01'))

symbol = st.text_input('Enter the stock ticker symbol', 'AAPL')

ticker_data = yf.Ticker(symbol)
ticker_df = ticker_data.history(period = '1d', start = start_date, end = end_date)

st.dataframe(ticker_df)

# let's create some charts

st.write('## closing price charts')
st.line_chart(ticker_df['Close'])

