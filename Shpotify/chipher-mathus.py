from os import system
def clear_console():
    system('clear')


tamanio_max_psw = 26

def selecMode():
    while True:
        print('Hola! ¿Quieres encriptar o desencriptar?')
        mode = input()
        if mode in 'encriptar e desencriptar d'.split():
            return mode
        else:
            print('Para encriptar escribe "encriptar" o "e", si por el contrario quieres desencriptar pulsa "desenciptar" o "d"')

def mensaje():
    print('Ingresa tu mensaje:')
    return input().upper()

def pasword():
    keyy = ''
    while True: 
        print('Ingresa la llave: ')
        keyy = (input())
        key_clean = ''
        for letra in keyy:
            if letra not in key_clean:
                key_clean += letra
         
        len_key = len(key_clean)
    
        if len_key >= 1 and len_key <= 26 :
            u_key = key_clean.upper()
            return u_key

mode = selecMode()
mensaje = mensaje()
pasword = pasword()
clear_console()

alfabeto_real = list('ABCDEFGHIJKLMNÑOPQRSTUVWXYZ')

alfabeto_secreto = list(pasword)


for letra in alfabeto_real:
    if letra not in alfabeto_secreto:
        alfabeto_secreto.append(letra)


cipher = {}
indice = 0
for letra in alfabeto_real:
    cipher[letra] = alfabeto_secreto[indice]
    indice += 1


cipher_invertido = {}
indice = 0
for letra in alfabeto_secreto:
    cipher_invertido[letra] = alfabeto_real[indice]
    indice += 1


def traducir_mensaje(mode, mensaje ):
    translated = ''
    if mode[0] == 'e':
  
        for letra in mensaje: 
            if letra == ' ':
                translated += ' '
            else:
                translated += cipher[letra]

    elif mode[0] == 'd':
    
        for letra in mensaje: 
             if letra == ' ':
                translated += ' '
             else:
                translated += cipher_invertido[letra]

    return translated



print('Tu mensaje es:')
print(traducir_mensaje(mode, mensaje))
print('Adiós!')