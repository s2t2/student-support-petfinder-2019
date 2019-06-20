from pprint import pprint
import os
from dotenv import load_dotenv
import requests

load_dotenv()

TOKEN = os.environ.get("PETFINDER_ACCESS_TOKEN")
#print(TOKEN)

request_url = "https://api.petfinder.com/v2/animals"

headers = {"Authorization": f"Bearer {TOKEN}"}

response = requests.get(request_url, headers=headers)
print(type(response))
print(response.status_code)
pprint(response.text)
