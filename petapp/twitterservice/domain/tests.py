from .twitter import parse_tweets

from django.test import TestCase


class TweetParserTestCase(TestCase):
    def test_build_struct_parses(self):
        tweet = '{"screen_name":"monkey head", "tweets":[{"text":"here is #blah"}, {"text":"http://www.news.com is a #crappy site"}]}'
        actual = parse_tweets(tweet)
        self.assertEqual("monkey head", actual.screen_name())
        # self.assertEqual(['here', 'is', 'is', 'a', 'site'], actual.words())
