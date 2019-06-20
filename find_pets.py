
import os

from dotenv import load_dotenv
import petpy

import json
import pdb

load_dotenv()

API_KEY = os.environ.get("PETFINDER_API_KEY")
#CLIENT_SECRET = os.environ.get("PETFINDER_CLIENT_SECRET")
#HOST = "https://api.petfinder.com/v2/"

#print("--------------")
#print("CLIENT SECRET", CLIENT_SECRET)
#print("API KEY", API_KEY)
#print("HOST", HOST)
print("--------------")
#pf = petpy.Petfinder(API_KEY, secret=CLIENT_SECRET, host=HOST) #> TypeError: __init__() got an unexpected keyword argument 'host'
pf = petpy.Petfinder(API_KEY)
print(type(pf)) #> <class 'petpy.api.Petfinder'>
print(pf.host)
#print(dir(pf)) #>
print("--------------")

#cats_list = pf.breed_list("cat") #> json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#print(type(cats_list))

#pf.pet_getRandom() #> AttributeError: 'Petfinder' object has no attribute 'pet_getRandom'

#breakpoint() NOT AVAILABLE IN 3.6
#pdb.set_trace()

#cats_list = pf.breed_list("cat", return_df=True) #> json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
#print(type(cats_list))

try:

    pets_list = pf.pet_find(location="Seattle", animal="cat", sex="Female", count=100, return_df=True)
    print(type(cats_list))

except json.decoder.JSONDecodeError as e:
    print("OH, SOMETHING WENT WRONG...")
    print(e)
