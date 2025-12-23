import pandas as pd
import streamlit as st
import seaborn as sns
import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="wide")

st.title("How did the U.S. use social media in 2025?")
st.subheader("See how Americans in different demographics used social media this year.")

path = 'code/data/NPORS_2025_socials_demographics.csv'
df = pd.read_csv(path)

#Demographics input questions:
col1, col2 = st.columns(2, vertical_alignment='center')

age = st.select_slider(label="What is your age group?",
         options=["18-29", "30-49", "50-64", "65+"])

with col1:
    gender = st.radio(label='Describe your gender:',
            options=['A man', 'A woman', 'In some other way'])
with col2:
    education = st.selectbox(label="Select your education level:",
                options=["College graduate+", "Some College", "H.S. graduate or less"])

income = st.select_slider(label="What is your family income?",
         options=["Less than $30,000", 
                  "$30,000 to less than $40,000", 
                  "$40,000 to less than $50,000",
                  "$50,000 to less than $70,000",
                  "$70,000 to less than $100,000",
                  "$100,000 to less than $125,000",
                  "$125,000 to less than $150,000",
                  "$150,000 or more"])

#Filtering the dataframe
filtered_df = df[(df['Age group']==age) & (df['Gender']==gender) & (df['Education Level']==education) & (df['Family income']==income)]
#Adding a 'count' column to be able to aggregate social media data
filtered_df['count'] = 1
#st.dataframe(filtered_df)

#Aggregating for visualizations

#Respondent counts for metrics
responder_count = filtered_df['respid'].unique().size
total_respondent_count = df['respid'].unique().size
respondent_percent = round((responder_count/total_respondent_count)*100, 2)

agg_df = filtered_df.groupby(['platform', 'response'])['count'].sum().reset_index()
#st.dataframe(agg_df)

#Metrics

col1, col2 = st.columns(2, vertical_alignment='bottom')

with col1:
    st.metric(label='No. respondents of this profile:',
            value=responder_count)
with col2:
    st.metric(label='Percent of respondents with this profile:',
            value=f"{respondent_percent}%")

#Visualizations
#creating a colormap to maintain legend consistent:
color_map = {
    "Yes, use this": "#59F2B9",
    "No, don't use this": "#F26D59",
    "Refused/Web blank": "#D3D3D3"
}

if responder_count > 0:
    bargraph = px.bar(agg_df,
                    x='platform',
                    y='count',
                    color='response',
                    barmode='group',
                    color_discrete_map=color_map)
    st.plotly_chart(bargraph)
else:
    st.error("No respondents matching this profile")

# 
st.caption(body=f"Responder count: {responder_count}")


