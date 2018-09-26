# Sol 2 : Derive the sentiment of each tweet


import json
import sys
import re

class TweetSentiment:
    def __init__(self):
        self.sentiment_dict = None

    def get_sentiment_dict(self,sentiment_file_path):
        sentiment_file = open(sentiment_file_path,'r')
        sentiment_dict = dict()
        for line in sentiment_file.readlines():
            line_sp =  line[:-1].split("\t")
            try:
                sentiment_dict[line_sp[0]] = int(line_sp[1])
            except ValueError:
                sentiment_dict[line_sp[0]] = 0
        self.sentiment_dict = sentiment_dict


    @staticmethod
    def parse_tweet_text(line):
        tweet = json.loads(line[:-1], encoding='utf-8')
        try:
            tweet_text = tweet['text']
        except KeyError:
            tweet_text = ""
        text_parsed = re.sub('[^A-Za-z0-9 ]+', '', tweet_text).lower().split(" ")
        return text_parsed

    def get_sentiment_score(self,text_parsed):
        tot_sentiment = 0.0
        for word in text_parsed:
            try:
                tot_sentiment += self.sentiment_dict[word]
            except KeyError:
                tot_sentiment += 0.0
        return tot_sentiment

    def calculate_score(self):
        sentiment_file_path = (sys.argv[1])
        tweet_file_path     = (sys.argv[2])

        data = open(tweet_file_path,'r')
        self.get_sentiment_dict(sentiment_file_path)


        for line in data.readlines():
            text_parsed = self.parse_tweet_text(line)
            print(self.get_sentiment_score(text_parsed))


if __name__ == '__main__':
    tweet_sentiment = TweetSentiment()
    tweet_sentiment.calculate_score()
