import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# json file 
file_path = "./data/trends_20260410.json"

# read json file
df = pd.read_json(file_path)

# output
print(f"Loaded {len(df)} stories from {file_path}")

# remove duplicates (based on post_id)
df = df.drop_duplicates(subset='post_id')

# output
print(f"After removing duplicates: {len(df)}")

# drop missing values
df = df.dropna(subset=['post_id', 'title', 'score'])

# output
print(f"After removing nulls: {len(df)}")

# fix data types
df['score'] = df['score'].astype(int)
df['num_comments'] = df['num_comments'].astype(int)

# remove low-quality rows (score < 5)
df = df[df['score'] >= 5]

# output
print(f"After removing low scores: {len(df)}")

# strip whitespace from title
df['title'] = df['title'].str.strip()

# save cleaned DataFrame to CSV
output_path = "./data/trends_clean.csv"

df.to_csv(output_path, index=False)

# output
print(f"Saved {len(df)} rows to {output_path}")

# output
print("\nStories per category:")

print(df['category'].value_counts())
