# liste avec les donner de base
print(" ")
characters = ["alvin et les Chipmunks", "Babar", "betty boop", "calimero", "casper", "le chat potté", "Kirikou"]
print("La liste avec tout les donner : ", characters)

# pour savoir l'emplacement d'un element:
print(" ")
print("Pour savoir l'emplacement d'un element: characters.index('Babar')")
characters.index("Babar")

# pour ajouter un element a la fin de la liste:
print(" ")
print("Pour ajouter un element a la fin de la liste: characters.append('Jérémy')")
characters.append("Jérémy")
print("Maintenant c'est comme ça : ", characters)

# pour ajouter un element a un emplacement specifique:
print(" ")
print("Pour ajouter un element a un emplacement specifique: characters.insert(3,'element_name')")
characters.insert(3,"element_name")
print("Maintenant c'est comme ça : ", characters)

# Pour eleminer le dernier element de la liste : 
print(" ")
print("Pour eleminer le dernier element de la liste : characters.pop()")
characters.pop()
print("Maintenant c'est comme ça : ", characters)

# Pour eleminer un element specifique: 
print(" ")
print("Pour eleminer un element specifique: characters.remove('element_name')")
characters.remove('element_name')
print("Maintenant c'est comme ça : ", characters)


