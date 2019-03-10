This is a small project for analyzing a donation dataset from the WeTrust organization.
In order to run any file it is required to have >=python3.4, numpy, pandas, and matplotlib
DataReader is contains the main class for reading csv of the dataset, it is now generic and can read any file of the same format
NFT.py contains a small pandas program which ultimately calculates and compares the number of donors that collected nfts
Repeats.py contains a small pandas program which currently calculates and compares how many donors are returning users, it is unfinished with it's extra comparisons.
Plot.py contains a small pandas program which creates a scatter plot of date to ammmount, all donations.