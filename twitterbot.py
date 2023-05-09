import tweepy
import os
import requests

secrets = os.environ["client_secret]

client = tweepy.Client(
    consumer_key=secrets.API_KEY,
    consumer_secret=secrets.API_SECRET,
    access_token=secrets.ACCESS_TOKEN,
    access_token_secret=secrets.ACCESS_TOKEN_SECRET
)

auth = tweepy.OAuth1UserHandler(secrets.API_KEY, secrets.API_SECRET,secrets.ACCESS_TOKEN, secrets.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Initialize API clients
unsplash_access_key = secrets.UNSPLASH_ACCESS_KEY

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
