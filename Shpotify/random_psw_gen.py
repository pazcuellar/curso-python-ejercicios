from random import choice

longitud = int(input("cuantos caracteres debe tener la contraseña?: "))
valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

pasword = ""
pasword = pasword.join([choice(valores) for i in range(longitud)])
print(pasword)