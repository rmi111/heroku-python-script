import requests
import time
import os
import asyncio
import json
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client
from supabase.lib.client_options import ClientOptions

def upsert(*data):
    error, response = (supabase.table('twitter_followers_db').upsert(data).execute())
    print(error)
    print(response)

def is_following(source_user: str, target_user: str)-> bool:
        try:
            url = "https://api.twitter.com/1.1/friendships/show.json?source_screen_name=" + source_user + "&target_screen_name=" + target_user
            payload = {}
            headers = { 'Authorization': 'Bearer ' + access_token  }
            response = requests.request("GET", url, headers=headers, data=payload, timeout=60)
            response = response.json()

            if 'errors' in response:
                print('waiting 1000 secs')
                print(response)
                time.sleep(1000)
            else:
                relationship = response['relationship']

                following = relationship['source']['following']
                followed_by = relationship['source']['followed_by']
                    
                return following
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
        return False

def follow(source_user: str):
        print(type(source_user))
        try:
            url = "https://api.twitter.com/1.1/friendships/create.json?user_id=" + str(source_user) + "&follow=true"
            payload = {}
            headers = { 'Authorization': 'Bearer '+access_token  }
            response = requests.request("POST", url, headers=headers, data=payload, timeout=60)
            response = response.json()

            if 'errors' in response:
                print('waiting 1000 secs')
                print(response)
                time.sleep(1000)
            else:
                # relationship = response['relationship']
                # following = relationship['source']['following']
                # followed_by = relationship['source']['followed_by']
                print("Response:" + response)
                # return following
        except BaseException as error:
            print('An exception occurred: {}'.format(error))
        return False
    
    
# Techcrunch Fastcompany Wired Smartcompany Businessinsider Dynamicbusiness
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")  

array = []
list = []
length = 5000
i = 0
cursor = -1

url = os.environ.get("SUPABASE_URL") 
key = os.environ.get("SUPABASE_KEY")

client_options = ClientOptions(timeout=1000)
supabase = create_client(url , key, options=client_options)

lenth = -1
minRange = 0
maxRange = 5

while lenth != 0:
    data = supabase.table('twitter_followers_db').select('*').range(minRange,maxRange).execute()
    # minRange = maxRange + 1
    # maxRange = maxRange + 1000
    # print(data.data)
    # lenth = len(dictionary)

    for tweeter_info in data.data:
        follower_count = tweeter_info['followers_count']
        id = tweeter_info['id']
        print(follower_count)
        screen_name = tweeter_info['screen_name']
        is_following_dynamic_business = is_following(screen_name,'Dynamicbusiness')
        print(is_following_dynamic_business)
        if int(follower_count) > 100 and is_following_dynamic_business == False:
            follow(id)

        time.sleep(10)
