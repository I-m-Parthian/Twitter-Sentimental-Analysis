# Sol:3 Derive the sentiment of new terms

import sys
import json

class TermSentiment:
    def __init__(self,file_sentiment,file_tweet):
        self.file_sentiment = file_sentiment
        self.file_tweet = file_tweet
        self.word_scores = {}
        self.tweet_scores = {}
        self.tweet_text = []
        self.new_words = []

    def createdictionary(self):
        for line in self.file_sentiment:
            term, score = line.split("\t")
            self.word_scores[term] = int(score)

    def loadtweets(self):
        for line in self.file_tweet:
            tweet = json.loads(line)
            if 'text' in tweet:
                text = tweet['text'].lower()
                self.tweet_text.append(text)


    def sentimentscore(self):
        for t in self.tweet_text:
            sentiment = 0 # Initialize the tweet's sentiment to 0
            token = t.split() # Split the tweet into individual strings token

		    # For every word in the tweet
            for word in token:
                # If the word exists in AFINN-111, increase sentiment appropriately
                # Else, add it to the list of new words
                #print(word)
                if word in self.word_scores:
                    sentiment = sentiment + self.word_scores[word]
                else:
                    self.new_words.append(word)

            self.tweet_scores[t] = int(sentiment)

    def newsentimentscore(self):
        # For all new words
        for new in self.new_words:
            pos = neg = total = 0
            for t in self.tweet_scores:
                if new in t:
                    if self.tweet_scores[t] > 0:
                        pos+=1
                    elif self.tweet_scores[t] < 0:
                        neg+=1
                    total+=1
            print(new,' ', (pos - neg)//total)


if __name__ == '__main__':
    file_sentiment = open(sys.argv[1])
    file_tweet = open(sys.argv[2])
    term_sentiment = TermSentiment(file_sentiment,file_tweet)
    term_sentiment.createdictionary()
    term_sentiment.loadtweets()
    term_sentiment.sentimentscore()
    term_sentiment.newsentimentscore()