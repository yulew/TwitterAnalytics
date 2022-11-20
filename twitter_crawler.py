import tweepy
import json
from configs import api_key,api_key_secret,access_token,access_token_secret
from configs import max_tweet_ids


# Authenticate
auth = tweepy.OAuth1UserHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)


def get_user_info(screen_name):
    '''
    To be added:
    request other dic if so
    :param screen_name:
    :return:
    '''
    user = api.get_user(screen_name=screen_name)
    resp = {

        'user_id': user.id,
        'user_name': user.name,
        'user_screen_name': user.screen_name,
        'followers_count': user.followers_count,
        'friends_count': user.friends_count,
        'follower_ids': api.get_follower_ids(user_id = user.id),
        'friends_ids': api.get_friend_ids(user_id=user.id)
            }
    return resp



def get_tweets(key_string=None, language='en', number=500, max_id=2**64-1, result_type='recent', include_rtws=False):
    """

    :param key_string:
    :param language:
    :param number:
    :param result_type:
    :return:
    resps,
    Last tweet's id. Next round will be until here
    """
    resps = []

    if not include_rtws:
        tweets = tweepy.Cursor(api.search_tweets, q= key_string+ ' -filter:retweets', lang=language, tweet_mode="extended",
                               result_type=result_type,max_id=max_id).items(number)
    else:
        tweets = tweepy.Cursor(api.search_tweets, q=key_string, lang=language,
                               tweet_mode="extended",
                               result_type=result_type, max_id=max_id).items(number)

    tweets_json = []
    for tweet in tweets:
        tweets_json.append(tweet._json)

    for tweet in tweets_json:
        resp = {}
        resp['tweet_id'] = tweet['id']
        resp['time'] = tweet['created_at']
        resp['user_id'] = tweet['user']['id']
        resp['user_name'] = tweet['user']['name']
        resp['tweet_text'] = tweet['full_text']
        resp['tweet_entities'] = tweet["entities"]
        resp['followers_count'] = tweet['user']['followers_count']
        resp['friends_count'] = tweet['user']['friends_count']
        resp['is_quote_status'] = tweet['is_quote_status']
        resp['retweet_count'] = tweet['retweet_count']
        resp['favorite_count'] = tweet['favorite_count']
        resp['retweeted'] = tweet['retweeted']

        resps.append(resp)

    return resps, resps[-1]['tweet_id'] if resps else 0

def save_jsons(key_phrases,max_ids = max_tweet_ids):

    for i in range(50):
        for key_phrase in key_phrases:
            print(max_ids)
            print(key_phrase,max_ids.get(key_phrase,2**64-1))
            resps, max_id = get_tweets(key_string=key_phrase,max_id=max_ids.get(key_phrase,2**64-1))
            if max_id == 0:
                key_phrases.remove(key_phrase)
                del max_ids[key_phrase]
                continue
            max_ids[key_phrase] = max_id - 1
            with open("./data/jsons_dir/{}_{}.json".format(key_phrase, max_id),"w") as json_file:
                json.dump(resps, json_file)

    # Rewrite the configs.py file
    with open("configs.py", "w") as pyfile:
        str1 = "api_key = '{}'\n".format(api_key)
        str2 = "api_key_secret = '{}'\n".format(api_key_secret)
        str3 = "access_token = '{}'\n".format(access_token)
        str4 = "access_token_secret = '{}'\n".format(access_token_secret)

        str5 = "max_tweet_ids = {\n" + "".join(
            ["'" + key + "': " + str(max_ids[key] - 1) + ",\n" for key in max_ids]) + "}"

        pyfile.writelines([str1, str2, str3, str4, "\n", str5])


if __name__ == "__main__":
    save_jsons(key_phrases=["'are hiring' 'machine learning'", "'is hiring' 'machine learning'"])

