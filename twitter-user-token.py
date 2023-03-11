# import requests
# import json
# import ast

# def get_access_token():
#     with open('config.json') as config_file:
#         data = json.load(config_file)

#         params = {
#             'grant_type': 'client_credentials',
#         }

#         response = requests.post('https://api.twitter.com/oauth/access_token', params=params, auth=(data['API_KEY'], data['API_KEY_SECRET']))

#         print(response.content)
#         json_data = ast.literal_eval(response.content.decode("UTF-8"))
#         return json_data['access_token']


# print(get_access_token())

import tweepy
 
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

my_screen_name = api.get_user(screen_name='DynamicBusiness')
for follower in my_screen_name.friends():
    Status = api.get_friendship(source_id = my_screen_name.id , source_screen_name = my_screen_name.screen_name, target_id = follower.id, target_screen_name = follower.screen_name)
    if Status [0].followed_by:
        print('{} he is following You'.format(follower.screen_name))
    else:
        print('{} he is not following You'.format(follower.screen_name))
        # api.destroy_friendship(screen_name = follower.screen_name)

# user = api.get_user('ChouinardJC')
# print(user.name)
# print(user.description)
# print(user.location)

# source_screen_name = "Twitter"
 
# # screen name of the account 2
# target_screen_name = "TwitterIndia"
 
# # getting the friendship details
# friendship = api.show_friendship(source_screen_name, target_screen_name)

# print(friendship)
# get_friendship(source_screen_name = source_screen_name, target_screen_name = target_screen_name)

# print(friendship.json())
# print("Is " + friendship[0].screen_name + " followed by " + friendship[1].screen_name, end = "? : ")
# if friendship[0].followed_by == False:
#     print("No")
# else:
#     print("Yes")
 
# print("Is " + friendship[0].screen_name + " following " + friendship[1].screen_name, end = "? : ")
# if friendship[0].following == False:
#     print("No")
# else:
#     print("Yes")
