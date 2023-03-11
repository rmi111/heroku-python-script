import requests
import time
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()
from supabase import create_client
from supabase.lib.client_options import ClientOptions


def init_log_table():
    screen_names = ['Techcrunch','Fastcompany','Wired','Smartcompany','Businessinsider','Dynamicbusiness']
    for screenname in screen_names:
        data, count = supabase.table('twitter_followers_service_log').insert({"screen_name": screenname,"last_cursor": -1, "status": "pending"}).execute()
        print(count)    

# Techcrunch Fastcompany Wired Smartcompany Businessinsider Dynamicbusiness

access_token = os.environ.get("TWITTER_ACCESS_TOKEN")  

url = os.environ.get("SUPABASE_URL") 
key = os.environ.get("SUPABASE_KEY")
client_options = ClientOptions()
supabase = create_client(url , key, options=client_options)

init_log_table()