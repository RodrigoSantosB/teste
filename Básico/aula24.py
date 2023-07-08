# Operador in e not in 
# Strings iteraveis 

nome = 'Rodrigo'

print(nome[1])
print('R' in nome)
print('A' in nome)
print('Rod' in nome)
 
 
# Aplicação:

nome = input("Digite seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome:
    print(f"{encontrar} está em {nome}")
else:
    print(f"{encontrar} não está em {nome}")
