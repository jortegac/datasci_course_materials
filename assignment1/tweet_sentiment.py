import sys
import json
import unicodedata

def process_sentiment(sent_file):
	sent_file_lines = sent_file.readlines()
	sentiments = {}
	for sentiment in sent_file_lines:
		words = sentiment.split()
		sentiments[words[0]] = words[1]
	
def process_tweets(tweet_file):
	tweet_file_lines = tweet_file.readlines()
	tweets = []
	for tweet_data in tweet_file_lines:
		data_point = json.loads(tweet_data)
		try:
			tweet = data_point.get("text").encode('utf-8')
			tweets.append(tweet)
		except AttributeError:
			pass
	return tweets

def hw(sent_file, tweet_file):
	sentiments = process_sentiment(sent_file)
	tweets = process_tweets(tweet_file)	

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    lines(sent_file)
    lines(tweet_file)

if __name__ == '__main__':
    main()
