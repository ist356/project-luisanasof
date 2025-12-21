import pandas as pd
import numpy as np

#First, going to load the dataset we will be using into the data folder

path = path = r"C:\Users\luisa\OneDrive\Documents\fall 2025\ist356\project-luisanasof\code\data\NPORS_2025_for_public_release_FINAL.csv"

df = pd.read_csv(path)

df.head()


#methodology:

#DROP IRRELEVANT COLUMNS> center in on specific factors like demographics, age, etc

#The dataset began with 65 columns, which was an insane amount of information to work with (all of the original columns can be found in the attached codebook).
#I decided to work with the following topic: How did the US use social media in 2025?
#Inspired by the 

'''
dropped columns:

- data collection mode
- language respondent finished/started interview with
- interview start date
- interview end date
- unity column
- govprotect ()
- moregunimpact
-fin_sit (usehousehold income instead)
vet1(vet status--too many possible answers, complicated to work with)

- vol12_cps
#INTERNET (taking almost all out):
-eminuse
-intmob
-intfreq
-intfreqcollapse
-home4nw2
bbhome
#social media:
RADIO
DEVICE1A
SMART2
NHISLL
#religion:
- religcat1
-born
-attendonline2
- attendper
-relimp
-pray
(keeping PARTY, tho considering not including party line at all)
-partyln
-partysum



- registration


- voted2024
-votegen_post
- agegrp (age 4 categories was easier to work with)




'''
#dropped columns:

df_cleaned = df.drop(columns=['MODE',
                 'LANGUAGE', 
                 'LANGUAGEINITIAL', 
                 'INTERVIEW_START', 
                 'INTERVIEW_END', 
                 'ECON1MOD',
                 'ECON1BMOD',
                 'UNITY', 
                 'CRIMESAFE',
                 'GOVPROTCT', 
                 'MOREGUNIMPACT', 
                 'FIN_SIT', 
                 'VET1', 
                 'VOL12_CPS',
                 'EMINUSE',
                 'INTMOB',
                 'INTFREQ',
                 'INTFREQ_COLLAPSED',
                 'HOME4NW2',
                 'BBHOME',
                 'RADIO',
                 'DEVICE1A',
                 'SMART2',
                 'NHISLL',
                 'RELIGCAT1',
                 'BORN',
                 'ATTENDONLINE2',
                 'ATTENDPER',
                 'RELIMP',
                 'PRAY',
                 'REGISTRATION',
                 'PARTYLN',
                 'PARTYSUM',
                 'VOTED2024',
                 'VOTEGEN_POST',
                 'AGEGRP'], inplace=False)

df_cleaned.head()

df_cleaned.to_csv(r'C:\Users\luisa\OneDrive\Documents\fall 2025\ist356\project-luisanasof\code\data\NPORS_2025_cleaned.csv', index=False)

#now, have to transform the codes to their respective values from the codebook


#after that is done, make sure data is clean. 


#after that is done, we can start to work with the program

#how i envision it (streamlit dashboard)
#title: how did the us use social media in 2025?
#input some information below, and see how your social media usage compares to the rest of the country!
#input: age, ethnicity, household income? education, which of the following social media platforms did you use this year? (list of platforms)
#output: how your usage compares to the rest of your demographic profile (tabs for age, race, education level, 
# plus bottom metric of what percent of people in that profile used the different platforms listed))


