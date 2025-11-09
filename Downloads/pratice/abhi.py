import streamlit as st 
import requests

res = requests.get('https://www.freetogame.com/api/games?platform=pc')

if res.status_code == 200:
    games_data = res.json()
    cols = st.columns([0.5,6,4])
st.sidebar.title('Navigation')
option = st.sidebar.radio("choose a mode",['ok','okkk','okkkkk'])
print(option)
with cols[1]:
  search = st.text_input("search for a game", placeholder='search for a game',label_visibility='collapsed')

  if search == "":
    st.info('search for a game ')
  else:
    for game in games_data:
                    if search in game["title"].lower():
                        with st.container(border=True):
                            cols1 = st.columns([3, 2])
                        with cols1[0]:
                            st.write('ids',game["id"])
                            st.write('title', game["title"])
                            st.write('profile_url',game['freetogame_profile_url'])
                            st.link_button('play now',game["game_url"],type = 'primary')
                        with cols1[1]:
                    #  for game in games_data:
                    #    if search in game["title"].lower():
                            st.image(game['thumbnail'])
                    # st.write('hello')
with cols[2]:
       st.subheader('Navigation') 
       chusuko = st.radio('choose a choice',['ai recodemdations','songs'])
      #  index =1
       print(chusuko)
       if chusuko == 'songs':
            st.success('okay this is a good choice')