first_initial = {'A' : 'Amanzing', 'B' : 'Brilliant', 'C' : 'Awesome', 
'D' : 'Incredible', 'E' : 'Uncanny', 'F' : 'Impossible', 'G' : 'Unbelievable', 
'H' : 'Surprisingly', 'I' : 'Unexpected', 'J' : 'Dastardly', 'K' : 'Evil', 
'L' : 'Monstrous', 'M' : 'Preposterous', 'N' : 'Alarming', 'O' : 'Insane', 
'P' : 'Terrifying', 'Q' : 'Unthinkable', 'R' : 'Absurd', 'S' : 'Improbable', 
'T' : 'Outlandish', 'U' : 'Questionable', 'V' : 'Ridiculous', 'W' : 'Erotic', 
'X' : 'Unfathomable', 'Y' : 'Inconceivable', 'Z' : 'Unimaginable'}

second_initial = {'A' : 'Giant', 'B' : 'Tiny', 'C' : 'Shrinking', 
'D' : 'Magic', 'E' : 'Slimy', 'F' : 'Flying', 'G' : 'Angry', 
'H' : 'Crazy', 'I' : 'Shiny', 'J' : 'Golden', 'K' : 'Sticky', 
'L' : 'Diamond', 'M' : 'Flaming', 'N' : 'Psychic', 'O' : 'Silent', 
'P' : 'Screaming', 'Q' : 'Jumping', 'R' : 'Crouching', 'S' : 'Friendly',
'T' : 'Omnipotent', 'U' : 'Dripping', 'V' : 'Flimsy', 'W' : 'Hairy', 
'X' : 'Translucent', 'Y' : 'Strange', 'Z' : 'Silver'}

last_initial = {'A' : 'Man', 'B' : 'Moth', 'C' : 'Goat', 
'D' : 'Princess', 'E' : 'Girl', 'F' : 'Machine', 'G' : 'Cat', 
'H' : 'Balloon', 'I' : 'Ant', 'J' : 'Bee', 'K' : 'Wolf', 
'L' : 'Bear', 'M' : 'Lion', 'N' : 'Ball', 'O' : 'Ghost', 
'P' : 'Witch', 'Q' : 'Vampire', 'R' : 'Hand', 'S' : 'Foot',
'T' : 'Tornado', 'U' : 'Fish', 'V' : 'Millipede', 'W' : 'Rock', 
'X' : 'Nose', 'Y' : 'Dog', 'Z' : 'Boy'}


def dame_nombre():
    while True:
        print('Dame tu nombre: ')
        nombre = input().upper()
        return nombre

def genera_nombre(nombre, dicc1, dicc2, dicc3):
   first_symbol = nombre[0]
   second_symbol = nombre [1]
   ultimo = int(len(nombre)) -1
   last_symbol = nombre[ultimo]

   if first_symbol in dicc1:
        nombre_uno = dicc1[first_symbol]
   if second_symbol in dicc2:
        nombre_dos = dicc2[second_symbol]
   if last_symbol in dicc3:
        nombre_ultimo = dicc3[last_symbol]

   print(" tu nombre es:", nombre_uno, nombre_dos, nombre_ultimo)

nombre = dame_nombre()
genera_nombre(nombre, first_initial, second_initial, last_initial)  



         
