alfabeto_codificado=['k','q','f','m','x','e','t','z','r','h','v','n','d','l','j','a','s','u','y','b','g','w','p','o','i','c']
alfabeto=['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z']
teen_team=['rex splode','atom eve','duplikate','robot']
qnt_times=int(input())
times=[[]for _ in range(qnt_times)]
poder_times=[[]for _ in range(qnt_times)]
acao=""

#variáveis e listas globais

while acao!="FIM": 
    acao=input()
    if acao=="adicionar":
        print("Quem será o próximo integrante do time?") 
        nome_poder=input()
        nome_codificado,poder_str=nome_poder.split(' - ')
        nome=""
        for letra in nome_codificado: #codificador
            if letra==" ":
                nome+=" "
            else:
                for i in range(len(alfabeto_codificado)):
                    if letra==alfabeto_codificado[i]:
                        nome+=alfabeto[i]
        if nome=="rex splode":
            print("Eu vou te detonar!")
        elif nome=="atom eve":
            print("Eu reescrevo a matéria... incluindo a SUA.")
        elif nome=="duplikate":
            print("Quantas de mim você acha que consegue lidar?")
        elif nome=="robot":
            print("Minha lógica diz que você vai perder.")
        poder=int(poder_str)
        n_time=int(input())
        times[n_time].append(nome)
        poder_times[n_time].append(poder)
    if acao=="metamorfo":
        print("Atenção!!! Metamorfo encontrado, quem deverá ser removido do time?")
        removido=input()
        print("Quem você gostaria de colocar no lugar?")
        nome_poder=input()
        nome_codificado,poder_str=nome_poder.split(' - ')
        nome=""
        for letra in nome_codificado: #codificador
            if letra==" ":
                nome+=" "
            else:
                for i in range(len(alfabeto_codificado)):
                    if letra==alfabeto_codificado[i]:
                        nome+=alfabeto[i]
        if nome=="rex splode":
            print("Eu vou te detonar!")
        elif nome=="atom eve":
            print("Eu reescrevo a matéria... incluindo a SUA.")
        elif nome=="duplikate":
            print("Quantas de mim você acha que consegue lidar?")
        elif nome=="robot":
            print("Minha lógica diz que você vai perder.")
        poder=int(poder_str)
        n_time=int(input())
        indice_removido=times[n_time].index(removido) #índice do elemento a ser removido
        poder_times[n_time].pop(indice_removido) #remoção
        times[n_time].remove(removido) #remoção
        times[n_time].append(nome)
        poder_times[n_time].append(poder)
        
#loop das ações

indice_teen_team=0
indice_atual=0
teen_team_bool=False
for sublista in times:
        if all(nome in sublista for nome in teen_team):
            teen_team_bool=True
            indice_teen_team=indice_atual
        indice_atual+=1
if teen_team_bool:
    print("O teen team esta completo, Cecil esta muito contente!")
    for i in range(len(poder_times[indice_teen_team])):
        #adiciona 10% a cada valor de poder
        poder_times[indice_teen_team][i]*=1.1

#verificação do teen team

somatorios=[]
for time_poder in poder_times: #somatório da força de cada time
    soma=0
    for poder in time_poder:
        soma+=poder
    somatorios.append(soma)
indices=list(range(len(times))) #lista de índices
n=len(indices)
for i in range(n): #ordenação
    for j in range(0,n-i-1): #bubble sort
        if somatorios[indices[j]]<somatorios[indices[j+1]]:
            indices[j], indices[j+1]=indices[j+1],indices[j]
times_ordenados=[]
poderes_ordenados=[]
for i in indices:
    times_ordenados.append(times[i])
    poderes_ordenados.append(poder_times[i])

#ordenação das listas

poderes_time_terra=poderes_ordenados[0]
time_terra=times_ordenados[0]
n=len(poderes_time_terra)
for i in range(n):
    for j in range(0, n - i - 1):
        if poderes_time_terra[j]<poderes_time_terra[j+1]:  
            poderes_time_terra[j], poderes_time_terra[j+1] = poderes_time_terra[j+1], poderes_time_terra[j]
            time_terra[j],time_terra[j+1]=time_terra[j+1], time_terra[j]
indice_luta=0
duelo=1
vit_herois=0
vit_viloes=0
viltrumitas=['general kregg','conquista','anissa'] #lista de viltrumitas
poderes_viltrumitas=[110,100,90]
print(f"Aqui está o poderoso time da terra: {', '.join(time_terra[:3])}")
for i in range(3): 
    print(f"{duelo} Duelo: {time_terra[indice_luta]} X {viltrumitas[indice_luta]}")
    if poderes_time_terra[indice_luta]>poderes_viltrumitas[indice_luta]:
        vit_herois+=1
    else:
        vit_viloes+=1
    indice_luta+=1
    duelo+=1

#laço da batalha

if vit_herois>vit_viloes:
    print("A terra venceu!")
else:
    print("Infelizmente o imperio viltrumita conquistou a terra!")

#prints do resultado
