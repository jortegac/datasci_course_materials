import sys
import json
import unicodedata

#Process the sentiment input file and store them in memory as a dictionary
def process_sentiment(sent_file):
	sent_file_lines = sent_file.readlines()
	sentiments = {}
	for sentiment in sent_file_lines:
		#Sentiment and value are separated by tab
		words = sentiment.split("\t")
		sentiments[words[0]] = words[1]
	return sentiments
	
#Process the tweets input file and store them in memory
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
	
#Based on the sentiment dictionary and list of tweets, calculate the sentiment of every tweet and print them
def calculate_tweets_sentiment(sentiments, tweets):
	#Iterate through all the tweets
	for tweet in tweets:
		words = tweet.split()
		
		#The sentiment score
		score = float(0)
		
		#Number of words in the tweet
		num = len(words)
		
		#Iterate through every word in the tweet
		for word in words:			
			try:	
				#Find the word, get its score and add it to the current tweet score
				score += float(sentiments[word])
			except (NameError, TypeError, KeyError):
				#If the word is not in the dictionary, ignore the error and continue
				pass
		
		#No word in the tweet was found in the sentiment dictionary
		if num == 0:
			print "0"
		else:
			#Average the score by the number of words in the tweet
			print score/num
		
		

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
