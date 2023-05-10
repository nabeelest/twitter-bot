import tweepy
import os
import requests

api_key = os.environ["api_key"]
api_secret = os.environ["api_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]
bearer_token = os.environ["bearer_token"]

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

auth = tweepy.OAuth1UserHandler(api_key, api_secret,access_token, access_token_secret)
api = tweepy.API(auth)

# Initialize API clients
unsplash_access_key = os.environ["unsplash_access_key"]

# Get random photo from Unsplash
unsplash_url = 'https://api.unsplash.com/photos/random?query=aesthetic'
unsplash_headers = {'Authorization': f'Client-ID {unsplash_access_key}'}
response = requests.get(unsplash_url, headers=unsplash_headers)
response.raise_for_status()
unsplash_data = response.json()
unsplash_image_url = unsplash_data['urls']['regular']

# Download image from Unsplash
image_response = requests.get(unsplash_image_url)
with open('unsplash_image.jpg', 'wb') as f:
    f.write(image_response.content)

# Upload media file
media = api.media_upload('unsplash_image.jpg')

# Create tweet with media
tweet = client.create_tweet(
    media_ids = [media.media_id]
)


os.remove('unsplash_image.jpg')
