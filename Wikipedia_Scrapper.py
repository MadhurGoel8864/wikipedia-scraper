import streamlit as st
import requests
import pyperclip
from bs4 import BeautifulSoup
import pandas as pd
st.title("Wikipedia Scrapper ")
prefix = "https://www.google.com/search?q="
topic = st.text_input("Enter topic here")
a =st.button("Get Wikipedia Article")
corpus = ''
if st.button("Clear Input", key=1):
    corpus = ''
    topic = ''
    st.markdown(corpus)


if a==True:
    topic = topic.replace(' ','+')
    google_src_link = prefix + topic + '+wikipedia'
    res = requests.get(google_src_link)
    soup = BeautifulSoup(res.text,'html.parser')
    final_lnk = ''
    for i in soup.find_all('div'):
        try:
            lnk = i.find('a').get('href')
            if(lnk.find('https://en.wikipedia.org/wiki/') !=-1):
                x = lnk.split('&')
                final_lnk = x[0][7:]
                break
        except:
            pass
    res = requests.get(final_lnk)
    soup = BeautifulSoup(res.text,'html.parser')
    for p in soup.find_all('p'):
        corpus+= p.text
        corpus+='\n'

    st.markdown(corpus)




# print(corpus)