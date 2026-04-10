import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load our dataset for Remote Work & Mental Health Dataset
df = pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")

# count missing values per column
missing = df.isnull().sum()
print("Missing values per column:")
print(missing)

# percentage of total rows
print("\nMissing as % of total:")
print((missing / len(df) * 100).round(2))

