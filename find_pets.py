
import os
from dotenv import load_dotenv
import petpy

load_dotenv()

API_KEY = os.environ.get("PETFINDER_API_KEY")
print("API KEY", API_KEY)

pf = Petfinder(API_KEY)
print(type(pf))

cats_list = pf.breed_list("cat")
print(type(cats_list))


#pf.pet_getRandom()
