import random
import json

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

characters = [
    "alvin et les Chipmunks", 
    "Babar", 
    "betty boop", 
    "calimero", 
    "casper", 
    "le chat potté", 
    "Kirikou"
]
# Read values from a JSON file
def read_value_from_json():
  values = []
  with open ('characters.json') as f:
    # Load all the data contained in my file. data = entries
    for entry in data:
        values.append(entry['character'])
    return values
  # add each item in my list
  # return my completed list

def get_random_quote(my_list):
  rand_numb = random.randint(0,len(my_list)-1)
  item = my_list[rand_numb] # get a quote from a list
  return item # return the item
    
def capitalize(words):
  for word in words:
    word.capitalize()

def message(character, quote):
  capitalize(character)
  capitalize(quote)
  return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour conaitre une autre citation ou B pour quitter le programe.")

while user_answer != "B":
  print(message(get_random_quote(characters), get_random_quote(quotes)))
  user_answer = input("Tapez entrée pour conaitre une autre citation ou B pour quitter le programe.")
