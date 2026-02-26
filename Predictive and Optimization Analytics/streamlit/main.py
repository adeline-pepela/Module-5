import streamlit as st
st.write("My first streamlit app")

st.set_page_config(
    page_title='Our streamlit app',
    page_icon=':smiley:',
    layout='wide'
)

#side bar
st.sidebar.title('Streamlit Dashboard')

section = st.sidebar.radio('Select a section', ['Home', 'Data', 'Model', 'Evaluation'])