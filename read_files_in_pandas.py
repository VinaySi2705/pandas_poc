import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dframe = pd.read_csv('data/btc-market-price.csv')
# one row of data becomes header in the above case

dframe = pd.read_csv('data/btc-market-price.csv', header=None)
# print(dframe)

# we can set the name of each column explicitely by setting the df.columns attribute:
dframe.columns = ['timestamp', 'price']
print(dframe.head())  # by default .head() will show 5 rows
print('Shape of data is', dframe.shape)
print('types of data is->\n', dframe.dtypes)

# using this we intrepet the type of timestamp to datetime as previously it is of object type
dframe['timestamp'] = pd.to_datetime(dframe['timestamp'])
print(dframe.head())
print('now data type is-> \n', dframe.dtypes)

# now we change the timestamp as the index of the dataframe
# this will set the index of data frame
dframe.set_index(['timestamp'], inplace=True)
print(dframe.head())

# for accessing any row with the help of index
print(dframe.loc['2017-04-03'])
