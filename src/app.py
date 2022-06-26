# desde la consola: pip install tweepy

# librerias
import os
from dotenv import load_dotenv
import tweepy
import requests

# cargo .env
load_dotenv()

# cargo datos de acceso desde archivo .env
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')
bearer_token = os.environ.get('BEARER_TOKEN')

# 
tweepy.Client()

