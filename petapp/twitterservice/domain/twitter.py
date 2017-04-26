import json


def parse_tweets(tweet):
    return Tweet(tweet)


class Tweet:
    def __init__(self, tweet):
        as_dict = json.loads(tweet)
        self._screen_name = as_dict['screen_name']
        self._words = self.parse_words(as_dict['tweets'])

    def __repr__(self):
        return "Tweet: " + self._screen_name

    def screen_name(self):
        return self._screen_name

    def words(self):
        return self._words

    def parse_words(self, tweets_dict):
        pass
