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
	
#Based on the sentiment dictionary and list of tweets, calculate the sentiment of unknown words
def calculate_score_unknown_words(sentiments, tweets):

	pos_words = {}
	all_unknowns = set()
	
	#Iterate through all the tweets
	for tweet in tweets:
		words = tweet.split()
		
		#The sentiment score
		score = float(0)
		
		#Number of words in the tweet
		num = len(words)
		
		#Unknown words in the tweet
		unknown = []
		
		positive = 0.0
		negative = 0.0
		
		#Iterate through every word in the tweet
		for word in words:		
			try:	
				#Find the word, get its score 
				score = float(sentiments[word])
				#If score is positive
				if score > float(0):
					positive += 1.0
				#If score is negative
				elif score < float(0):
					negative += 1.0
				
			except (NameError, TypeError, KeyError):
				#If the word is not in the sentiment dictionary
				unknown.append(word)
				all_unknowns.add(word)
				pass
				
		for word in unknown:
			if negative > 0.0:
				score = float(positive/negative)
			else:
				score = 0.0
				
			pos_words[word] = pos_words.get(word, 0.0) + score
				
	#Print the score of every unknown word in the tweet
	for word in all_unknowns:
		print word + " " + str(pos_words.get(word))

def hw(sent_file, tweet_file):
	sentiments = process_sentiment(sent_file)
	tweets = process_tweets(tweet_file)	
	calculate_score_unknown_words(sentiments, tweets)

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
