import pandas as pd
import os
import numpy as py
import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
from DataReader import CSVReader


#Takes a dataframe from CSVReader
#Creates or edits a .svg file, which will contain a scatter plot of the donation in 2018, dates to ammount donated.
def plot_donations(df):
    fig, ax = plt.subplots(1, 1)
    df.sort_values("date",inplace=True)
    ax.plot_date(df["date"], df["amount"])
    plt.gca().set_xlabel("Date(yyyy-mm-dd)")#Label x axis
    plt.gca().set_ylabel("Crypto Donations in multiples of 1e20")#Label y axis
    plt.gca().set_title("All 2018 donations to WeTrust")#Title the graph
    for spine in plt.gca().spines.values():#Remove graph edges
        spine.set_visible(False)
    plt.tick_params(top = False, bottom = False, left = False, right = False, labelleft=True, labelbottom = True) #Remove all ticks from the graph edges
    plt.grid(True, alpha = 0.8)#Turn on the grid instead to better understand the ammounts being donated
    plt.yticks([0.0, 2.5 * 1e18, 7.5 * 1e18, 0.2 * 1e20, 1e20], ["",.025,.075,.2,1])#Reformat the yaxis ticks to more closely label according to the values that the donations actually fall on.
    fig.savefig("CauseGraph.svg")
    
reader = CSVReader()
df_temp = reader.get_df()
plot_donations(df_temp)