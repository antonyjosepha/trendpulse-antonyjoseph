import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load our dataset for Remote Work & Mental Health Dataset
df = pd.read_csv("Impact_of_Remote_Work_on_Mental_Health.csv")

print("Dataset loaded.")

print(f"Shape: {df.shape}")

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)
