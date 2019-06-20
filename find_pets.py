
import os
from dotenv import load_dotenv
import petpy

load_dotenv()

API_KEY = os.environ.get("PETFINDER_API_KEY")
print("API KEY", API_KEY)

pf = petpy.Petfinder(API_KEY)
print(type(pf)) #> <class 'petpy.api.Petfinder'>

cats_list = pf.breed_list("cat") #> json.decoder.JSONDecodeError: Expecting value: line 1 column 1 (char 0)
print(type(cats_list))


#pf.pet_getRandom()
