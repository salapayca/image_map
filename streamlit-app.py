# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 09:32:36 2023

@author: ssalapayca
"""

import streamlit as st

st.title('Images that I have taken all over the world!')
st.write('A map depicting my sight-seeings in the World!')

@st.cache_data()
def get_my_map():
  HtmlFile = open("map.html", 'r', encoding='utf-8')
  bcn_map_html = HtmlFile.read()
  return bcn_map_html

bcn_map_html = get_my_map()

import streamlit.components.v1 as components

with st.container():
  components.html(bcn_map_html,width=1000, height=1000)
