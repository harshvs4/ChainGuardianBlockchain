import numpy as np
import pandas as pd

#merge two csv files

df1 = pd.read_csv('simulated_transactions.csv')
df2 = pd.read_csv('/Users/harshsharma/Desktop/Hackathons/ChainGuardian/files/transactions.csv')

df = pd.concat([df1, df2], ignore_index=True)

df.to_csv('merged_file.csv', index=False)