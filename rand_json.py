import random
import json

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
]

# Read values from a JSON file
def read_value_from_json():
  values = []
  with open('characters.json') as f:
    # Load all the data contained in my file. data = entries
    data = json.load(f) # ça va charger le fichier OPEN et transformer les donner lamba en json
    for entry in data:
        values.append(entry['character'])
    return values

def get_random_item(my_list):
  rand_numb = random.randint(0,len(my_list)-1)
  item = my_list[rand_numb] # get a quote from a list
  return item # return the item
    
def random_character():
  all_values = read_value_from_json()
  return get_random_item(all_values)

def capitalize(words):
  for word in words:
    word.capitalize()

def message(character, quote):
  capitalize(character)
  capitalize(quote)
  return "{} a dit : {}".format(character, quote)

user_answer = input("Tapez entrée pour conaitre une autre citation ou B pour quitter le programe.")

while user_answer != "B":
  print(message(random_character(), get_random_item(quotes)))
  user_answer = input("Tapez entrée pour conaitre une autre citation ou B pour quitter le programe.")