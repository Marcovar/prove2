#pass generator:
# 1)prendere input numerico da utente
# 2)genera una password casuale con lettere, numeri e caratteri
#     -la lunghezza sarà l'input numerico dall'utente

#guardate random.choiche()

import string
import random
lunghezza = input("Quanti caratteri vuoi nella tua password?")
def Password(lunghezza,lista_caratteri):
    lista_caratteri = random.choice(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","z","?","!","^","_","@","$","%"])

    numero_lettere = int(lunghezza) - len(lista_caratteri)
    for index in range(numero_lettere):
        lista_caratteri.append(random.choice(string.ascii_letters))
        random.shuffle(lista_caratteri)
        password = "".join(lista_caratteri)
return Password