## Twitter Analytics Program
### Python and Packages
This program is tested under ```Python 3.9```.\
To install required Python packages, type the following command
```commandline
pip install -r requirement.txt
```

### About This Program
This program contains several parts as follows:

1. Tweets Crawler:
   With using the TwitterAPI -- Tweepy, this program helps crawl Twitter data with any keywords you intend to match with the tweets within seven days.
   By run the program,
   Firstly, replace`<Your API KEY>， <Your API KEY SECRET>, <Your ACCESS TOKEN> and <Your ACCESS TOKEN SECRET>`in `configs.py` with your API KEY, API KEY SECRET, ACCESS TOKEN and ACCESS TOKEN SECRET that you requested with your developer account.

```
   api_key = <Your API KEY>
   api_key_secret = <Your API KEY SECRET>
   access_token = <Your ACCESS TOKEN>
   access_token_secret =  <Your ACCESS TOKEN SECRET>
```

Then you can run `main.py` that will ask you to enter the key-phrases you want to match with the tweets:
```
    python main.py
```

2. Analyze the tweets from NLP tools, such as sPacy.
