import os
import json
import time
import datetime
import requests

# collected data
all_data_list = []

# top story ids - url
top_story_ids_url = "https://hacker-news.firebaseio.com/v0/topstories.json"

# story - url
story_url = "https://hacker-news.firebaseio.com/v0/item"

# story url header
headers = {"User-Agent": "TrendPulse/1.0"}

# category
category_counter_dict = {"technology":0, "worldnews":0, "sports":0, "science":0, "entertainment":0}

# category keywords
categories = {
    "technology": ["ai", "software", "tech", "code", "computer", "data", "cloud", "api", "gpu", "llm"],
    "worldnews": ["war", "government", "country", "president", "election", "climate", "attack", "global"],
    "sports": ["nfl", "nba", "fifa", "sport", "game", "team", "player", "league", "championship"],
    "science": ["research", "study", "space", "physics", "biology", "discovery", "nasa", "genome"],
    "entertainment": ["movie", "film", "music", "netflix", "game", "book", "show", "award", "streaming"]
}


# write into a JSON file
file_path = os.path.join("data", "trends_20260410.json")

# create directory and its parents if they don't exist
os.makedirs(os.path.dirname(file_path), exist_ok=True)

def get_category(title):
    title_lower = title.lower()
    for category, keywords in categories.items():
        for keyword in keywords:
            if keyword in title_lower:
                return category
    return None

def write(data):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)  # indent=4 makes the file readable

def main():
    # to get the list of top story ids
    response = requests.get(top_story_ids_url)
    # to ensure the request was successful
    if response.status_code == 200:
        # parse JSON data into a Python dictionary
        data_list = response.json()
        # tmp category
        tmp_category = None
        # iterate the list of ids
        for top_story_id in data_list:
            try:
                # story url
                story_id_url = f"{story_url}/{top_story_id}.json"
                # to get the story for the given id
                response = requests.get(story_id_url, headers=headers)
                story_dict = response.json()
                # get data
                post_id = story_dict.get("id")
                title = story_dict.get("title")
                score = story_dict.get("score")
                num_comments = story_dict.get("descendants")
                author = story_dict.get("by")
                collected_at = str(datetime.datetime.now())
                # get category
                category = get_category(title)
                if category:
                    # get counter
                    total = category_counter_dict[category]
                    if total < 25:
                        category_counter_dict[category] = total + 1
                        all_data_list.append(dict(post_id=post_id, 
                                title=title, 
                                score=score, 
                                num_comments=num_comments, 
                                author=author, 
                                collected_at=collected_at, 
                                category=category))
                    # wait - on category changed
                    if tmp_category:
                        if tmp_category != category:
                            tmp_category = category
                            print("Waiting...")
                            time.sleep(2) # sleep for 2 secs
                    else:
                        tmp_category = category

            except Exception as e:
                print(f"Error: {e}")
    # write
    write(all_data_list)

    # summary
    summary_log = f"Collected {len(all_data_list)} stories. Saved to {file_path}"
    print(summary_log)

main()
