from json import dumps, loads
from os import environ

from django.http import JsonResponse
from django.shortcuts import render, redirect
from requests_oauthlib import OAuth1Session

CONSUMER_KEY = environ.get("CONSUMER_KEY")
CONSUMER_SECRET = environ.get("CONSUMER_SECRET")


def get_request_token(callback, error):
    oauth = OAuth1Session(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    response_json = oauth.fetch_request_token("https://api.twitter.com/oauth/request_token")
    if response_json and response_json["oauth_callback_confirmed"]:
        resource_owner_key = response_json.get('oauth_token')
        resource_owner_secret = response_json.get('oauth_token_secret')
        return callback(resource_owner_key, resource_owner_secret)
    else:
        return error("Failed")


def build_oauth_url(resource_owner_key, resource_owner_secret):
    oauth = OAuth1Session(client_key=CONSUMER_KEY,
                          client_secret=CONSUMER_SECRET,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          callback_uri="http://127.0.0.1:8000/authenticated/", )
    return oauth.authorization_url("https://api.twitter.com/oauth/authorize")


def index(request):
    if "token" in request.COOKIES:
        token = loads(request.COOKIES['token'])
        printFriends(token['oauth_token'], token['oauth_token_secret'])
        return render(request, "twitterservice/index.html")
    else:
        print("no token")
        return get_request_token(
            lambda key, secret: redirect(build_oauth_url(key, secret)),
            lambda message: render(request, "twitterservice/error.html", {"error": message}))


def friends(request, screen_name):
    return JsonResponse({'status': 'ok'})


def get_name(user_entry):
    return user_entry['name']


def printFriends(token, secret):
    oauth = OAuth1Session(CONSUMER_KEY,
                          client_secret=CONSUMER_SECRET,
                          resource_owner_key=token,
                          resource_owner_secret=secret)
    print(list(map(get_name, oauth.get("https://api.twitter.com/1.1/friends/list.json").json()['users'])))


def authenticated(request):
    oauth_token = request.GET['oauth_token']
    oauth_verifier = request.GET['oauth_verifier']
    oauth = OAuth1Session(client_key=CONSUMER_KEY,
                          client_secret=CONSUMER_SECRET,
                          resource_owner_key=oauth_token,
                          callback_uri="http://127.0.0.1:8000/")
    access_token = oauth.fetch_access_token(url="https://api.twitter.com/oauth/access_token", verifier=oauth_verifier)

    response = redirect("/twitter")
    response.set_cookie("token", dumps(access_token))
    return response
