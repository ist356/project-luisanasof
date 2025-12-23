import pytest
import pandas as pd
import sys
import os
import code
from code.etl import get_demographics, get_social_demographics, get_social_responses
from code.codebook import mapping_dict

def test_should_pass():
    print("\nAlways True!")
    assert True

def test_get_mapped_dataframe():
    mapped_df = pd.read_csv(file)
    file = 'code/data/NPORS_2025_mapped.csv'
    print(f"TESTING: {file} file exists")
    assert os.path.exists(file)

    expected_rows = 4846
    expected_col_count = 24
    expected_col_names = ['respid', 'comtype2', 'smuse_fb', 'smuse_yt', 'smuse_x', 'smuse_ig',
       'smuse_sc', 'smuse_tt', 'smuse_rd', 'smuse_bsk', 'smuse_th', 'smuse_ts',
       'relig', 'educcat', 'party', 'hisp', 'racethn', 'agecat', 'birthplace',
       'gender', 'adults', 'inc_sdt1', 'cregion', 'metro']
    
    print("\nTesting row count of {expect_row_count}...")
    assert len(mapped_df) == expected_rows
    
    print("\nTesting column count of {expect_col_count}...")
    assert len(mapped_df.columns) == expected_col_count

    print("\nTesting column names are {expect_col_names}...")
    assert set(mapped_df.columns) == set(expected_col_names)

    
def test_get_social_responses():
    file = 'code/data/NPORS_2025_socials.csv'
    print(f"TESTING: {file} file exists")
    assert os.path.exists(file)

    mapped_df = pd.read_csv('code/data/NPORS_2025_mapped.csv')

    expected_rows = 48460
    expected_col_count = 3
    expected_col_names = ['respid', 'platform', 'response']
    
    socials_df = get_social_responses(mapped_df)

    print("\nTesting row count of {expect_row_count}...")
    assert len(socials_df) == expected_rows
    
    print("\nTesting column count of {expect_col_count}...")
    assert len(socials_df.columns) == expected_col_count

    print("\nTesting column names are  {expect_col_names}...")
    assert set(socials_df.columns) == set(expected_col_names)


def test_get_demographics():
    file = 'code/data/NPORS_2025_demographics.csv'
    print(f"TESTING: {file} file exists")
    assert os.path.exists(file)

    socials_df = pd.read_csv('code/data/NPORS_2025_socials.csv')

    expected_rows = 4846
    expected_col_count = 8
    expected_col_names = ['respid', 'Community Type', 'Religion', 'Education Level', 'Age group',
       'Gender', 'Family income', 'US region']
    
    demographics_df = get_demographics(socials_df)

    print("\nTesting row count of {expect_row_count}...")
    assert len(demographics_df) == expected_rows
    
    print("\nTesting column count of {expect_col_count}...")
    assert len(demographics_df.columns) == expected_col_count

    print("\nTesting column names are  {expect_col_names}...")
    assert set(demographics_df.columns) == set(expected_col_names)


def test_social_demographics():
    file = 'code/data/NPORS_2025_socials_demographics.csv'
    print(f"TESTING: {file} file exists")
    assert os.path.exists(file)

    socials_df = pd.read_csv('code/data/NPORS_2025_socials.csv')
    demographics_df = pd.read_csv('code/data/NPORS_2025_demographics.csv')

    expected_rows = 48460
    expected_col_count = 10
    expected_col_names = ['respid', 'platform', 'response', 'Community Type', 'Religion',
        'Education Level', 'Age group', 'Gender', 'Family income', 'US region']
    
    socials_demographics_df = get_social_demographics(socials_df, demographics_df)

    print("\nTesting row count of {expect_row_count}...")
    assert len(socials_demographics_df) == expected_rows
    
    print("\nTesting column count of {expect_col_count}...")
    assert len(socials_demographics_df.columns) == expected_col_count

    print("\nTesting column names are  {expect_col_names}...")
    assert set(socials_demographics_df.columns) == set(expected_col_names)
