dico_en_fr = {"three": "trois", "one": "un", "two": "deux"}
print(dico_en_fr)
print("Pour montrer le type on fai: type(dico_en_fr")
print(type(dico_en_fr))
print("Pour voir quelle est la traduction d'un certain mots en anglais on fait: dico_en_fr['one']")
print(dico_en_fr["one"])
print("Maintenan vue que j'ai oublier de metre la premiere letre dans les resulta, je peux le modifier comme ça: ")
print("dico_en_fr.update({'one': 'Un', 'two': 'Deux'})")
dico_en_fr.update({"one": "Un", "two": "Deux"})
print("Maintenan pour suprimer un mots specifique:")
print(dico_en_fr)
print("Je fait: dico_en_fr.pop('three')")
dico_en_fr.pop("three")
print("Et le resulta est:")
print(dico_en_fr)