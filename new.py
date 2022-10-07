import streamlit as st
import pandas as pd
import socket
import time

df = pd.DataFrame()


@st.cache
def readFile():
    df = pd.read_csv("housing.csv")
    return df


@st.cache
def get_regions(df):
    return df["region"].unique()


@st.cache
def get_states():
    return tuple(df["state"].unique())


def write_descriptions(df2):
    j = 0
    for (region,phone,latitude,longitude,description) in zip(df2.region, df2.id, df2.lat, df2.long, df2.description):

        with st.container():
            st.write("Region:",region)
            st.write("Contact: ", phone)
            st.write("Latitude: ",latitude)
            st.write("Longitude: ", longitude)
            st.write("Description: \n", description)


    st.write()


df = readFile()
st.title("Find your home")
st.caption("A Mamillapalli Keerthi Project")
regions = get_regions(df)
regions = tuple(regions)
states = get_states()
region = st.selectbox(
    'What are your region preferences?',
    regions)
state = st.selectbox(
    'State',
    states)

beds = st.slider("How many beds you want?", 0, 10, 2)
sqfeet = st.slider("Square feets: ",100,10000)
price = st.slider("Let us know your price range: ",1,2000,865)

if st.button("Show Results"):
    with st.spinner('Hang tight! We are finding the best home for you.....'):
        time.sleep(3)
    df1 = df[(df.region == region) & (df.beds >= beds) & (df.state == state) & (df.price <= price) & (df.price != 0) & (df.sqfeet <= sqfeet )& (df.sqfeet>=100)]
    if df1 is not None and len(df1.axes[0]) > 1:
        st.balloons()
    if df1 is None or len(df1.axes[0]) <= 1:
        st.write("Oops! looks like there is no home for these filters at this moment")
    else:

        #st.write(df1)

        st.download_button('Download CSV', df1.to_csv(), "findyourhomebykeerthi.csv", 'text/csv')
        write_descriptions(df1)
