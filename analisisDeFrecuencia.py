
######################################################## ANÁLISIS DE FRECUENCIA ########################################################

from collections import Counter

mensajeLabo="RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE. AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK HKCZJOI OKEJSZCNHE."
alfabeto="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
frecuencia="EAOLSNDRUITCPMYQBHGFVJÑZXKW"
listaCaracteresOrdenada=""
print("Escribe el mensaje que quieres descrifrar:")
mensaje=input()
#Para contar la letras del mensaje
counter=Counter(mensaje)
listaLetras= {}
for caracter in alfabeto:
    listaLetras[caracter]=counter[caracter]
listaOrdenada = sorted(listaLetras.items(), key=lambda x: x[1], reverse=True)
print(listaOrdenada)
for i in range(len(listaOrdenada)):
    listaCaracteresOrdenada= listaCaracteresOrdenada + listaOrdenada[i][0]

mensajeDescifrado = mensaje.maketrans(listaCaracteresOrdenada, frecuencia)
print("############### MENSAJE CIFRADO ###############")
print(mensaje)
print("############### FRECUENCIAS ###############")
print(frecuencia)
print("############### CARACTERES ORDENADOS DE MAYOR FRECUENCIA A MENOS ###############")
print(listaCaracteresOrdenada)
print("############### MENSAJE DESCIFRADO ###############")
mensajeDescifrado=mensaje.translate(mensajeDescifrado)
print(mensajeDescifrado)
print("############### AJUSTAR MENSAJE ###############")
#|A|B|C|D|E|F|G|H|I|J|K|L|M|N|Ñ|O|P|Q|R|S|T|U|V|W|X|Y|Z|
#|D|K|I|P|A|X|J|T|O|N|R|Z|H|S|Ñ|F|M|B|C|Q|L|G|Y|W|E|V|U|
#DKIPAXJTONRZHSÑFMBCQLGYWEVU

listaLetrasAjustadas=input();
mensajeDescifrado = mensaje.maketrans(alfabeto,listaLetrasAjustadas)
mensajeDescifrado=mensaje.translate(mensajeDescifrado)
print(mensajeDescifrado)




