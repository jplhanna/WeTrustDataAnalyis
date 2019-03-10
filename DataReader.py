import pandas as pd
import numpy as np


#A class for reading in the WeTrust donor 2018 csv, is not generic, can be made so by rewording the __init__ to include file name, and inputing the file name at the beginning of pd.read_csv
class CSVReader:
    def __init__(self):
        self.df = pd.read_csv("2018.csv", header = 0, names = ["id", "cause", "amount", "date", "nft_collected", "account"] , index_col = 0, usecols = [0, 2, 3, 8, 17, 18], 
            dtype = {"id" : np.intp, "amount" : np.float64},
            parse_dates = ["date"], infer_datetime_format = True,
            skiprows =[x for x in range(168, 185)])
        
    #Returns a copy of the dataframe in order to keep the original intact, in case of changes during the runtime of another data analysis program
    def get_df(self):
        return self.df.copy()
        
    #Simpy returns the datatypes of the original dataframe stored in the class, probably not necessary
    def get_dtypes(self):
        return self.df.dtypes
        