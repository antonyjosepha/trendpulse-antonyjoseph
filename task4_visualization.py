import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# set visualization styles
sns.set(style="whitegrid")

# load our dataset from csv file
df = pd.read_csv("./data/trends_analysed.csv")

# create outputs folder
os.makedirs("outputs", exist_ok=True)

# to shorten titles
def shorten_title(title, max_len=50):
    return title if len(title) <= max_len else title[:47] + "..."

# chart 1: Top 10 Stories by Score
top10 = df.sort_values(by="score", ascending=False).head(10)
titles = top10['title'].apply(shorten_title)
scores = top10['score']
plt.figure()
plt.barh(titles, scores)
plt.xlabel("Score")
plt.ylabel("Story Title")
plt.title("Top 10 Stories by Score")
plt.gca().invert_yaxis()
plt.savefig("outputs/chart1_top_stories.png")
plt.close()

# chart 2: Stories per Category
category_counts = df['category'].value_counts()
plt.figure()
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category")
plt.ylabel("Number of Stories")
plt.title("Stories per Category")
plt.savefig("outputs/chart2_categories.png")
plt.close()

# chart 3: Score vs Comments
popular = df[df['is_popular'] == True]
not_popular = df[df['is_popular'] == False]
plt.figure()
plt.scatter(popular['score'], popular['num_comments'], label="Popular")
plt.scatter(not_popular['score'], not_popular['num_comments'], label="Not Popular")
plt.xlabel("Score")
plt.ylabel("Number of Comments")
plt.title("Score vs Comments")
plt.legend()
plt.savefig("outputs/chart3_scatter.png")
plt.close()

# dashboard
plt.figure(figsize=(20, 12))
plt.subplot(1,3,1)
plt.barh(titles, scores)
plt.xlabel("Score", fontsize=12)
plt.ylabel("Story Title", fontsize=12)
plt.title("Top 10 Stories by Score", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.gca().invert_yaxis()

plt.subplot(1,3,2)
plt.bar(category_counts.index, category_counts.values)
plt.xlabel("Category", fontsize=12)
plt.ylabel("Number of Stories", fontsize=12)
plt.title("Stories per Category", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

plt.subplot(1,3,3)
plt.scatter(popular['score'], popular['num_comments'], label="Popular")
plt.scatter(not_popular['score'], not_popular['num_comments'], label="Not Popular")
plt.xlabel("Score", fontsize=12)
plt.ylabel("Number of Comments", fontsize=12)
plt.title("Score vs Comments", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend()
plt.tight_layout()
plt.savefig("outputs/dashboard.png")
plt.close()
