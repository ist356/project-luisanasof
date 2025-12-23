# About My Project

Student Name:  Luisana
Student Email:  lsortiz@syr.edu

### What it does

This is an interactive dashboard where users can input basic demographic information and retrieve a "snapshot" of how Americans with a similar profile used different social media platforms this past year.

### How you run my project

Before anything, make sure the required packages are installed. They can be found in the 'requirements.txt' folder.

Follow the instructions below:
1. From VS Code, open a terminal: Menu => Terminal => New Terminal
2. In the terminal, type and enter: `pip install -r requirements.txt`

Step 1: etl.PY
After that is done, go to the etl.py file to create the necessary dataframes through the ETL. Each function is built to 1. create a csv file under the code/data folder and 2. return a dataframe of the given docstring constraints. Call each function in the order that it appears in the etl.py file, as the output from the previous function will be the input for each following one.

Before starting, you should have 2 dataframes under the code/data folder:
- 'NPORS_2025_for_public_release_FINAL.csv'.
- ''NPORS_2025_coded'

The first function will create a transformed, cleaned and mapped version of the original dataframe, 'NPORS_2025_for_public_release_FINAL.csv'. In the transformation step, it will drop all irrelevant columns (more information on selection process below), all null rows, and transform column names to lowercase. Finally, it will replace the coded values with their categorical equivalents based on the included NPORS 2025 codebook.
**NOTE: the included 'NPORS_2025_coded' dataset is a coded version of the mapped dataset.

The rest of the functions are pretty straightforward, and more information is included in each of their docstrings. One function that should be noted is the get_demographics function, which requires a list of demographic columns as a parameter. While working on the functions, I was unsure what demographic selections I wanted, so I included all of them. I ended up only utilizing gender, education, income and age group, but didn't filter the dataset to just include these four (so that in the future I might build a more extensive project where users can choose what demographics to build for a profile themselves, perhaps).

At the end of this step, you should have 4 new dataframes:

- NPORS_2025_mapped.csv
- NPORS_2025_socials.csv
- NPORS_2025_demographics.csv
- NPORS_2025_socials_demographics.csv

Step 3. test_etl.
After all dataframes are completed, run all tests in the above file to make sure they were constructed correctly.

Once all tests pass, you can move on to the final step, which is initializing and playing with the dashboard!

Step 3: dashboard.py

Run this file using the streamlit configuration in the 'Run and Debud' page in VSCode. The program should look like the one pictured in 'dashboard-sc.png'.

The program is built to be engaging and simple for users to follow. Once you "build" the demographic profile you are interested in looking at, the barchart will automatically reset to reflect respondent answers matching your selections. Right above the barchart are two metrics: the first will tell you how many respondents from the survey matched your profile--reflected again at the bottom of the barchart to remind users that this serves as the chart's sample size-- and the second will say what percent of all respondents from the social_demographics dataframe match this profile.

### Other things you need to know

This dashboard is built on a survey dataset by the Pew Research Center, where each row is one respondent and each respondent has a unique ID, or 'respid'. The original dataset had 65 columns and just over 5,000 rows, and values were coded based on a provided codebook (included in this project as 'NPORS_2025_codebook_FINAL.txt'). After irrelevant columns and null-value rows were dropped, and categorical values were mapped onto coded ones based on the codebook, the final cleaned and transformed dataset had just 24 columns and nearly 4850 rows. I created a function to do this in the etl.py file.

One important thing to note is the "refused" answer category. Respondents were given the option to refuse to answer a question, and rather than mark their answer as a null the codebook reported their answer as such. Within the socials_demographic dataset utilized in the dashboard, only about 1% of all cells contain this value, so it is not too dense in this sense.
For the sake of simplicity, the final dashboard does not allow users to "refuse" to answer one of the demographic questions, but it does include this as a category in the bar chart demonstrating respondents' social media usage.

Below is a list of all dropped columns. Besides those irrelevant to the topic of social media usage, I also removed the WhatsApp usage 'SMUSE_WA' column, as, in my opinion, it is a messaging app and not a social media platform.

['MODE',
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
                 'AGEGRP', 'BASEWT', 'WEIGHT', 'RACECMB', 'STRATUM', 'SMUSE_WA']    
