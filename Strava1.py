import requests
from pandas import json_normalize
import json
import csv

# Get the tokens from file to connect to Strava
with open('strava_tokens.json') as json_file:
    strava_tokens = json.load(json_file)
# Loop through all activities
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']

# Loop through all activities
page = 1
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']

# Get page of activities from Strava
r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
r = r.json()

df = json_normalize(r)
df.to_csv('strava_activities_all_fields.csv')

