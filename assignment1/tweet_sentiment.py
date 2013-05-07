import sys
import json
import unicodedata

def process_sentiment(sent_file):
	sent_file_lines = sent_file.readlines()
	sentiments = {}
	for sentiment in sent_file_lines:
		words = sentiment.split("\t")
		sentiments[words[0]] = words[1]
	return sentiments
	
def process_tweets(tweet_file):
	tweet_file_lines = tweet_file.readlines()
	tweets = []
	for tweet_data in tweet_file_lines:
		data_point = json.loads(tweet_data)
		try:
			tweet = data_point.get("text").encode('ascii', 'ignore')
			tweets.append(tweet)
		except AttributeError:
			pass
	return tweets

def hw(sent_file, tweet_file):
	sentiments = process_sentiment(sent_file)
	tweets = process_tweets(tweet_file)	
	
	calculate_tweets_sentiment(sentiments, tweets)
	
def calculate_tweets_sentiment(sentiments, tweets):
	for tweet in tweets:
		words = tweet.split()
		score = float(0)
		num = float(0)
		for word in words:
			num = len(words)
			try:	
				score += float(sentiments[word])
			except (NameError, TypeError, KeyError):
				pass
		if num == 0:
			print "0"
		else:
			print score/num
		
		

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)
    #lines(sent_file)
    #lines(tweet_file)

if __name__ == '__main__':
    main()
