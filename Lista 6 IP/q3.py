# função para a definição dos confrontos

def cruzamento(grupos,grupo_x,grupo_y,chave):
    print()
    print(f"Confrontos chave {chave}:")
    print(f"{grupos[int(grupo_x)][0]} x {grupos[int(grupo_y)][1]}")
    print(f"{grupos[int(grupo_x)][1]} x {grupos[int(grupo_y)][0]}")
    chave+=1
    return chave

# função para a ordenação pelo sorted() funcionar

def pegar_os_pontos(item_tupla):
    return item_tupla[1]

# programa principal

qtd_grupos=int(input())
grupos={}

# input dos grupos, ordenação e adição ao dicionário principal

for indice_grupo in range(qtd_grupos):

    # primeiro ordenando o grupo, passando como tupla para o dicionário principal

    ordenador={}
    for i in range(4):
        info=input()
        time,pts=info.split(" - ")
        ordenador[time]=int(pts)

    times_ordenados_tuplas=sorted(ordenador.items(),key=pegar_os_pontos,reverse=True)

    # agora adicionando a lista ordenada ao respectivo grupo

    lista_times_ordenados=[]
    for tupla in times_ordenados_tuplas:
        lista_times_ordenados.append(tupla[0])

    grupos[indice_grupo+1]=lista_times_ordenados

# validação e cruzamento dos confrontos

if qtd_grupos<2 or qtd_grupos%2!=0:
    print(f"Mas como que vamos fazer um torneio com {qtd_grupos} grupos Samir!?")
else:
    print("Roda os dados Samir!")

    chave=1
    for i in range(qtd_grupos//2):
        chaveamento=input()
        grupo_x,grupo_y=chaveamento.split(" x ")
        chave=cruzamento(grupos,grupo_x,grupo_y,chave)
    
# print do reBaixados 🦁🦁🦁

    print()
    for i in range(qtd_grupos):
        print(f"O time {grupos[i+1][-1]} ficou em último lugar em seu grupo e foi rebaixado!")