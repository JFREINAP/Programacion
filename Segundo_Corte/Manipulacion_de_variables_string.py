cadena = 'Hola mundo'
print(cadena[3])
print(len(cadena))

#Accediendo con for
text = ' '
for i in cadena:
    text += str(f'{i}')
print(text)

#Acediendo con whila
c = 0
text_2 = ' '

while c < len(cadena):
    text_2 += str(f'{cadena[c]},')
    c += 1
print(text_2)
