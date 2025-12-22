import pandas as pd
import streamlit as st
import seaborn as sns
import folium
import geopandas as gpd
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(layout="centered")

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
#sliced_df = filtered_df[demographics]
#st.dataframe(sliced_df)

#Aggregating for visualizations
#Adding a 'count' column to be able to aggregate social media data
filtered_df['count'] = 1
agg_df = filtered_df.groupby(['platform', 'response']).sum('count').reset_index()
#st.dataframe(agg_df)
responder_count = agg_df['count'].sum()

#Visualizations

#creating a colormap to maintain legend consistent:
import plotly.express as px

# Define a consistent color mapping
color_map = {
    "Yes, use this": "#008ecc",
    "No, don't use this": "#Ff6f61",
    "Refused/Web blank": "#CCCCCC"
}

bargraph = px.bar(agg_df,
                  x='platform',
                  y='count',
                  color='response',
                  barmode='group',
                  color_discrete_map=color_map)

st.plotly_chart(bargraph)
st.caption(body=f"Responder count: {responder_count}")



# st.radio("Which of these best describes your community?",
#          options=["Urban",
#                   "Suburban",
#                   "Rural",
#                   "None of these/Other"])

# st.radio(label="What is your level of education?")


# st.selectbox(label="What is your race/ethnicity? (Select the best option)",
#          options=["White non-Hispanic",
#         "Black non-Hispanic",
#         "Hispanic",
#         "Other",
#         "Asian non-Hispanic",
#         "Prefer not to answer"])

# st.map
# # st.radio(label=)
# # st.radio(label=)
