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



def get_tweets(key_string=None, language='en', number=500, max_id=2**64-1, result_type='recent'):
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

    tweets = tweepy.Cursor(api.search_tweets, q=key_string, lang=language, tweet_mode="extended",
                           result_type=result_type,max_id=max_id).items(number)

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

        resps.append(resp)

    return resps, resps[-1]['tweet_id']

def save_jsons(key_phrases,max_ids = max_tweet_ids):

    for i in range(50):
        for key_phrase in key_phrases:
            resps, max_id = get_tweets(key_string=key_phrase,max_id=max_ids.get(key_phrase,2**64-1))
            max_ids[key_phrase] = max_id - 1
            with open("./data/{}_{}.json".format(key_phrase, max_id),"w") as json_file:
                json.dump(resps, json_file)
    with open("configs.py", "w") as pyfile:
        pyfile.write(max_ids)


if __name__ == "__main__":
    save_jsons(key_phrases=["is hiring", "are hiring"])

