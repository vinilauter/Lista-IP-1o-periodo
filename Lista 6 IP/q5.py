# função para cálculo de pontuação do jogador titular

def calculo_pontuacao(jogador):
    pontos=0

    # separação dos dados

    nome,posicao,gols_feitos,assistencias,amarelos,vermelhos,gols_sofridos=jogador.split(",")

    # adição de pontos por gol

    for i in range(int(gols_feitos)):
        pontos+=8

    # adição de pontos por assistências

    for i in range(int(assistencias)):
        pontos+=4

    # adição de pontos por cartões amarelos

    for i in range(int(amarelos)):
        pontos-=1

    # adição de pontos por cartões vermelhos

    for i in range(int(vermelhos)):
        pontos-=3

    # adição de pontos por clean sheet

    if posicao=="goleiro" or posicao=="lateral" or posicao=="zagueiro":
        if gols_sofridos=="0":
            pontos+=5
        if gol_sofrido!="0":
            gol_sofrido=True
    return pontos,gol_sofrido,posicao,nome

# função para recepção do time titular

def titulares(pontos_time,pontos_goleiros,pontos_zagueiros,pontos_laterais,pontos_meias,pontos_atacantes,goleiros_lista,zagueiros_lista,laterais_lista,meias_lista,atacantes_lista):

    gol_sofrido=False

    for i in range(11):
        jogador=input()
        pontos,gol_sofrido,posicao,nome=calculo_pontuacao(jogador,gol_sofrido)
        if posicao=="goleiro":
            pontos_goleiros.append(pontos)
            goleiros_lista.append(nome)
            pontos_time+=pontos
        elif posicao=="zagueiro":
            pontos_zagueiros.append(pontos)
            zagueiros_lista.append(nome)
            pontos_time+=pontos
        elif posicao=="lateral":
            pontos_laterais.append(pontos)
            laterais_lista.append(nome)
            pontos_time+=pontos
        elif posicao=="meia":
            pontos_meias.append(pontos)
            meias_lista.append(nome)
            pontos_time+=pontos 
        elif posicao=="atacante":
            pontos_atacantes.append(pontos)
            atacantes_lista.append(nome)
            pontos_time+=pontos
    
    return pontos_time,pontos_goleiros,pontos_zagueiros,pontos_laterais,pontos_meias,pontos_atacantes,goleiros_lista,zagueiros_lista,laterais_lista,meias_lista,atacantes_lista

# função para recepção do time reserva

def reservas(pontos_goleiros_reservas,pontos_zagueiros_reservas,pontos_laterais_reservas,pontos_meias_reservas,pontos_atacantes_reservas,goleiros_lista_reservas,zagueiros_lista_reservas,laterais_lista_reservas,meias_lista_reservas,atacantes_lista_reservas):

    gol_sofrido=False

    for i in range(5):
        jogador=input()
        pontos,gol_sofrido,posicao=calculo_pontuacao(jogador,gol_sofrido)
        if posicao=="goleiro":
            pontos_goleiros_reservas.append(pontos)
            goleiros_lista_reservas.append(jogador)
        elif posicao=="zagueiro":
            pontos_zagueiros_reservas.append(pontos)
            zagueiros_lista_reservas.append(jogador)
        elif posicao=="lateral":
            pontos_laterais_reservas.append(pontos)
            laterais_lista_reservas.append(jogador)
        elif posicao=="meia":
            pontos_meias_reservas.append(pontos)
            meias_lista_reservas.append(jogador)
        elif posicao=="atacante":
            pontos_atacantes_reservas.append(pontos)
            atacantes_lista_reservas.append(jogador)
        
    return pontos_goleiros_reservas,pontos_zagueiros_reservas,pontos_laterais_reservas,pontos_meias_reservas,pontos_atacantes_reservas,goleiros_lista_reservas,zagueiros_lista_reservas,laterais_lista_reservas,meias_lista_reservas,atacantes_lista_reservas

# função da substituição inteligente

def sub_inteligente(pontos_time,pontos_goleiros_reservas,pontos_zagueiros_reservas,pontos_laterais_reservas,pontos_meias_reservas,pontos_atacantes_reservas,goleiros_lista_reservas,zagueiros_lista_reservas,laterais_lista_reservas,meias_lista_reservas,atacantes_lista_reservas,pontos_goleiros,pontos_zagueiros,pontos_laterais,pontos_meias,pontos_atacantes,goleiros_lista,zagueiros_lista,laterais_lista,meias_lista,atacantes_lista):

    for i in range(5):
        # pontuações hipotéticas se houver substituição
        if i==0:
            indice_minimo_goleiros=pontos_goleiros.index(min(pontos_goleiros))
            if min(pontos_goleiros)<pontos_goleiros_reservas[0]:
                pontos_time_copia_goleiro=pontos_time
                pontos_time_copia_goleiro=pontos_time_copia_goleiro-pontos_goleiros[indice_minimo_goleiros]+pontos_goleiros_reservas[0]
        elif i==1:
            indice_minimo_zagueiros=pontos_zagueiros.index(min(pontos_zagueiros))
            if min(pontos_zagueiros)<pontos_zagueiros_reservas[0]:
                pontos_time_copia_zagueiro=pontos_time
                pontos_time_copia_zagueiro=pontos_time_copia_zagueiro-pontos_zagueiros[indice_minimo_zagueiros]+pontos_zagueiros_reservas[0]
        elif i==2:
            indice_minimo_laterais=pontos_laterais.index(min(pontos_laterais))
            if min(pontos_laterais)<pontos_laterais_reservas[0]:
                pontos_time_copia_lateral=pontos_time
                pontos_time_copia_lateral=pontos_time_copia_lateral-pontos_laterais[indice_minimo_laterais]+pontos_laterais_reservas[0]
        elif i==3:
            indice_minimo_meias=pontos_meias.index(min(pontos_meias))
            if min(pontos_meias)<pontos_meias_reservas[0]:
                pontos_time_copia_meia=pontos_time
                pontos_time_copia_meia=pontos_time_copia_meia-pontos_meias[indice_minimo_meias]+pontos_meias_reservas[0]
        elif i==4:
            indice_minimo_atacantes=pontos_atacantes.index(min(pontos_atacantes))
            if min(pontos_atacantes)<pontos_atacantes_reservas[0]:
                pontos_time_copia_atacante=pontos_time
                pontos_time_copia_atacante=pontos_time_copia_atacante-pontos_atacantes[indice_minimo_atacantes]+pontos_atacantes_reservas[0]

            # pontuação máxima com substituição
        maximo_pontos=max(pontos_time_copia_goleiro,pontos_time_copia_zagueiro,pontos_time_copia_lateral,pontos_time_copia_meia,pontos_time_copia_atacante)
        if maximo_pontos!=pontos_time:
            pontos_time=maximo_pontos
            if pontos_time_copia_goleiro==maximo_pontos:
                print(f"{nome_tecnico} é um gênio da bola mesmo, a substituição de {goleiros_lista[indice_minimo_goleiros]} por {goleiros_lista_reservas[0]} fez ele ganhar pontos!")
            elif pontos_time_copia_zagueiro==maximo_pontos:
                print(f"{nome_tecnico} é um gênio da bola mesmo, a substituição de {zagueiros_lista[indice_minimo_zagueiros]} por {zagueiros_lista_reservas[0]} fez ele ganhar pontos!")
            elif pontos_time_copia_lateral==maximo_pontos:
                print(f"{nome_tecnico} é um gênio da bola mesmo, a substituição de {laterais_lista[indice_minimo_laterais]} por {laterais_lista_reservas[0]} fez ele ganhar pontos!")
            elif pontos_time_copia_meia==maximo_pontos:
                print(f"{nome_tecnico} é um gênio da bola mesmo, a substituição de {meias_lista[indice_minimo_meias]} por {meias_lista_reservas[0]} fez ele ganhar pontos!")
            elif pontos_time_copia_atacante==maximo_pontos:
                print(f"{nome_tecnico} é um gênio da bola mesmo, a substituição de {atacantes_lista[indice_minimo_atacantes]} por {atacantes_lista_reservas[0]} fez ele ganhar pontos!")

# programa principal

# recepção dos técnicos 

n_tecnicos=int(input())

for i in range(n_tecnicos):
    # input do técnico

    nome_tecnico=input()
    escalacao=input()

    # flag para titulares

    titulares=False

    # listas para titulares

    pontos_goleiros=[]
    pontos_zagueiros=[]
    pontos_laterais=[]
    pontos_meias=[]
    pontos_atacantes=[]

    goleiros_lista=[]
    zagueiros_lista=[]
    laterais_lista=[]
    meias_lista=[]
    atacantes_lista=[]

    # listas para reservas

    pontos_goleiros_reservas=[]
    pontos_zagueiros_reservas=[]
    pontos_laterais_reservas=[]
    pontos_meias_reservas=[]
    pontos_atacantes_reservas=[]

    goleiros_lista_reservas=[]
    zagueiros_lista_reservas=[]
    laterais_lista_reservas=[]
    meias_lista_reservas=[]
    atacantes_lista_reservas=[]

    # pontos totais do time

    pontos_time=0

    # condicionais para recepção de titulares ou reservas
     
    if escalacao=="titulares":

        titulares=True
        pontos_time,pontos_goleiros,pontos_zagueiros,pontos_meias,pontos_laterais,pontos_atacantes,goleiros_lista,zagueiros_lista,laterais_lista,meias_lista,atacantes_lista=titulares(pontos_time,pontos_goleiros,pontos_zagueiros,pontos_laterais,pontos_meias,pontos_atacantes,goleiros_lista,zagueiros_lista,laterais_lista,meias_lista,atacantes_lista)

        # agora os reservas
    elif escalacao=="reservas":

        pontos_goleiros_reservas,pontos_zagueiros_reservas,pontos_laterais_reservas,pontos_meias_reservas,pontos_atacantes_reservas,goleiros_lista_reservas,zagueiros_lista_reservas,laterais_lista_reservas,meias_lista_reservas,atacantes_lista_reservas=reservas(pontos_goleiros_reservas,pontos_zagueiros_reservas,pontos_laterais_reservas,pontos_meias_reservas,pontos_atacantes_reservas,goleiros_lista_reservas,zagueiros_lista_reservas,laterais_lista_reservas,meias_lista_reservas,atacantes_lista_reservas)
        
        if not titulares:
            escalacao=input()
        
            

                        