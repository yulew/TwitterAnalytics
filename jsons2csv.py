import os
import json
import datetime

import pandas as pd

DIR = "/Users/Yule/Documents/ML_Projects/TwitterAnalytics/data/jsons_dir/"


def jsons_combination(DIR):
    tweets_json = []
    keyphrases = []
    for file in os.listdir(DIR):
        if file == '.DS_Store': continue
        with open(DIR + file, 'r') as f:
            tweets_json.extend(json.load(f))
        keyphrases.append(file.split('_')[0])
    return tweets_json, keyphrases


def json2csv(tweets_json, csv_path=DIR[:-10] + "csv_dir/" + str(datetime.datetime.now())):
    columns = ['tweet_id', 'time', 'user_id', 'user_name', 'tweet_text', 'tweet_entities',
               'followers_count', 'friends_count', 'is_quote_status', 'retweet_count', 'favorite_count','retweeted']
    data = []
    for tweet in tweets_json:
        data.append([tweet[key] for key in tweet])

    df = pd.DataFrame(data, columns=columns)
    df.to_csv(csv_path)
    return df


def jsons2csv(input_jsons_dir=DIR, csv_output_dir=DIR[:-10] + "csv_dir/" ):
    tweets_json, keyphrases = jsons_combination(input_jsons_dir)

    if not os.path.exists(csv_output_dir):
        os.mkdir(csv_output_dir)
    file_path = csv_output_dir + '_'.join(keyphrases) + str(datetime.datetime.now()) + '.csv'
    json2csv(tweets_json, file_path)
    print("The tweeter data csv file has been generated in '{}'".format(file_path))
    remove_jsons(input_jsons_dir)
    return file_path


def remove_jsons(input_jsons_dir):
    '''
    Remove json files after they are combined with csv.
    '''
    for file in os.listdir(input_jsons_dir):
        os.remove(os.path.join(input_jsons_dir, file))


if __name__ == "__main__":
    jsons2csv()
