import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load our dataset for Remote Work & Mental Health Dataset
df = pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")

# to ook at the first 5 rows
print(df.head())

# to look at a random sample — sometimes more revealing than the first rows
print(df.sample(5, random_state=10))

print(df.describe())
