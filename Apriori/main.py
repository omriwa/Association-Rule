# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Market_Basket_Optimisation.csv',header=None)
transactions = []

for i in range(0, len(dataset)):
    transactions.append([])
    for j in range(0, len(dataset.iloc[i])):
        if(pd.notna(dataset.iloc[i][j])):
            transactions[i].append(dataset.iloc[i][j])

# Training the model
from apyori import apriori

rules = apriori(transactions=transactions, min_support=0.003, min_confidence=0.2, min_lift=3,min_length=2, max_length=2)




# Visualizing the prediction



