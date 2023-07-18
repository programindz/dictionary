import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie

st.set_page_config(
     page_title="Dictionary By programindz",
     page_icon=":book:",
     layout="wide",
     menu_items={
        'Get help': "https://google.com/",
        'About': "Made With Love And Lots Of Efforts!!"
     }
 )
@st.cache_data
def get_json(url):
   req = requests.get(url)
   if req.status_code != 200:
      return None
   return req.json()

@st.cache_data
def get_definition(word):
   url = "https://dictionary-by-api-ninjas.p.rapidapi.com/v1/dictionary"

   querystring = {"word": word}

   headers = {
      "X-RapidAPI-Host": "dictionary-by-api-ninjas.p.rapidapi.com",
      "X-RapidAPI-Key": "1bb4ae38e4msh41488d47c23c2bep1ceec9jsncf9727ecbf11"
   }

   response = requests.request("GET", url, headers=headers, params=querystring)
   if response.status_code != 200:
      return None

   definition = json.loads(response.text)
   return definition['definition']


animation_book = get_json("https://assets1.lottiefiles.com/packages/lf20_xwgclkyh.json")

with st.container():
   left, right = st.columns([2, 1])
   with left:
      st.title(":books:  DICTIONARY")
      st.caption("By *programindz*")

      word = st.text_input("What are you looking for?", placeholder = "Search for a word")
      button = st.button("Search", help = "Search for the word")
   with right:
      st_lottie(animation_book, height = 280)

     

st.write("---")
if button:
   with st.spinner("Loading...."):

      if word == "":
         st.warning("**Enter Word Please!**")
      else:
         with st.container():
            col1, col2 = st.columns(2)

            with col1:
               st.subheader("Definition")
               defi = get_definition(word)

               defi = defi.split("3." and "2.")
               st.info(defi[0])

               try:
                  st.info("2. " + defi[1].split("3.")[0])
               except:
                  pass


            with col2:
               st.subheader("Thesaurus")
               st.markdown("***Working on this***")


