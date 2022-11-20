import os
import json
import datetime

import pandas as pd

DIR = "/Users/Yule/Documents/ML_Projects/TwitterAnalytics/data/jsons_dir/"

def jsons_combination(DIR):
    tweets_json = []

    for file in os.listdir(DIR):
        if file == '.DS_Store':continue
        with open(DIR + file, 'r') as f:
            tweets_json.extend(json.load(f))
    return tweets_json


def json2csv(tweets_json, csv_path=DIR[:-10]+"csv_dir/"+str(datetime.datetime.now())):
    columns = ['tweet_id', 'time', 'user_id', 'user_name', 'tweet_text', 'tweet_entities',
               'followers_count', 'friends_count', 'is_quote_status', 'retweet_count', 'favorite_count']
    data = []
    for tweet in tweets_json:
        data.append([tweet[key] for key in tweet])

    df = pd.DataFrame(data, columns=columns)
    df.to_csv(csv_path)
    return df

def jsons2csv(input_jsons_dir=DIR, csv_output_dir=DIR[:-10]+"csv_dir/"+str(datetime.datetime.now()) + '.csv'):
    tweets_json = jsons_combination(input_jsons_dir)
    json2csv(tweets_json, csv_output_dir)

if __name__ == "__main__":
    jsons2csv()