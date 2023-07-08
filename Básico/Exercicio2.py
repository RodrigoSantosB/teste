"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
def nunInt():
    inteiro = input("Digite um número inteiro: ")
    parImpar = None
    if inteiro.isdigit():
        inteiro = int(inteiro)
        parImpar = inteiro%2 == 0
        if parImpar:
            print("Número é par\n")
        else:
            print("Número é impar\n")
    else:
        print(" Você não digitou um numero\n")
        nunInt()


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
def saudacao():
        
    try:
        hora  = int(input("Digite a hora: "))
        manha = hora >= 0 and hora <=11
        tarde = hora >=12 and hora <=17
        noite = hora >=18 and hora <=23
        
        if manha:
            print("Bom dia\n")
        elif tarde:
            print("Boa tarde\n")
        elif noite:
            print("Boa noite")
        else:
            print("Hora inválida\n")
            saudacao()
    except:
        print("Entre com um número inteiro\n")
        saudacao()
"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
def verificaNome():
    nome = input("Digite seu nome: ")
    
    curto  = len(nome) < 4
    medio  = len(nome) >=5 and len(nome) <=6
    grande = len(nome) > 6
    
    if len(nome) > 1:
        if curto:
            print("Seu nome é curto ") 
        elif medio:
            print("Seu nome é normal ")
        else:
            print("Seu nome é muito grande ")
    else:
        print("Digite mais de uma letra\n")
        verificaNome()
         
        


def main():
    verificaNome()
    
        

if __name__ == '__main__':
    main()

    