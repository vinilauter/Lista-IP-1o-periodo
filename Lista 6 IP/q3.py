# função para a definição dos confrontos

def cruzamento(grupos,grupo_x,grupo_y,chave):
    print()
    print(f"Confrontos chave {chave}:")
    print(f"{grupos[grupo_x][0]} x {grupos[grupo_y][1]}")
    print(f"{grupos[grupo_x][1]} x {grupos[grupo_y][0]}")
    chave+=1
    return chave

# programa principal

qtd_grupos=int(input())
grupos={}
chave=1

i=1
for i in range(qtd_grupos-1):
    grupos[grupo_i]
