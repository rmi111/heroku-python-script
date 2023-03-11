import requests
import time
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client
from supabase.lib.client_options import ClientOptions

def upsert(*data):
    error, response = (supabase.table('twitter_followers_records').upsert(data).execute())
    print(error)
    print(response)

def update_log_table(id, screen_name, last_cursor, status):
    data, count = supabase.table('twitter_followers_service_log').update({"screen_name": screen_name,"last_cursor": last_cursor, "status": status}).eq("id",id).execute()
    print(count)

# Techcrunch Fastcompany Wired Smartcompany Businessinsider Dynamicbusiness

access_token = os.environ.get("TWITTER_ACCESS_TOKEN")  

array = []
list = []
length = 5000
i = 0
cursor = -1

url = os.environ.get("SUPABASE_URL") 
key = os.environ.get("SUPABASE_KEY")
client_options = ClientOptions()
supabase = create_client(url , key, options=client_options)

# screen_names = ['Techcrunch','Fastcompany','Wired','Smartcompany','Businessinsider','Dynamicbusiness']
response = supabase.table('twitter_followers_service_log').select("*").eq('status','pending').execute()

for log_data in response.data:
    print(log_data)
    screenname = log_data['screen_name']
    cursor = log_data['last_cursor']
    array = []
    list = []
    i = 0
    last_cursor = cursor

    while cursor != 0:
        i = 0
        while i < 15:
            try:
                url = "https://api.twitter.com/1.1/followers/list.json?cursor="+str(cursor)+"&screen_name="+screenname+"&skip_status=true&include_user_entities=false&count=200"     
                payload = {}
                headers = { 'Authorization': 'Bearer '+access_token  }
                response = requests.request("GET", url, headers=headers, data=payload, timeout=60)
                response = response.json()

                if 'errors' in response:
                    print('waiting 1000 secs')
                    print(response)
                    time.sleep(1000)
                else:
                    user_data = response['users']
                    # print(len(user_data))
                    cursor = response ['next_cursor']
                    list = []
                    last_cursor = cursor

                    for data in user_data:
                        id = data['id']
                        screen_name = data['screen_name']
                        name = data['name']
                        location = data['location']
                        url = data['url']
                        description = data['description']
                        verified = data['verified']
                        followers_count = data['followers_count']
                        dict = {"twitter_id":id,"name":name,"screen_name":screen_name,"location":location,"url":url,"description":description,"verified":verified,"followers_count":followers_count,"screen_source":screenname}
                        list.append(dict)

                    print(len(list))
                    upsert(*list)
                    # update_log_table(screenname, last_cursor)
                    update_log_table(log_data['id'],log_data['screen_name'], cursor, 'pending')
                    # await (supabase.table('twitter_followers_db').upsert(list).execute())
                    # print(db_data)
                    i += 1
                    time.sleep(3)
            except BaseException as error:
                print('An exception occurred: {}'.format(error))
    cursor = -1
    update_log_table(log_data['id'],log_data['screen_name'], cursor, 'complete')