# continue + while

# Usado para ignorar um trecho uma execução no while
# sob determinada condição

cont = 0
max = 50

while cont < max:
    cont+=1
    
    # ex de uso do continue:
    if cont == 4:
        continue # ignora o valor de 4 e continua o fluxo do código
    
    print(cont)
    
    if cont > 10 and 27:
        print("ignorado ... ")
    