import pandas as pd
import numpy as np
from codebook_copy import mapping_dict

socialmedia_cols = ['smuse_fb', 'smuse_yt', 'smuse_x', 'smuse_ig', 'smuse_sc', 'smuse_tt', 'smuse_rd', 'smuse_bsk', 'smuse_th', 'smuse_ts']

demographic_cols = ['comtype2', 'relig', 'educcat', 'party', 'hisp', 'racethn', 'agecat', 'birthplace', 'gender', 'adults', 'inc_sdt1', 'cregion', 'metro']
#use the following column selection below for the get_demographics call:
selected_demographic_cols = ['comtype2', 'relig', 'educcat', 'agecat', 'gender', 'inc_sdt1', 'cregion']

socials_map = {
    "smuse_fb": "Facebook",
    "smuse_yt": "YouTube",
    "smuse_x": "X",
    "smuse_ig": "Instagram",
    "smuse_sc": "Snapchat",
    "smuse_tt": "TikTok",
    "smuse_rd": "Reddit",
    "smuse_bsk": "Bluesky",
    "smuse_th": "Threads",
    "smuse_ts": "TruthSocial",
}

demographics_column_map = {
'comtype2': 'Community Type', 
'relig': 'Religion', 
'educcat': 'Education Level', 
'party': 'Political Party', 
'hisp': 'Hispanic?', 
'racethn': 'Race/Ethnicity', 
'agecat': 'Age group', 
'birthplace': 'Birthplace', 
'gender': 'Gender', 
'adults': 'Household size (adults)', 
'inc_sdt1': 'Family income', 
'cregion': 'US region', 
'metro': 'Metropolitan area?'
}

npors_df = pd.read_csv('/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_for_public_release_FINAL.csv')

def get_mapped_dataframe(npors_df: pd.DataFrame) -> pd.DataFrame:
    npors_df_cleaned = npors_df.drop(columns=['MODE',
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
                 'AGEGRP', 'BASEWT', 'WEIGHT', 'RACECMB', 'STRATUM', 'SMUSE_WA'], inplace=False)

    cols_to_map = ['comtype2', 'smuse_fb', 'smuse_yt', 'smuse_x', 'smuse_ig',
       'smuse_sc', 'smuse_tt', 'smuse_rd', 'smuse_bsk', 'smuse_th', 'smuse_ts',
       'relig', 'educcat', 'party', 'hisp', 'racethn', 'agecat', 'birthplace',
       'gender', 'adults', 'inc_sdt1', 'cregion', 'metro']

    mapped_df = npors_df_cleaned

    mapped_df.columns = mapped_df.columns.str.lower()

    for col in cols_to_map:
        mapped_df[col] = mapped_df[col].map(mapping_dict[col])

    mapped_df = mapped_df.dropna()

    mapped_df.to_csv('/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_mapped.csv', index=False)
    return mapped_df

def get_social_responses(mapped_df: pd.DataFrame) -> pd.DataFrame:

    '''
    Returns a dataframe that brings social media columns and respondents' answers down into one column.
    The resulting dataframe will have just 3 columns: respondent id, platform, and user response about their usage.
    '''
    socials_df = mapped_df.melt(
        id_vars= 'respid',
        value_vars=socialmedia_cols,
        var_name='platform',
        value_name='response',
        ignore_index=False
    ).copy()

    socials_df['platform'] = socials_df['platform'].map(socials_map)
    socials_df.to_csv('/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_socials.csv', index=False)
    return socials_df

def get_demographics(mapped_df: pd.DataFrame, demographics: list) -> pd.DataFrame:
    '''
    Return a dataframe with demographic columns of choice.
    '''
    #adding back the respid column for identification
    mapped_df = get_mapped_dataframe(npors_df)
    cols = ['respid'] + demographics
    demographics_df = mapped_df[cols].copy()
    for col in demographics:
        demographics_df = demographics_df.rename(columns=demographics_column_map)
    demographics_df.to_csv('/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_demographics.csv', index=False)
    return demographics_df

def get_social_demographics(socials_df: pd.DataFrame, demographics_df: pd.DataFrame) -> pd.DataFrame:
    '''
    Utilizing the 3-col socials dataframe, attach respondent demographics, creating a new dataframe.
    '''
    socials_demographics_df = socials_df.merge(right=demographics_df,
                                               how='left',
                                               on='respid')
    socials_demographics_df.to_csv('/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_socials_demographics.csv', index=False)
    return socials_demographics_df

if __name__ == '__main__':
    '''
    Main ETL job. 
    '''
    npors_df = pd.read_csv('/Users/luisanasof/Desktop/Undergrad Classes and Docs/Fall 2025/Classes/IST356/assignments/project-luisanasof/code/data/NPORS_2025_for_public_release_FINAL.csv')

    mapped_df = get_mapped_dataframe(npors_df)

    get_demographics(mapped_df,selected_demographic_cols)