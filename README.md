## Twitter Analytics Program
### Python and Packages
```Python 3.9```
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
Secondly, enter the key-phrases you would like to match with the tweets in save_jsons of tweeter_crawler.py, and then run
```
   python tweeter_crawler.py
```
You will get your json files in ./jsons_dir. You can run jsons2csv to transform them to a single csv file, by
```commandline
   python jsons2csv.py
```

2. Analyze the tweets from NLP tools, such as sPacy.
