import tweepy
import os
import requests
import random

quote_key = os.environ["quote_key"]
api_key = os.environ["api_key"]
api_secret = os.environ["api_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]
bearer_token = os.environ["bearer_token"]

# Initialize API clients
unsplash_access_key = os.environ["unsplash_access_key"]
print(f"unsplash key: {unsplash_access_key}")

client = tweepy.Client(
    consumer_key=api_key,
    consumer_secret=api_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

auth = tweepy.OAuth1UserHandler(api_key, api_secret,access_token, access_token_secret)
api = tweepy.API(auth)

# Query Selector
my_list = ['aestheic','travel','greener-cities','people','wallpapers','health','arts-culture','beautiful','spirituality','current-events','abstract','wallart','painting','poetry','3d-renders','street-photography','textures-patterns','textures-patterns','fashion-beauty','qoutes','experimental','art','photography','gore','sweet','architecture-interior','lines','bad','good','horny','tumblr','random','pashtun_girl','kpk','pakistan']
random_item = random.choice(my_list)
print(random_item)


# Get random photo from Unsplash
unsplash_url = 'https://api.unsplash.com/photos/random?query='+ random_item
unsplash_headers = {'Authorization': f'Client-ID {unsplash_access_key}'}
response = requests.get(unsplash_url, headers=unsplash_headers)
response.raise_for_status()
unsplash_data = response.json()
unsplash_image_url = unsplash_data['urls']['regular']

# Download image from Unsplash
image_response = requests.get(unsplash_image_url)
with open('unsplash_image.jpg', 'wb') as f:
    f.write(image_response.content)
        
        
### Quote Generator

# Quote Query
quote_list = ['computers','alone','art','communications','god','history','learning','movies','love','life','knowledge','imagination']
category = random.choice(quote_list)
api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)

# Quoute Lenght should be less than 100
while(True):
  response = requests.get(api_url, headers={'X-Api-Key': quote_key})
  if response.status_code == requests.codes.ok:
    data = response.json()
    try:
        quote = data[0]['quote']
    except IndexError:
        print(data)
        print("Index out of range error occurred. Please check the data list.") 
    if len(quote) > 220:
        continue
    else:
        # Upload media file to twitter
        media = api.media_upload('unsplash_image.jpg')

        # Create tweet with media
        caption = f"[{random_item}]\n" + quote
        tweet = client.create_tweet(
        media_ids = [media.media_id],
        text=caption
        )
        break
  else:
    print("Error:", response.status_code, response.text)
