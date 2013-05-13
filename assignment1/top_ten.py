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
			# Only tweets with tags
			if(data_point.get("entities").get("hashtags")):
				tweets.append(data_point)
		except (AttributeError, TypeError):
			pass
	return tweets

def hw(tweet_file):
	tweets = process_tweets(tweet_file)
	
	# Hashtags and their number of ocurrences
	hashtags = {}
	
	for tweet in tweets:
		# Get the hashtags
		tags = tweet.get("entities").get("hashtags")
		
		for tag in tags:
			text = tag.get("text").encode('ascii', 'ignore')
			
			# Get rid of empty tags
			if (text != ""):
				hashtags[text] = hashtags.get(text, 0.0) + 1.0
	
	# Only top ten
	top_ten = get_top_ten(hashtags)
	
	# Print top ten tags
	for item in top_ten:
		print item + " " + str(hashtags.get(item))
	
def get_top_ten(hashtags):
	 return sorted(hashtags, key=hashtags.get, reverse = True)[0:10]

def lines(fp):
    print str(len(fp.readlines()))

def main():
    tweet_file = open(sys.argv[1])
    hw(tweet_file)

if __name__ == '__main__':
    main()
