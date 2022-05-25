

import pandas as pd
import requests
import json
import time



# Get the tokens from file to connect to Strava
with open('strava_tokens.json') as json_file:
    strava_tokens = json.load(json_file)
# If access_token has expired then use the refresh_token to get the new access_token
if strava_tokens['expires_at'] < time.time():
    # Make Strava auth API call with current refresh token
    response = requests.post(
        url='https://www.strava.com/oauth/token',
        data={
            'client_id': 46630,
            'client_secret': 'e61257e1ebc328fac5d6414b7c2789adade8dfc6',
            'grant_type': 'refresh_token',
            'refresh_token': strava_tokens['refresh_token']
        }
    )
    # Save response as json in new variable
    new_strava_tokens = response.json()
    # Save new tokens to file
    with open('strava_tokens.json', 'w') as outfile:
        json.dump(new_strava_tokens, outfile)
    # Use new Strava tokens from now
    strava_tokens = new_strava_tokens
# Loop through all activities
page = 1
url = "https://www.strava.com/api/v3/activities"
access_token = strava_tokens['access_token']
# Create the dataframe ready for the API call to store your activity data
activities = pd.DataFrame(
    columns=[
        "id",
        "name",
        "start_date_local",
        "type",
        "distance",
        "moving_time",
        "elapsed_time",
        "total_elevation_gain",
        "end_latlng",
        "external_id",
        "average_watts",
        "weighted_average_watts",
        "max_watts",
        "average_cadence",
        "suffer_score",
        "average_speed",
        "max_speed",
        "average_temp"
    ]
)
while True:

    # get page of activities from Strava
    r = requests.get(url + '?access_token=' + access_token + '&per_page=200' + '&page=' + str(page))
    r = r.json()
    print(range(len(r)))
    print(r)
    #print(activities)
    # if no results then exit loop
    if (not r):
        break

    # otherwise add new data to dataframe --- should this be null?
    for x in range(len(r)):
        activities.loc[x + (page - 1) * 200, 'id'] = r[x].get('id', 0)
        activities.loc[x + (page - 1) * 200, 'name'] = r[x].get('name', 0)
        activities.loc[x + (page - 1) * 200, 'start_date_local'] = r[x].get('start_date_local', 0)
        activities.loc[x + (page - 1) * 200, 'type'] = r[x].get('type', 0)
        activities.loc[x + (page - 1) * 200, 'distance'] = r[x].get('distance', 0)
        activities.loc[x + (page - 1) * 200, 'moving_time'] = r[x].get('moving_time', 0)
        activities.loc[x + (page - 1) * 200, 'elapsed_time'] = r[x].get('elapsed_time', 0)
        activities.loc[x + (page - 1) * 200, 'total_elevation_gain'] = r[x].get('total_elevation_gain', 0)
        activities.loc[x + (page - 1) * 200, 'end_latlng'] = r[x].get('end_latlng', 0)
        activities.loc[x + (page - 1) * 200, 'external_id'] = r[x].get('external_id', 0)
        activities.loc[x + (page - 1) * 200, 'average_watts'] = r[x].get('average_watts', 0)
        activities.loc[x + (page - 1) * 200, 'weighted_average_watts'] = r[x].get('weighted_average_watts', 0)
        activities.loc[x + (page - 1) * 200, 'max_watts'] = r[x].get('max_watts', 0)
        activities.loc[x + (page - 1) * 200, 'average_cadence'] = r[x].get('average_cadence', 0)
        activities.loc[x + (page - 1) * 200, 'suffer_score'] = r[x].get('suffer_score', 0)
        activities.loc[x + (page - 1) * 200, 'average_speed'] = r[x].get('average_speed', 0)
        activities.loc[x + (page - 1) * 200, 'max_speed'] = r[x].get('max_speed', 0)
        activities.loc[x + (page - 1) * 200, 'average_temp'] = r[x].get('average_temp', 0)

    # increment page
    page += 1
activities.to_csv('strava_activities.csv')

