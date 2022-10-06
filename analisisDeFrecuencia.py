
######################################################## ANÁLISIS DE FRECUENCIA ########################################################

from collections import Counter

alfabetoMayus="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
alfabetoMinus="abcdefghijklmnñopqrstuvwxyz"

#Frecuencia de aparición de letras
frecuencia="EAOLSNDRUITCPMYQBHGFVJÑZXKW"

#Lista con las letras ordenadas de mayor a menor frecuencia que aparecen en el texto cifrado
listaCaracteresOrdenada=""

print("Escribe el mensaje que quieres descrifrar:")
mensaje=input()
mensajeTodoMayus=mensaje.maketrans(alfabetoMinus, alfabetoMayus)
mensajeTodoMayus=mensaje.translate(mensajeTodoMayus)
#Para contar la letras del mensaje cifrado
counter=Counter(mensajeTodoMayus)

listaLetras= {}

for caracter in alfabetoMayus:
    listaLetras[caracter]=counter[caracter]

#Ordena la listaLetras de mayor a menos frecuencia
listaOrdenada = sorted(listaLetras.items(), key=lambda x: x[1], reverse=True)
print("")
print(listaOrdenada)

#Letras de mayor frecuencia a menor frecuencia juntas en un mismo string
for i in range(len(listaOrdenada)):
    listaCaracteresOrdenada= listaCaracteresOrdenada + listaOrdenada[i][0]

#Intercambiamos letras en el mensaje cifrado
mensajeDescifrado = mensajeTodoMayus.maketrans(listaCaracteresOrdenada, frecuencia)

print("\n############### MENSAJE CIFRADO ###############")
print(mensajeTodoMayus)

print("\n############### CARACTERES ORDENADOS DE MAYOR FRECUENCIA A MENOS ###############")
print(listaCaracteresOrdenada)

print("\n############### FRECUENCIAS ###############")
print(frecuencia)

print("\n############### MENSAJE DESCIFRADO ###############")
mensajeDescifrado=mensajeTodoMayus.translate(mensajeDescifrado)
print(mensajeDescifrado)

print("\nQuieres ajustar el mensaje? (yes/no)")
ajustarMensaje=input()
if ajustarMensaje=="yes":
    terminar="yes"
    while terminar=="yes":
        print("\n############### AJUSTAR MENSAJE ###############")
        #|A|B|C|D|E|F|G|H|I|J|K|L|M|N|Ñ|O|P|Q|R|S|T|U|V|W|X|Y|Z|
        #|D|K|I|P|A|X|J|T|O|N|R|Z|H|S|Ñ|F|M|B|C|Q|L|G|Y|W|E|V|U|
        #DKIPAXJTONRZHSÑFMBCQLGYWEVU

        listaLetrasAjustadas=input()
        mensajeDescifrado = mensajeTodoMayus.maketrans(alfabetoMayus,listaLetrasAjustadas)
        mensajeDescifrado=mensajeTodoMayus.translate(mensajeDescifrado)
        print("\n############### MENSAJE DESCIFRADO ###############")
        print(mensajeDescifrado)
        print("\nQuieres seguir ajustando el mensaje? (yes/no)")
        terminar=input()





