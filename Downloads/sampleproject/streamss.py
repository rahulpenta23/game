import streamlit as st
import requests 

res = requests.get("https://www.freetogame.com/api/games?platform=pc")

if res.status_code == 200: 
    res = res.json()
    tracks = res['title']
cols = st.columns([0.3, 3, 0.3])
with cols[1]:
        st.subheader('Musicon')
        search_phrase = st.text_input('Search a Track', placeholder='🔍  Search a Track', label_visibility='collapsed')
        for track in tracks:
            if search_phrase in res['title']:
            #   with st.container(border=True):
                st.write('ok')