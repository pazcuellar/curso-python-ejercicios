from os import system
def clear_console():
    system('clear')

print("Bienvenido al Ahorcado!!!")
print("Comencemos!")
print("Presiona cualquier tecla para continuar...")
input()

palabra_secreta = 'GERARDO'
letras_correctas = []
oportunidades = 10
restantes = []
for letra in palabra_secreta:
    if letra not in restantes:
        restantes.append(letra)
#restantes = ['P' , 'Y', 'T' , 'H', 'O' , 'N']

def mostrar_casillas(correctas):
    for letra in palabra_secreta:
        if letra in correctas:
            print(letra, end='')
        else:
            print(" __ ", end='')
    print("\n")




while oportunidades > 0 and len(restantes) > 0:
    print("Te quedan {} oportunidades".format(oportunidades))
    mostrar_casillas(letras_correctas)
    adivinanza = input("Adivina una letra: ")
    clear_console()
    if adivinanza in palabra_secreta:
        letras_correctas.append(adivinanza)
        restantes.remove(adivinanza)
    else:
        oportunidades -= 1
    
if len(restantes) == 0:
    print("GANASTE!!")
else:
    print("PERDISTE!")
input()
    
    #si el usuario adivina una letra
        #colocamos la letra
    #si se equivoca el usuario
        #restaruna oportunidades