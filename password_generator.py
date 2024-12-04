#pass generator:
# 1)prendere input numerico da utente
# 2)genera una password casuale con lettere, numeri e caratteri
#     -la lunghezza sarà l'input numerico dall'utente

#guardate random.choiche()

import random
lunghezza = int(input("Quanti caratteri vuoi nella tua password? "))
def Password(lunghezza):
    lista_caratteri = []
    lista_caratteri.append(random.choice("qwertyuiopasdfghjklzxcvbnm0123456789?!^_@$%"))
    
    while len(lista_caratteri) < lunghezza:
        lista_caratteri.append(random.choice("qwertyuiopasdfghjklzxcvbnm0123456789?!^_@$%"))
        
    random.shuffle(lista_caratteri)

    password = "".join(lista_caratteri)
    return password
password_generata = Password(lunghezza)
print(f"La tua password generata è: {password_generata}")
