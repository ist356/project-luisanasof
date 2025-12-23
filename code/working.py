import pandas as pd
import numpy as np
import codebook

#This file is mainly for scratch notes, trynig out code eetc. 
#not exacttly in order but does demonstrate how I thought through the logic of the program

# agg_df = pd.pivot_table(filtered_df,
#                         values=['response'],
#                         index=['respid'],
#                         columns=['platform', 'response'],
#                         aggfunc="sum")

# agg_df = pd.melt(filtered_df,
#                  id_vars= 'respid',
#                  value_vars='platform',

                 
#                         values=['response'],
#                         index=['respid'],
#                         columns=['platform','response'],
#                         aggfunc="count")



#path = '/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_for_public_release_FINAL.csv'
dems= '/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_demographics.csv'
soc_dem = '/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_socials_demographics.csv'

#df = pd.read_csv(path)
df1 = pd.read_csv(dems)
df2 = pd.read_csv(soc_dem)

df.isna().sum()
#has na
df1.isna().sum()
df2.isna().sum()

path = '/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_socials_demographics.csv'
df = pd.read_csv(path)

#print(df[df["Age group"]=='Refused'].sum())



print((df['Education Level']=='Refused').sum())
print(df[df['Family income']=="Refused/Web blank"].sum())
print(df[df["Gender"]=="Refused/Web blank"].sum())

#df_test


# df.dropna(inplace=True)
# df.info()
# df.drop(columns=['BASEWT','WEIGHT',])

# #First, going to load the dataset we will be using into the data folder

# path = '/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_for_public_release_FINAL.csv'
# df = pd.read_csv(path)

# df.head()


# #methodology:

# #DROP IRRELEVANT COLUMNS> center in on specific factors like demographics, age, etc

# #The dataset began with 65 columns, which was an insane amount of information to work with (all of the original columns can be found in the attached codebook).
# #I decided to work with the following topic: How did the US use social media in 2025?
# #Inspired by the 

# '''
# dropped columns:

# -stratum
# - data collection mode
# - language respondent finished/started interview with
# - interview start date
# - interview end date
# - unity column
# - govprotect ()
# - moregunimpact
# -fin_sit (usehousehold income instead)
# vet1(vet status--too many possible answers, complicated to work with)

# - vol12_cps
# #INTERNET (taking almost all out):
# -eminuse
# -intmob
# -intfreq
# -intfreqcollapse
# -home4nw2
# bbhome
# #social media:
# -smuse_wa (messaging platform, not social media)
# RADIO
# DEVICE1A
# SMART2
# NHISLL
# #religion:
# - religcat1
# -born
# -attendonline2
# - attendper
# -relimp
# -pray
# (keeping PARTY, tho considering not including party line at all)
# -partyln
# -partysum



# - registration


# - voted2024
# -votegen_post
# - agegrp (age 4 categories was easier to work with)




# '''
# #dropped columns:

# df_cleaned = df.drop(columns=['MODE',
#                  'LANGUAGE', 
#                  'LANGUAGEINITIAL', 
#                  'INTERVIEW_START', 
#                  'INTERVIEW_END', 
#                  'ECON1MOD',
#                  'ECON1BMOD',
#                  'UNITY', 
#                  'CRIMESAFE',
#                  'GOVPROTCT', 
#                  'MOREGUNIMPACT', 
#                  'FIN_SIT', 
#                  'VET1', 
#                  'VOL12_CPS',
#                  'EMINUSE',
#                  'INTMOB',
#                  'INTFREQ',
#                  'INTFREQ_COLLAPSED',
#                  'HOME4NW2',
#                  'BBHOME',
#                  'RADIO',
#                  'DEVICE1A',
#                  'SMART2',
#                  'NHISLL',
#                  'RELIGCAT1',
#                  'BORN',
#                  'ATTENDONLINE2',
#                  'ATTENDPER',
#                  'RELIMP',
#                  'PRAY',
#                  'REGISTRATION',
#                  'PARTYLN',
#                  'PARTYSUM',
#                  'VOTED2024',
#                  'VOTEGEN_POST',
#                  'AGEGRP'], inplace=False)

# df_cleaned.head()


# df_cleaned.drop(columns =['STRATUM', 'SMUSE_WA'], inplace=True)

# #df_cleaned.to_csv('/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_cleaned.csv', index=False)

# df_cleaned.isna().sum()
#now, have to transform the codes to their respective values from the codebook

#want to first try ths out with a subset of the dataframe:
#df_test

#after that is done, make sure data is clean. 


#after that is done, we can start to work with the program
'''
How I envision it (st dashboard)




'''
#title: how did the us use social media in 2025?


#ETL:
#first create the filtered DFs
#then save to cache
#then 
#finally create final program
#then: TESTS, explanation, reflection
#function

#socialmedia_cols = ['smuse_fb', 'smuse_yt', 'smuse_x', 'smuse_ig', 'smuse_sc', 'smuse_tt', 'smuse_rd', 'smuse_bsk', 'smuse_th', 'smuse_ts']
#for index, row in df.iterrows():
    #if
