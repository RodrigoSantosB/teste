"""
s - string
d - int 
f - float

.< número de dígitos >f
x e X - Hexadecimal (ABCDEF0123456789)
> - Esquerda 
< - Direita 
^ - Centro
Sinal - + ou -

Ex.: 0 > -100, .1f
Conversion flags - !r !s !a
"""

variavel = "ABC"
menu = "_MENU_"
print(f"{variavel}")
print(f"{variavel:*>10}") #preenche a esquerta com a quntida de caracteres passados (op de 'PAD')
print(f"{variavel:.<10}") #preenche a direita com a quntida de caracteres passados (op de 'PAD')
print(f"{variavel:,^10}") #preenche o centro com a quntida de caracteres passados (op de 'PAD')
print(f'{menu:#^50}')