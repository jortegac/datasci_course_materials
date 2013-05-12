import sys
import json
import unicodedata

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

def hw(tweet_file):
	tweets = process_tweets(tweet_file)	
	
	# Number of occurrences of the term in all tweets
	terms = {}	
	
	# Number of occurrences of all terms in all tweets
	all_terms = 0.0
	
	for tweet in tweets:
		words = tweet.split()		
		for word in words:
			terms[word] = terms.get(word, 0.) + 1.0			
			all_terms = all_terms + 1.0
	
	for term in terms:
		print term + " " + str(float(terms.get(term)/all_terms))
	
def main():
	tweet_file = open(sys.argv[1])
	hw(tweet_file)	

if __name__ == '__main__':
    main()
