from twitter_crawler import tweets2jsons
from jsons2csv import jsons2csv

key_phrase = input("Enter at lease one key phrase:")
if not key_phrase or key_phrase == 'q':
    key_phrase = input("Enter at lease one key phrase:")
else:
    key_phrases = ["'" + key_phrase + "'" ]
    while key_phrase and key_phrase != 'q':
        key_phrase = input("Enter more key phrase (enter 'q' if no more key phrases to put):")
        key_phrases.append("'" + key_phrase + "'" )


tweets2jsons(key_phrases=key_phrases)
jsons2csv()
