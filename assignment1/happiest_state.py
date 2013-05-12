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
			# Only tweets in English
			if((data_point.get("lang") == "en") or (data_point.get("user").get("lang") == "en")):
				# Only tweets in the US
				if((data_point.get("place").get("country_code") == "US")):					
					tweets.append(data_point)
		except (AttributeError, TypeError):
			pass
	return tweets

def hw(sent_file, tweet_file):
	sentiments = process_sentiment(sent_file)
	tweets = process_tweets(tweet_file)
	
	# States and their sentiment score
	list_states = {}
	
	for tweet in tweets:
		# Get the state name
		state = tweet.get("place").get("full_name").split(", ")[1]
		
		# Make sure only state names represented with 2 letters go through
		if (len(state )== 2):
			# Calculate tweet sentiment and add it to the state score
			list_states[state] = list_states.get(state, 0.0) + calculate_score(sentiments, tweet.get("text"))	
	
	# Only happiest state
	print find_happiest(list_states)
	
def find_happiest(states):
     values = list(states.values())
     keys = list(states.keys())
     return keys[values.index(max(values))]

def calculate_score(sentiments, text):
		
	# Normalize text
	text = text.lower()
	
	# Split into words
	words = text.split()
	
	#The sentiment score
	sentiment_score = 0.0
	
	#Number of words in the tweet
	num = len(words)
	
	#Iterate through every word in the tweet
	for word in words:			
		try:	
			#Find the word, get its score and add it to the current tweet score
			sentiment_score += float(sentiments[word])
		except (NameError, TypeError, KeyError):
			#If the word is not in the dictionary, ignore the error and continue
			pass
	
	if num == 0:
		# Avoid division by zero
		sentiment_score = 0.0
	else:
		#Average the score by the number of words in the tweet
		sentiment_score = sentiment_score/num
	
	return sentiment_score
		

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw(sent_file, tweet_file)

if __name__ == '__main__':
    main()
