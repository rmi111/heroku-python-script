import requests
import tweepy
import json

def handler(pd: "pipedream"):
  # Reference data from previous steps
  # print(pd.steps["trigger"]["context"]["id"])
  api_key = "VzDNTdvSlz6H32aXY2dMpyYKQ"
  api_secrets = "0SoHyMziNFFDKTwrJAtOxUl9Lm19UIq51mYvu0kMuGBuSjM01c"
  access_token = "15154740-edk7ANzjdrAivuTOERkKQGEbIJlftIlWAm2ZBQB1m"
  access_secret = "lo6py7m319rOYTE1nrktolgGbhQXKP0pHElw3mX7bDcTb"
  
  # Authenticate to Twitter
  auth = tweepy.OAuthHandler(api_key,api_secrets)
  auth.set_access_token(access_token,access_secret)
  
  api = tweepy.API(auth)
  
  try:
      api.verify_credentials()
      print('Successful Authentication')
  except:
      print('Failed authentication')

  filtered_list = []
  my_screen_name = api.get_user(screen_name='DynamicBusiness')
  for users in pd.steps['retrieve_twitter_db']['$return_value']:
    print(users)
    Status = api.get_friendship(source_id = my_screen_name.id , source_screen_name = my_screen_name.screen_name, target_id = users['id'], target_screen_name = users['screen_name'])
    if int(users['followers_count']) > 500 and not Status [0].followed_by:
     filtered_list.append(users)
    else:
      print('{} he is not following You'.format(users['screen_name']))  
  # Return data for use in future steps
  # return {"foo": {"test":True}}
  return filtered_list

