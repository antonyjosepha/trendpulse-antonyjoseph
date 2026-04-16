import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load our dataset from csv file
df = pd.read_csv("./data/trends_clean.csv")

# first 5 rows
print("First 5 rows:")
print(df.head())

# shape
print("\nShape of DataFrame:")
print(df.shape)

# average score and comments
print("\nAverages:")
print("Average score:", df['score'].mean())
print("Average num_comments:", df['num_comments'].mean())

# analysis
scores = df["score"].values

# mean, median, std dev
print("\nScore Statistics:")
print("Mean:", np.mean(scores))
print("Median:", np.median(scores))
print("Standard Deviation:", np.std(scores))

# highest and lowest score
print("\nScore Range:")
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))

# category with most stories
print("\ncategory with most stories:")
top_category = df['category'].value_counts().idxmax()
print(top_category)

# Highest and Lowest score
print("\nScore Range:")
print("Highest score:", np.max(scores))
print("Lowest score:", np.min(scores))

# Category with most stories
print("\nCategory with most stories:")
top_category = df['category'].value_counts().idxmax()
print(top_category)

# Story with most comments
print("\nMost commented story:")
max_comments_idx = df['num_comments'].idxmax()
print("Title:", df.loc[max_comments_idx, 'title'])
print("Comments:", df.loc[max_comments_idx, 'num_comments'])

# Story with most comments
print("\nLess commented story:")
min_comments_idx = df['num_comments'].idxmin()
print("Title:", df.loc[min_comments_idx, 'title'])
print("Comments:", df.loc[min_comments_idx, 'num_comments'])

# Engagement = num_comments / (score + 1)
df['engagement'] = df['num_comments'] / (df['score'] + 1)

# is_popular = score > average score
avg_score = df['score'].mean()
df['is_popular'] = df['score'] > avg_score

print("\nNew columns added: engagement, is_popular")

output_path = "./data/trends_analysed.csv"

df.to_csv(output_path, index=False)

print(f"Updated file saved to {output_path}")

print(f"Total rows: {len(df)}")
