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
    

user_answer = input("Tapez entrée pour conaitre une autre citation ou B pour quitter le programe.")

while user_answer != "B":
  print(get_random_quote(quotes))
  user_answer = input("Tapez entrée pour conaitre une autre citation ou B pour quitter le programe.")

for character in characters:
  n_character = character.capitalize()
  # .capitalize() ser metre la premiere letre en majuscule
  print(n_character)


print(get_random_quote(quotes))