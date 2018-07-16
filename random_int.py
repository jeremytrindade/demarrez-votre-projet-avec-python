import random

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

def get_random_quote(my_list):
  # TODO: get a random number
  item = my_list[0]
  return item
    
def capitalize(words):
  for word in words:
    word.capitalize()

def message(character, quote):
  capitalize(character)
  capitalize(quote)
  return "{} a dit : {}".format(character, quote))

user_answer = input("Tapez entrée pour conaitre une autre citation ou B pour quitter le programe.")

while user_answer != "B":
  print(message(get_random_item(characters), get_random_item(quotes)))
  user_answer = input("Tapez entrée pour conaitre une autre citation ou B pour quitter le programe.")
