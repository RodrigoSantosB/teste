"""
EXERCICIO

Peça ao usuario para digitar seu nome
Peça ao usuario para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contem ou não espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    Exiba:
        "Desculpe, você deixou compos vazios"
"""

nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
print()
msg = "Desculpe, você deixou compos vazios"
nome_invetido = nome[::-1]
p_letra = nome[0]
u_letra = nome[-1]
n = len(nome)

if (nome and idade) or (idade and nome):
    print(f"Seu nome é {nome}\n")
    print(f"Seu nome invetido é {nome_invetido}\n")
    if ' ' in nome:
        print("Seu nome contem espaços\n")
    else:
        print("Seu nome não contem espaços\n")
        
    print(f"Seu nome contem {n} Letras\n")
    print(f"A primeira letra do seu nome é {p_letra}\n")
    print(f"A última letra do seu nome é {u_letra}\n")
    print(f"Sua idade é {idade}")
else:  
    print(f"{msg}")
