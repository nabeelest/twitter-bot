import tweepy
import os
import requests

client_id = "VGN5WnRmUjZaREVwU3QzVUZ2VWU6MTpjaQ"
client_secret = "MNq0Qa8pe6WfmMGQaU_XqAfRz6Ew9nMrsFWfeLqWl60cIMixnl"
api_key = "Kbac48DDrpOyD02en72ELZL7z"
api_secret = "Tnu10IIzpGPSJ7PKUmY43sRBzbC9e1D3j0QMh4fZen0SqYv3im"
access_token = "1624851913345994753-96411rQhCbtICx3U0GFrsPaV2Da7BY"
access_token_secret = "aE2pW1TEJIjRXU2marMx1f2kn8PAFRmLqCz6qxvh89zoi"
bearer_token = r"AAAAAAAAAAAAAAAAAAAAAD1fnAEAAAAAe3GNoV5R9IxdAvVz%2Fszjtetu5bU%3DWAPm72xaY8r5Cac6IWGECrVhMCPkeYMQ7AqDS0IozHkQtdQCSz"

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

auth = tweepy.OAuth1UserHandler(api_key, api_secret,access_token, access_token_secret)
api = tweepy.API(auth)

# Initialize API clients
unsplash_access_key = 'Hato407HTCfPeG9y5MRBaNenaDqckkbC_vRUCLTYwBk'

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