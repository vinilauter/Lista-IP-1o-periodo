quantidade_atletas=int(input())
rodada=1
primeiro_lugar=""
pts_primeiro=0
segundo_lugar=""
pts_segundo=0
terceiro_lugar=""
pts_terceiro=0
i=0

#variáveis iniciais

if quantidade_atletas==1: #se houver apenas 1 atleta
    atleta=input()
    posicao=int(input())
    ranking=int(input())
    velocidade=float(input())
    print(f"Não há dúvidas... {atleta} é o culpado!")
elif quantidade_atletas==2: #se a quantidade de atletas for apenas 2
    atleta=input()
    posicao=int(input())
    ranking=int(input())
    velocidade=float(input())
    atleta2=input()
    posicao=int(input())
    ranking=int(input())
    velocidade=float(input())
    print(f"Caso encerrado: {atleta} e {atleta2} roubaram o troféu!")
else:
    for i in range(quantidade_atletas):
        n_vogais=0
        print(f"COMEÇANDO A {rodada}ª RODADA DE INVESTIGAÇÃO")
        atleta=input()
        posicao=int(input())
        ranking=int(input())
        velocidade=float(input())
        pts_atleta=0
        for i in atleta:
            letra=i
            if letra in "aeiou" or letra in "AEIOU":
                n_vogais+=1
        if n_vogais%2==0:
                pts_atleta+=10
        else:
                pts_atleta+=5

        #pontos por vogais

        if posicao>=45 and posicao<=135:
             print(f"{atleta} estava em posição estratégica para pegar o troféu... muito suspeito!")
             pts_atleta+=10
        elif posicao>=225 and posicao<=315:
             pts_atleta+=5
        else:
             pts_atleta+=2

        #pontos por posição

        if ranking<=10:
             print(f"{atleta} é um dos melhores do mundo... e também um dos principais suspeitos!")
             pts_atleta+=10
        elif ranking>=11 and ranking<=50:
             pts_atleta+=5
        else:
             pts_atleta+=2

        #pontos por ranking

        if velocidade>140:
             print(f"Alta velocidade detectada! {atleta} pode ter fugido rapidamente com o troféu!")
             pts_atleta+=10
        elif velocidade>=100 and velocidade<=140:
             pts_atleta+=5
        else:
             pts_atleta+=2
        
        #pontos por velocidade

        if not velocidade>140 and not ranking<=10 and not (posicao>=45 and posicao<=135):
             print(f"Hum, esse {atleta} sei não viu... Deve tá escondendo alguma coisa.")
        
        #print caso não se encaixe em nenhuma habilidade excepcional

        if pts_atleta>pts_primeiro:
             terceiro_lugar=segundo_lugar
             pts_terceiro=pts_segundo
             segundo_lugar=primeiro_lugar
             pts_segundo=pts_primeiro
             primeiro_lugar=atleta
             pts_primeiro=pts_atleta
        elif pts_atleta>pts_segundo:
             terceiro_lugar=segundo_lugar
             pts_terceiro=pts_segundo
             segundo_lugar=atleta
             pts_segundo=pts_atleta
        elif pts_atleta>pts_terceiro:
             terceiro_lugar=atleta
             pts_terceiro=pts_atleta
        
        #condicionais do ranking

        rodada+=1

#laço da investigação

if quantidade_atletas>2:
    print()
    print("RESULTADOS DAS INVESTIGAÇÕES:")
    print()
    print("Os 3 principais suspeitos são:")
    print(f"1. {primeiro_lugar} - {pts_primeiro} pontos")
    print(f"2. {segundo_lugar} - {pts_segundo} pontos")
    print(f"3. {terceiro_lugar} - {pts_terceiro} pontos")
    print()
    if pts_primeiro==pts_segundo:
        print(f"Que absurdo... {primeiro_lugar} e {segundo_lugar} roubaram o troféu juntos!")
    else:
        print(f"Mistério resolvido: O culpado é {primeiro_lugar}! Ele roubou o troféu de Calderano.")

#prints finais em caso de mais de 2 atletas
             


    