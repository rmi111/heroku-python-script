import requests
import time
import os
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client

# Techcrunch Fastcompany Wired Smartcompany Businessinsider Dynamicbusiness

access_token =  "AAAAAAAAAAAAAAAAAAAAABQhXQEAAAAADS0YTzYvY2lfyjd0hj3PSH6tQtY%3DSrDI54qZm7iH3jPpLHHjxft9uEFxWHiQaHNB8OgGo8XTrsIHKf"
# screenname = "@aiyanaish"
# url = "https://api.twitter.com/1.1/followers/list.json?screen_name="+screenname+"&skip_status=true&include_user_entities=false&count=200"
# payload={}
# headers = { 'Authorization': 'Bearer ' + access_token  }
# response = requests.request("GET", url, headers=headers, data=payload)
# response = response.json()

array = []
list = []
length = 5000
i = 0
cursor = -1

url = os.environ.get("SUPABASE_URL") 
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url , key)

screen_names = ['Techcrunch','Fastcompany','Wired','Smartcompany','Businessinsider','Dynamicbusiness']

for screenname in screen_names:
    while cursor != 0:
        while i < 15:
            url = "https://api.twitter.com/1.1/followers/list.json?cursor="+str(cursor)+"&screen_name="+screenname+"&skip_status=true&include_user_entities=false&count=200"     
            payload = {}
            headers = { 'Authorization': 'Bearer '+access_token  }
            response = requests.request("GET", url, headers=headers, data=payload)
            response = response.json()

            if 'errors' in response:
                time.sleep(1000)
            else:
                user_data = response['users']
                cursor = response ['next_cursor']
                list = []

                for data in user_data:
                    id = data['id']
                    screen_name = data['screen_name']
                    name = data['name']
                    location = data['location']
                    url = data['url']
                    description = data['description']
                    verified = data['verified']
                    followers_count = data['followers_count']
                    dict = {"id":id,"name":name,"screen_name":screen_name,"location":location,"url":url,"description":description,"verified":verified,"followers_count":followers_count,"screen_source":screenname}
                    list.append(dict)
                
                db_data = supabase.table('twitter_followers_db').upsert(list).execute()
                print(db_data)
                i += 1
