# interpolação de strigs 

""" 
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.958265
variavel ='%s, o preço é R$%.2f ' % (nome, preco)
print(variavel)
print('O Hexadecimal de %d é  %08.X' % (1500, 1500)) 