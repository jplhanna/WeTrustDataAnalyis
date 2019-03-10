import pandas as pd
import numpy as np
from DataReader import CSVReader

#takes a dataframe from the CSVReader class which has had non users removed
#returns a dataframe containing the number of times a user donated, and the number of times they collected an NFT. Sorted by donation count in descending order
def count_repeats(df):
    return df.groupby("account").count().sort_values("amount", ascending = False)
    
#Takes a repeat dataframe, the output of count_repeats
#returns a sub dataframe containing only users that have donated more than once
def check_repeats(repeats):
    return repeats[repeats['cause']>1]
######################################
#This section of code was not finished and should not be used, it's purpose was to compare the amounts donated between returning and non returning users

#Takes a dataframe from CSVReader and check_repeats
#Returns a dataframe mask of the same shape as the dataframe from CSVReader where the row is True if the donation is from a user that has donated more than once
def repeat_mask(df, repeat):
    temp = []
    for x in df["account"]:
        temp.append(x in repeat.index)
    return pd.DataFrame({"cause":temp, "amount": temp, "date": temp, "nft_collected": temp, "account": temp}, df.index)

#Unfinished, should return the max donation from all returning users, all non returning users, all anonymous users
def check_highs(df, repeats):
    mask_temp = repeat_mask(df, repeats)
    df = df.where(mask_temp)
    df = df[df["account"].isnull()==False]
    return None

#Unfinished
def check_amounts(df):
    repeats_temp = count_repeats(df)
    true_temp = check_repeats(repeats_temp)
    check_highs(df, true_temp)
    return None
####################################

#Takes a dataframe from CSVReader
#Returns a string describing the total number of donations in 2018 made with accounts, the number of returning donors with accounts, the proportion of donations they make up. How many of those donations
#had an nft collected, and the highest number of donations by a returning donor.
def compare_repeats(df):
    repeats_temp = count_repeats(df)
    repeats_total = repeats_temp["cause"].sum()
    actual_repeats = check_repeats(repeats_temp)
    actual_sum = actual_repeats["cause"].sum()
    nft_sum = actual_repeats["nft_collected"].sum()
    nft_max = actual_repeats["nft_collected"].max()
    
    repeat_fration = np.round(actual_sum / repeats_total * 100, decimals = 3)
    nft_fraction = np.round(nft_sum / repeats_total * 100, decimals = 3)
    
    return "Of the {} donations made with accounts in 2018, {} accounts donated more than once, making up a total of {}({}%) of those donations.\nFrom those donations, only {}({}% of all account donations) nfts were collected, with the most collected from any single account being {}.\nAnd, the highest repeated donor donating {} times.".format(
        repeats_total, actual_repeats.shape[0], actual_sum, repeat_fration, nft_sum, nft_fraction, nft_max, repeats_temp.iloc[0]["cause"])


reader = CSVReader("2018.csv")
df_temp = reader.get_df()


print(compare_repeats(df_temp))
#check_amounts(df_temp)
