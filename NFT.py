import pandas as pd
import numpy as np
from DataReader import CSVReader

#Takes a dataframe from CSVReader
#Returns the number of donations made with accounts
def count_accounts(df):
    return df[df["account"].isnull()==False].shape[0]
    
#Takes a dataframe from CSVReader
#Returns the number of donations where an nft was collected    
def count_nft(df):
    return df[df["nft_collected"].isnull()==False].shape[0]

#Takes a dataframe from CSVReader
#Returns a string describing the number of total donations in 2018, how many made with accounts, and how many of those collected an nft
def compareData(df):
    nft = count_nft(df)
    accounts = count_accounts(df)
    total =  df.shape[0]
    account_fraction = np.round(accounts/total*100, decimals = 3)
    nft_fraction = np.round(nft/accounts*100, decimals = 3)
    
    return "Of all {} donations through WeTrust in 2018, {}({}%) were made with accounts, and {}({}%) of those donations with accounts claimed an nft".format(df.shape[0], accounts, account_fraction, nft, nft_fraction)
    
reader = CSVReader("2018.csv")
df_temp = reader.get_df()
print(compareData(df_temp))