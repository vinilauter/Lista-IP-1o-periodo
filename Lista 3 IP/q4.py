print("Go! Go! Power Rangers!")
sequencia=input() #input dos zords e nível de força
zords=sequencia.split('-') #separação dos integrantes do input
nomes=[] #nomes dos zords
nivel=[] #níveis dos zords
nomes_tipo1=[] #separação pro tipo 1
forca_tipo1=[] #separação pro tipo 1
nomes_tipo2=[] #separação pro tipo 2
forca_tipo2=[] #separação pro tipo 2
nomes_tipo3=[] #separação pro tipo 3
forca_tipo3=[] #separação pro tipo 3

#variáveis e listas iniciais

i = 0 
while i<len(zords):
    # Se o item atual for um nome (posições pares: 0, 2, 4...)
    if i%2==0:
        nomes.append(zords[i])
    # Se o token atual for um número (posições ímpares: 1, 3, 5...)
    else:
        nivel.append(int(zords[i]))
    i+=1

#laço para a separação dos nomes e níveis de força

i = 0 
while i<len(nivel):
    if nivel[i]<=10:
        forca_tipo3.append(nivel[i])
        nomes_tipo3.append(nomes[i])
    elif nivel[i]<=30:
        forca_tipo2.append(nivel[i])
        nomes_tipo2.append(nomes[i])
    elif nivel[i]>30:
        forca_tipo1.append(nivel[i])
        nomes_tipo1.append(nomes[i])
    i+=1

#ordenação por tipo

n = len(forca_tipo1)
for i in range(n):
    for j in range(0,n-i-1):
        if forca_tipo1[j]<forca_tipo1[j+1]:
            # trocar forças
            temp_forca=forca_tipo1[j]
            forca_tipo1[j]=forca_tipo1[j+1]
            forca_tipo1[j+1]=temp_forca
            # trocar nomes no mesmo índice
            temp_nome=nomes_tipo1[j]
            nomes_tipo1[j]=nomes_tipo1[j+1]
            nomes_tipo1[j+1]=temp_nome

#ordenação por força no tipo 1

n = len(forca_tipo2)
for i in range(n):
    for j in range(0,n-i-1):
        if forca_tipo2[j]<forca_tipo2[j+1]:
            # trocar forças
            temp_forca=forca_tipo2[j]
            forca_tipo2[j]=forca_tipo2[j+1]
            forca_tipo2[j+1]=temp_forca
            # trocar nomes no mesmo índice
            temp_nome=nomes_tipo2[j]
            nomes_tipo2[j]=nomes_tipo2[j+1]
            nomes_tipo2[j+1]=temp_nome

#ordenação por força no tipo 2 

n = len(forca_tipo3)
for i in range(n):
    for j in range(0,n-i-1):
        if forca_tipo3[j]<forca_tipo3[j+1]:
            # trocar forças
            temp_forca=forca_tipo3[j]
            forca_tipo3[j]=forca_tipo3[j+1]
            forca_tipo3[j+1]=temp_forca
            # trocar nomes no mesmo índice
            temp_nome=nomes_tipo3[j]
            nomes_tipo3[j]=nomes_tipo3[j+1]
            nomes_tipo3[j+1]=temp_nome

#ordenação por força no tipo 3

if 'robocin' in nomes:
    print("Os rangers encontraram o zord lendário!!!! O Robocin!!!! Eles não precisam mais de outros zords!")
else:
    if len(nomes_tipo1)>0: #prints do tipo 1
        print(f"Zord do Ranger Vermelho: {nomes_tipo1[0]}")
        if len(nomes_tipo1)>1:
            print(f"Zord do Ranger Verde: {nomes_tipo1[1]}")
        else: 
            print("Ranger Verde ficou sem zord!")
    elif not len(nomes_tipo1)>0:
        print("Ranger Vermelho ficou sem zord!")
        print("Ranger Verde ficou sem zord!")
    if len(nomes_tipo2)>0: #prints do tipo 2
        print(f"Zord da Ranger Rosa: {nomes_tipo2[0]}")
        if len(nomes_tipo2)>1:
            print(f"Zord do Ranger Preto: {nomes_tipo2[1]}")
        else: 
            print("Ranger Preto ficou sem zord!")
    elif not len(nomes_tipo2)>0:
        print("Ranger Rosa ficou sem zord!")
        print("Ranger Preto ficou sem zord!")
    if len(nomes_tipo3)>0: #prints do tipo 3
        print(f"Zord do Ranger Azul: {nomes_tipo3[0]}")
        if len(nomes_tipo3)>1:
            print(f"Zord da Ranger Amarela: {nomes_tipo3[1]}")
        else: 
            print("Ranger Amarela ficou sem zord!")
    elif not len(nomes_tipo3)>0:
        print("Ranger Azul ficou sem zord!")
        print("Ranger Amarela ficou sem zord!")

#prints de atribuição de zords

if not 'robocin' in nomes:
    if len(nomes_tipo1)>0:
        print(f"Zords do tipo 1: {', '.join(nomes_tipo1)}")
    else:
        print("Não temos nenhum zord do tipo 1 :(")
    if len(nomes_tipo2)>0:
        print(f"Zords do tipo 2: {', '.join(nomes_tipo2)}")
    else:
        print("Não temos nenhum zord do tipo 2 :(")
    if len(nomes_tipo3)>0:
        print(f"Zords do tipo 3: {', '.join(nomes_tipo3)}")
    else:
        print("Não temos nenhum zord do tipo 3 :(")
    if len(nomes_tipo1)<2 or len(nomes_tipo2)<2 or len(nomes_tipo3)<2:
        print("Ai ai ai, essa não!! Não temos zords suficientes para formar o Megazord! Os ranger não vão conseguir derrotar Rita!")
    else:
        print("Os Rangers estão prontos para montar o Megazord e derrotar Rita!")
