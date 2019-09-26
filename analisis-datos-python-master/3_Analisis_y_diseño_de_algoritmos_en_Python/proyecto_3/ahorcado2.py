#importar módulo time
import time

print("Hola! Vamos a jugar ahocardo!\n")
time.sleep(1)
print("Comencemos...")
time.sleep(0.5)

#fijamos la cantidad de oportunidades y guardamos palabra secreta
oportunidades = 10
palabra_secreta = "GERARDO".upper()

#variable que va a ir guardando las respuestas del usuario
respuetas_de_usuario = ''

#ciclo que se repite mientras el usuario tenga oportunidades
while oportunidades > 0:
    # make a counter that starts with zero
    faltantes = 0

    #vamos letra por letra en la palabra secreta (A,R,I,S,T,O,T,E,L,E,S)
    for letra in palabra_secreta:
        # see if the character is in the players guess
        if letra in respuetas_de_usuario:
            print(letra, " ", end="")
        else:
            print("_ ", end=""),
            #incrementar letras faltantes en 1
            faltantes += 1

    if faltantes == 0:
        print("\n\nGANASTE!!!")
        break

    # pedir la letra que quiere intentar el usuario
    intento_de_usuario = input("\n\nAdivina una letra:").upper()

    # set the players guess to guesses
    respuetas_de_usuario += intento_de_usuario
    print("respuetas_de_usuario", respuetas_de_usuario)
    # si la adivinanza no está en la palabra secreta...
    if intento_de_usuario not in palabra_secreta:
        # restar una oportunidad
        oportunidades -= 1
        print("NO! La letra '", intento_de_usuario, "' no está en la palabra secreta")
        print("Te quedan", + oportunidades, 'oportunidades')
        #si ya no quedan oportunidades...
        if oportunidades == 0:
            print("Perdiste! Te quedaste sin oportunidades.")