import os
import facebook

"""
Post to a Facebook group.

Before running script, the environment variables
APP_SECRET and ACCESS_TOKEN must be set.
"""

GROUP_ID = '613723709247918'  # id of the TB-test group
APP_SECRET = os.environ['APP_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

if __name__ == "__main__":
    graph = facebook.GraphAPI(access_token=ACCESS_TOKEN, app_secret=APP_SECRET)

    groups = graph.get_object(id=GROUP_ID)
    
    graph.put_object(GROUP_ID, "feed", message="from terminal")