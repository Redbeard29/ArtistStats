import requests


API = 'https://api.spotify.com/v1/artists/13652'
response = requests.get(API)
data = response.json()

print(data)

#Need to register the app and provide a token for access