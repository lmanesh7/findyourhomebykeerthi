import streamlit as st
import pandas as pd
import socket
import time

df = pd.DataFrame()


@st.cache
def readFile():
    df = pd.read_csv("housing.csv")
    return df


df = readFile()
st.title("Find your home")
st.caption("A Mamillapalli Keerthi Project")

region = st.selectbox(
    'What are your region preferences?',
    ('select', 'albany', 'reno / tahoe', 'athens'))
state = st.selectbox(
    'State',
    ('select', 'ny', 'go'))

beds = st.slider("How many beds you want?", 0, 10, 2)

if st.button("Show Results"):
    with st.spinner('Hang tight! We are finding the best home for you.....'):
        time.sleep(3)
    df1 = df[(df.region == region) & (df.beds == beds) & (df.state == state)]
    st.balloons()

    st.write(df1)

    st.download_button('Download CSV', df1.to_csv(), "findyourhomebykeerthi.csv", 'text/csv')
