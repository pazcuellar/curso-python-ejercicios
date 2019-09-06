tamanio_max_psw = 26

def selecMode():
    while True:
        print('Quiere encriptar o desencriptar?')
        mode = input()
        if mode in 'encriptar e desencriptar d'.split():
            return mode
        else:
            print('Para encriptar escribe "encriptar" o "e", si por el contrario quieres desencriptar pulsa "desenciptar" o "d"')

def mensaje():
    print('Ingresa tu mensaje:')
    return input()

def pasword():
    key = 0
    while True: 
        print('Ingresa la llave (1-26)')
        key = int(input())
        if key >= 1 and key <= 26 :
            return key

def traducir_mensaje(mode, mensaje, key):
    if mode[0] == 'd':
        key = -key
    translated = ''

    for symbol in mensaje: 
        if symbol.isalpha():
            num = ord(symbol)
            num += key

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            
            translated += chr(num)
        else:
            translated += symbol

    return translated




mode = selecMode()
mensaje = mensaje()
pasword = pasword()

print('Tu mensaje es:')
print(traducir_mensaje(mode, mensaje, pasword))