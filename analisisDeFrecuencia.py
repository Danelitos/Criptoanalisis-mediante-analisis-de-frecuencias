
######################################################## ANÁLISIS DE FRECUENCIA ########################################################

from collections import Counter

alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

#Frecuencia de aparición de letras
frecuencia="EAOLSNDRUITCPMYQBHGFVJÑZXKW"

#Lista con las letras ordenadas de mayor a menor frecuencia que aparecen en el texto cifrado
listaCaracteresOrdenada=""

print("Escribe el mensaje que quieres descrifrar:")
mensaje=input()

#Para contar la letras del mensaje cifrado
counter=Counter(mensaje)

listaLetras= {}

for caracter in alfabeto:
    listaLetras[caracter]=counter[caracter]

#Ordena la listaLetras de mayor a menos frecuencia
listaOrdenada = sorted(listaLetras.items(), key=lambda x: x[1], reverse=True)
print("\n"listaOrdenada)

#Letras de mayor frecuencia a menor frecuencia juntas en un mismo string
for i in range(len(listaOrdenada)):
    listaCaracteresOrdenada= listaCaracteresOrdenada + listaOrdenada[i][0]

#Intercambiamos letras en el mensaje cifrado
mensajeDescifrado = mensaje.maketrans(listaCaracteresOrdenada, frecuencia)

print("\n############### MENSAJE CIFRADO ###############")
print(mensaje)

print("\n############### CARACTERES ORDENADOS DE MAYOR FRECUENCIA A MENOS ###############")
print(listaCaracteresOrdenada)

print("\n############### FRECUENCIAS ###############")
print(frecuencia)

print("\n############### MENSAJE DESCIFRADO ###############")
mensajeDescifrado=mensaje.translate(mensajeDescifrado)
print(mensajeDescifrado)

print("\nQuieres ajustar el mensaje? (yes/no)")
ajustarMensaje=input()
if ajustarMensaje=="yes":
    print("\n############### AJUSTAR MENSAJE ###############")
    #|A|B|C|D|E|F|G|H|I|J|K|L|M|N|Ñ|O|P|Q|R|S|T|U|V|W|X|Y|Z|
    #|D|K|I|P|A|X|J|T|O|N|R|Z|H|S|Ñ|F|M|B|C|Q|L|G|Y|W|E|V|U|
    #DKIPAXJTONRZHSÑFMBCQLGYWEVU

    listaLetrasAjustadas=input()
    mensajeDescifrado = mensaje.maketrans(alfabeto,listaLetrasAjustadas)
    mensajeDescifrado=mensaje.translate(mensajeDescifrado)
    print("\n############### MENSAJE DESCIFRADO ###############")
    print(mensajeDescifrado)





