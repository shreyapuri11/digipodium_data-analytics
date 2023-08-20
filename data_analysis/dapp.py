import streamlit as st
# run in terminal
# cd data_analysis
# streamlit run dapp.py

#reactive apps are formed using streamlit in python

import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns

#title of the app
st.title('Data Analysis App')

#st.set_page_config(layout="wide")

st.cache_data()
def load_data():
    df= sns.load_dataset('titanic')
    return df

with st.spinner('Loading Data....'):
    df = load_data()
    st.write("🎉🎉🎉")

cat_cols= df.select_dtypes(exclude=np.number).columns.tolist()
num_cols= df.select_dtypes(include=np.number).columns.tolist()

if st.checkbox("View the Data"):
    st.dataframe(df)

if st.checkbox("Show some statistics"):
    st.text(num_cols)
    st.text(cat_cols)

    c1,c2= st.columns(2)
    c1.metric(label="Average age of passengers",value=df['age'].mean().astype(int))
    c2.metric(label="Average fare",value=df['fare'].mean().astype(int),delta=round(df['fare'].std(),1)) # delta used for difference btw the values


    c1,c2= st.columns(2)
    c1.text("Number of survivors")
    survivors= df['survived'].value_counts()
    c1.dataframe(survivors)
    fig= px.pie(survivors,survivors.index,survivors.values)
    c1.plotly_chart(fig,use_container_width=True)
    c2.text("number of passengers in each class")
    classes = df['pclass'].value_counts()
    c2.dataframe(classes)
    fig= px.bar(classes, classes.index,classes.values)
    c2.plotly_chart(fig,use_container_width=True)


    # choose by the user
if st.checkbox("Visualize categorical data"):
    st.subheader("Categorical data visualization ")
    sel_col=st.radio("Select column",cat_cols,horizontal=True)
    sel_col_count= df[sel_col].value_counts()
    fig = px.pie(sel_col_count,sel_col_count.index,sel_col_count.values,title=f"Distribution of {sel_col}")
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox("visualize numerical data"):
    graph_types= ['Area','Line','Histogram','Boxplot','Violinplot']
    st.subheader("Numerical data Visualiztion")
    sel_col= st.selectbox("Select columns",num_cols)
    graph_type= st.radio("Select Graph types",graph_types,horizontal=True)

    if graph_type== graph_types[0]:
        fig=px.area(df,y=sel_col,title=f"area plot of {sel_col}")
        fig2=px.histogram(df,y=sel_col,title=f"histogram of {sel_col}")
        c1,c2= st.columns(2)
        c1.plotly_chart(fig,use_container_width=True)
        c2.plotly_chart(fig2,use_container_width=True)
    
    if graph_type== graph_types[1]:
        fig=px.line(df,y=sel_col,title=f"line plot of {sel_col}")
        st.plotly_chart(fig,use_container_width=True)
    if graph_type== graph_types[2]:
        fig=px.histogram(df,x=sel_col,title=f" Histogram of {sel_col}")
        st.plotly_chart(fig,use_container_width=True)
    if graph_type== graph_types[3]:
        fig=px.box(df,x=sel_col,title=f"Boxplot of {sel_col}")
        st.plotly_chart(fig,use_container_width=True)
    if graph_type== graph_types[4]:
        fig=px.violin(df,x=sel_col,title=f"violinplot of {sel_col}")
        st.plotly_chart(fig,use_container_width=True)
    