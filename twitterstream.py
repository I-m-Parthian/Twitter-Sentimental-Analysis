# Sol 1: get twitter data
import json
import twitter
import urllib.parse as encoder


class TwitterApi:
    def __init__(self):
        self.access_token_key=None
        self.access_token_secret = None
        self.consumer_key = None
        self.consumer_token_secret = None
        self.api = None
        self.results = None

    @staticmethod
    def get_settings():
        items = json.loads(open("Settings.json").read())
        return items

    def retrieve_credential(self):
        self.access_token_key = self.get_settings()["access_token_key"]
        self.access_token_secret = self.get_settings()["access_token_secret"]
        self.consumer_key = self.get_settings()["consumer_key"]
        self.consumer_secret = self.get_settings()["consumer_secret"]

    def twitter_request(self):
        self.api = twitter.Api(consumer_key=self.consumer_key, consumer_secret=self.consumer_secret,
                          access_token_key=self.access_token_key, access_token_secret=self.access_token_secret)

    def fetch_data(self,search):
        encoded_search = encoder.quote(search)
        self.results = self.api.GetSearch(raw_query="q="+encoded_search+"&result_type=recent&count=100")
        for line in self.results:
            print(line)


    def save(self):
        file = open("output.txt","w")
        for line in self.results:
            file.write(str(line)+"\n")
        file.close()
        print("Twitter Data saved to Output.txt")



if __name__ == '__main__':
  client = TwitterApi()
  client.get_settings()
  client.retrieve_credential()
  client.twitter_request()
  client.fetch_data("cricket")
  client.save()
