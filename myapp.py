import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of dogs")
col1,col2=st.columns(2)
with col1:
  st.subheader("French Bulldogs")
  st.image("./French bulldog.jpg",caption="French Bulldogs",width=300,use_column_width=True)
  st.write("French Bulldogs are cute")
  with col2:
  st.subheader("Golden Retriver")
  st.image("./golden retriver.jpg",caption="Golden Retriver",width=300,use_column_width=True)
  st.write("Golden Retriver dogs are cute")
