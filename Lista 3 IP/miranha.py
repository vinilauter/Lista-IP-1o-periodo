N=int(input())
cidade=[]
dias_sem_restaurar=0
dias_totais=0
fim=False
quarteiroes_restaurados=0
quarteiroes_destruidos=0
quarteiroes_corrompidos=0

for i in range(N): #input das linhas
    linha=input().split()
    cidade.append(linha)
    for j in range(N):
        if linha[j]=='H': #verificação da posição do miranha
            linha_miranha=i
            coluna_miranha=j
        if linha[j]=='E': #verificação de quarteirões corrompidos
            quarteiroes_corrompidos+=1
        if linha[j]=='X':
            quarteiroes_destruidos+=1

while fim==False and dias_totais<8: #condicional da missão do miranha
    acao=input()
    cidade[linha_miranha][coluna_miranha]="." #restauração da antiga posição
    if acao=="Esquerda":
        coluna_miranha-=1
    elif acao=="Direita":
        coluna_miranha+=1
    elif acao=="Baixo":
        linha_miranha+=1
    elif acao=="Cima":
        linha_miranha-=1
    #movimentação do miranha
    if linha_miranha<0 or coluna_miranha<0 or cidade[linha_miranha][coluna_miranha]=='X' or linha_miranha>=N or coluna_miranha>=N: #movimentação errada
        if acao=="Esquerda":
            coluna_miranha+=1
        elif acao=="Direita":
            coluna_miranha-=1
        elif acao=="Baixo":
            linha_miranha-=1
        elif acao=="Cima":
            linha_miranha+=1
        cidade[linha_miranha][coluna_miranha]="H"
        dias_totais+=1
        dias_sem_restaurar+=1
        print(f"Dia {dias_totais}")
        for i in range(N):
            print(f"{' '.join(cidade[i])}")
        print(f"Posição atual do Homem-Aranha: ({linha_miranha}, {coluna_miranha})")
        print(f"Quarteirões restaurados: {quarteiroes_restaurados} | Quarteirões destruídos: {quarteiroes_destruidos}")
        print("Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!")
        print()
    elif cidade[linha_miranha][coluna_miranha]=="." and acao!="FIM": #moviementação sem restaurar
        cidade[linha_miranha][coluna_miranha]="H"
        dias_sem_restaurar+=1
        dias_totais+=1
        if dias_sem_restaurar==3: #destruição pelo Electro
            if quarteiroes_corrompidos>0:
                dias_sem_restaurar=0
                alvo_encontrado=False
                i=0
                while i<N and not alvo_encontrado:
                    j=0
                    while j<N and not alvo_encontrado:
                        if cidade[i][j]=='E':
                            cidade[i][j]='X'
                            quarteiroes_corrompidos-=1
                            quarteiroes_destruidos+=1
                            alvo_encontrado=True
                        j+=1
                    i+=1 
        print(f"Dia {dias_totais}")
        for i in range(N):
            print(f"{' '.join(cidade[i])}")
        print(f"Posição atual do Homem-Aranha: ({linha_miranha}, {coluna_miranha})")
        print(f"Quarteirões restaurados: {quarteiroes_restaurados} | Quarteirões destruídos: {quarteiroes_destruidos}")
        print("O Electro está ganhando espaço!")
        print()
    elif cidade[linha_miranha][coluna_miranha]=="E": #movimentação restaurando
        cidade[linha_miranha][coluna_miranha]="H"
        dias_sem_restaurar=0
        quarteiroes_corrompidos-=1
        quarteiroes_restaurados+=1
        dias_totais+=1
        print(f"Dia {dias_totais}")
        for i in range(N):
            print(f"{' '.join(cidade[i])}")
        print(f"Posição atual do Homem-Aranha: ({linha_miranha}, {coluna_miranha})")
        print(f"Quarteirões restaurados: {quarteiroes_restaurados} | Quarteirões destruídos: {quarteiroes_destruidos}")
        print("O Miranha restaurou um quarteirão!")
        print()
    if quarteiroes_corrompidos==0: #print da vitória
        if quarteiroes_restaurados>0:
            print("Missão cumprida! Nova York está segura e o Miranha faz tudo novamente!")
        fim=True
    if acao=="FIM": #print se a ação for "FIM"
        if quarteiroes_corrompidos>0:
            print("Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!")
        fim=True
    if dias_totais==8 and quarteiroes_corrompidos>0: #print da derrota
        print("O Miranha não conseguiu restaurar a cidade a tempo, o Electro venceu!")
    