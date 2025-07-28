# função para calcular a pontuação de um único jogador
def calculo_pontuacao(info_jogador):
    pontos=0
    # separação dos dados do jogador
    nome,posicao,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos=info_jogador.split(",")

    # conversão dos dados para números inteiros
    gols_feitos=int(gols_feitos)
    assistencias=int(assistencias)
    amarelos=int(amarelos)
    vermelhos=int(vermelhos)
    gols_sofridos=int(gols_sofridos)

    # cálculo dos pontos 
    pontos+=gols_feitos*8
    pontos+=assistencias*5 
    pontos-=amarelos*1
    pontos-=vermelhos*3

    # bônus do clean sheet
    if posicao=="goleiro" or posicao=="lateral" or posicao=="zagueiro":
        if gols_sofridos==0:
            pontos+=5

    return pontos,posicao,nome

# função para ler os titulares
def titulares():
    jogadores_por_posicao={
        "goleiro":[],"zagueiro":[],"lateral":[],
        "meia":[],"atacante":[]
    }
    pontos_time=0
    for i in range(11):
        info_jogador=input()
        pontos,posicao,nome=calculo_pontuacao(info_jogador)
        
        jogadores_por_posicao[posicao].append((pontos,nome))
        pontos_time+=pontos
    
    return pontos_time,jogadores_por_posicao

# função para ler os reservas
def reservas():
    reservas={}
    for _ in range(5):
        info_jogador=input()
        pontos,posicao,nome=calculo_pontuacao(info_jogador)
        reservas[posicao]=(pontos,nome)
    return reservas

# função auxiliar para encontrar o pior titular a ser substituído em uma posição
def encontrar_pior_titular(titulares_posicao):
    pior_pontuacao=titulares_posicao[0][0]
    nome_pior_jogador=titulares_posicao[0][1]

    i=1
    while i<len(titulares_posicao):
        pontuacao_atual=titulares_posicao[i][0]
        nome_atual=titulares_posicao[i][1]
        
        if pontuacao_atual<pior_pontuacao:
            pior_pontuacao=pontuacao_atual
            nome_pior_jogador=nome_atual
        elif pontuacao_atual==pior_pontuacao:
            if nome_atual>nome_pior_jogador:
                nome_pior_jogador=nome_atual
        i+=1
        
    return pior_pontuacao,nome_pior_jogador

def obter_chave_troca(item):
    return (item[0],-item[1])

# função da substituição inteligente
def substituicao_inteligente(pontos_time,titulares,reservas):
    # definição da prioridade de substituição
    prioridade_posicao={"goleiro":1,"lateral":2,"zagueiro":3,"meia":4,"atacante":5}
    
    possiveis_trocas=[]

    for posicao in reservas:
        reserva_pontos,reserva_nome=reservas[posicao]
        
        titulares_posicao=titulares[posicao]
        
        pior_titular_pontos,pior_titular_nome=encontrar_pior_titular(titulares_posicao)

        ganho=reserva_pontos-pior_titular_pontos

        if ganho>0:
            info_troca=(ganho,prioridade_posicao[posicao],pior_titular_nome,reserva_nome)
            possiveis_trocas.append(info_troca)

    if not possiveis_trocas:
        return pontos_time,False,"",""

    # ordena as trocas para encontrar a melhor
    trocas_ordenadas=sorted(possiveis_trocas,key=obter_chave_troca,reverse=True)

    melhor_troca=trocas_ordenadas[0]
    ganho_final=melhor_troca[0]
    titular_sai=melhor_troca[2]
    reserva_entra=melhor_troca[3]

    pontos_time_final=pontos_time+ganho_final
    
    return pontos_time_final,True,titular_sai,reserva_entra

def obter_pontuacao(resultado_tecnico):
    return resultado_tecnico[1]


n_tecnicos=int(input())
# lista para guardar todos os resultados antes de imprimir
resultados_gerais=[]

for i in range(n_tecnicos):
    nome_tecnico=input()

    comando1=input()
    if comando1=="titulares":
        pontos_time,titulares_info=titulares()
        input() 
        reservas_info=reservas()
    else: 
        reservas_info=reservas()
        input() 
        pontos_time,titulares_info=titulares()

    pontos_finais,fez_sub,titular_removido,reserva_adicionado=substituicao_inteligente(pontos_time,titulares_info,reservas_info)
    
    # guarda todas as informações necessárias para a impressão posterior
    info_completa=(nome_tecnico,pontos_finais,fez_sub,titular_removido,reserva_adicionado)
    resultados_gerais.append(info_completa)

# imprime a lista de todos os técnicos participantes
nomes_dos_tecnicos=[resultado[0] for resultado in resultados_gerais]
print(f"Os técnicos que participarão da avaliação da rodada serão {', '.join(nomes_dos_tecnicos)}.")

# imprime a mensagem de substituição para cada técnico
for resultado in resultados_gerais:
    nome_tecnico=resultado[0]
    fez_sub=resultado[2]
    titular_removido=resultado[3]
    reserva_adicionado=resultado[4]

    if fez_sub:
        print(f"{nome_tecnico} é um gênio da bola mesmo, a substituição de {titular_removido} por {reserva_adicionado} fez ele ganhar pontos!")
    else:
        print(f"Pode cortar {nome_tecnico} dos candidatos a técnico da amarelinha, nem fazer uma substituição ele consegue...")

# ordena os técnicos pela pontuação para encontrar o vencedor
resultados_ordenados=sorted(resultados_gerais,key=obter_pontuacao,reverse=True)

vencedor_info=resultados_ordenados[0]
vencedor_nome=vencedor_info[0]
vencedor_pontos=vencedor_info[1]
vencedor_fez_sub=vencedor_info[2]

# imprime a mensagem do vencedor
print(f"{vencedor_nome} é incrível ganhou essa rodada com {vencedor_pontos} pontos!")

# imprime a mensagem adicional se o vencedor não fez substituição
if not vencedor_fez_sub:
    print(f"Temos que pedir desculpas a {vencedor_nome}, mesmo sem fazer uma substituição ele foi o melhor da rodada, talvez ele deva assumir a amarelinha depois do Ancelotti!")