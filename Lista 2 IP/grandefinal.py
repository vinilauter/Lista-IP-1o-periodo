print("Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!")
sets_hugo=0
sets_lin=0
sets=1
sacador1=input()
if sacador1=="hugo":
    sacador2="lin"
else:
    sacador2="hugo"
jogador_atual=sacador1
anuncio_vai_a_2=False
set_em_andamento=True

#variáveis e print inicial

while (sets_hugo<=3 or sets_lin<=3) and abs(sets_hugo-sets_lin)<=2 and (sets_hugo+sets_lin)<4: #laço dos sets normais
    print(f"Set {sets}:")
    set_em_andamento=True
    pts_hugo=0
    pts_lin=0
    i=0
    acao=""
    acao_ant=""
    anuncio_vai_a_2=False
    while set_em_andamento:
        sequencia=input()
        if sets%2==0 and (sets_hugo+sets_lin<4):
            jogador_atual=sacador2
        elif sets%2==1 and (sets_hugo+sets_lin<4):
            jogador_atual=sacador1
        for letra in sequencia:
            if letra!="-":
                acao+=letra
            else:
                if acao_ant=="ataque" and acao=="defesa":
                    if jogador_atual=="hugo":
                        jogador_atual="lin"
                    else:
                        jogador_atual="hugo"
                elif acao_ant=="controle" and (acao=="defesa" or acao=="ataque" or acao=="controle"):
                    if jogador_atual=="hugo":
                        jogador_atual="lin"
                    else:
                        jogador_atual="hugo"
                elif acao_ant=="saque" and (acao=="defesa" or acao=="controle"):
                    if jogador_atual=="hugo":
                        jogador_atual="lin"
                    else:
                        jogador_atual="hugo"
                elif acao_ant=="defesa" and (acao=="controle" or acao=="ataque"):
                    if jogador_atual=="hugo":
                        jogador_atual="lin"
                    else:
                        jogador_atual="hugo"
                acao_ant=acao
                acao=""
                if (pts_hugo>=4 and pts_lin>=4) and anuncio_vai_a_2==False:
                    print("O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!")
                    anuncio_vai_a_2=True 
            i+=1
        if acao != "":
            if acao_ant=="saque" and (acao=="ataque" or acao=="erro"):
                if jogador_atual=="hugo":
                    pts_hugo+=1
                    print(f"Uau, um ace! Hugo solta o braço e deixa o adversário parado!")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_lin+=1
                    print(f"Uau, um ace! Lin solta o braço e deixa o adversário parado!")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao=="erro" and acao_ant!="controle" and acao_ant!="" and acao_ant!="erro" and acao_ant!="saque":
                if jogador_atual=="hugo":
                    pts_hugo+=1
                    print(f"Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_lin+=1
                    print(f"Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao=="erro" and acao_ant=="erro":
                if jogador_atual=="lin":
                    pts_hugo+=1
                    print(f"Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_lin+=1
                    print(f"Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao=="erro" and acao_ant=="controle":
                if jogador_atual=="lin":
                    pts_lin+=1
                    print(f"Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_hugo+=1
                    print(f"Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao=="erro" and acao_ant=="":
                if jogador_atual=="hugo":
                    pts_lin+=1
                    print(f"Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_hugo+=1
                    print(f"Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao_ant=="ataque" and acao=="ataque":
                if jogador_atual=="lin":
                    pts_lin+=1
                    print(f"Lin acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_hugo+=1
                    print(f"Hugo acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao_ant=="ataque" and acao=="controle":
                if jogador_atual=="lin":
                    pts_lin+=1
                    print(f"Lin acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_hugo+=1
                    print(f"Hugo acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao_ant=="defesa" and acao=="defesa":
                if jogador_atual=="hugo":
                    pts_hugo+=1
                    print(f"Lin tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_lin+=1
                    print(f"Hugo tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            acao_ant = acao  
            acao = "" 
            i=0
        if (pts_hugo>=5 or pts_lin>=5) and abs(pts_hugo-pts_lin)>=2:
            if pts_hugo>pts_lin:
                if pts_hugo-pts_lin==5:
                    print ("Fim de set! Domínio total: 5 a 0, sem chance para o adversário — Hugo passeia na mesa")
                else:
                    print("E o set vai para Hugo!")
                sets_hugo+=1
                sets+=1
                print(f"Placar do jogo: {sets_hugo} x {sets_lin}")
                pts_hugo=0
                pts_lin=0
                set_em_andamento=False 
            elif pts_lin>pts_hugo:
                if pts_lin-pts_hugo==5:
                    print ("Fim de set! Domínio total: 5 a 0, sem chance para o adversário — Lin passeia na mesa")
                else:
                    print("E o set vai para Lin!")
                sets_lin+=1
                sets+=1
                print(f"Placar do jogo: {sets_hugo} x {sets_lin}")
                pts_hugo=0
                pts_lin=0
                set_em_andamento=False

anuncio_vai_a_2=False

if sets_hugo==2 and sets_lin==2: #condição do tie-break
    print(f"Set {sets}:")
    print("Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!")
    set_em_andamento=True
    acao=""
    acao_ant=""
    while set_em_andamento: #laço do tie break
        sequencia=input()
        i=0
        if (pts_lin+pts_hugo)==0:
            sacador_atual=sacador1
            jogador_atual=sacador1
        elif (pts_lin+pts_hugo)==1:
            sacador_atual=sacador2
            jogador_atual=sacador2
        elif (pts_lin+pts_hugo)==2 or (pts_lin+pts_hugo)==6 or (pts_lin+pts_hugo)==10:
            sacador_atual=sacador2
            jogador_atual=sacador2
        elif (pts_hugo+pts_lin)%2==1:
            if sacador_atual==sacador1:
                sacador_atual=sacador2
                jogador_atual=sacador2
            else:
                sacador_atual=sacador1
                jogador_atual=sacador1
        elif (pts_hugo+pts_lin)%2==0:
            if sacador_atual!=jogador_atual:
                jogador_atual=sacador_atual
        for letra in sequencia:
            if letra!="-":
                    acao+=letra
            else:
                if jogador_atual=="hugo":
                    jogador_atual="lin"
                else:
                    jogador_atual="hugo"
                acao_ant=acao
                acao=""
                if (pts_hugo>=6 and pts_lin>=6) and anuncio_vai_a_2==False:
                    print("O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?")
                    anuncio_vai_a_2=True 
            i+=1
        if acao != "":
            if acao_ant=="saque" and (acao=="ataque" or acao=="erro"):
                if jogador_atual=="lin":
                    pts_hugo+=1
                    print(f"Uau, um ace! Hugo solta o braço e deixa o adversário parado!")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_lin+=1
                    print(f"Uau, um ace! Lin solta o braço e deixa o adversário parado!")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao=="erro" and acao_ant!="controle" and acao_ant!="" and acao_ant!="erro" and acao_ant!="saque":
                if jogador_atual=="lin":
                    pts_hugo+=1
                    print(f"Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_lin+=1
                    print(f"Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao=="erro" and acao_ant=="erro":
                if jogador_atual=="lin":
                    pts_hugo+=1
                    print(f"Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_lin+=1
                    print(f"Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao=="erro" and acao_ant=="controle":
                if jogador_atual=="hugo":
                    pts_lin+=1
                    print(f"Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_hugo+=1
                    print(f"Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao=="erro" and acao_ant=="":
                if jogador_atual=="hugo":
                    pts_lin+=1
                    print(f"Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_hugo+=1
                    print(f"Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao_ant=="ataque" and acao=="ataque":
                if jogador_atual=="hugo":
                    pts_lin+=1
                    print(f"Lin acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_hugo+=1
                    print(f"Hugo acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao_ant=="ataque" and acao=="controle":
                if jogador_atual=="hugo":
                    pts_lin+=1
                    print(f"Lin acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_hugo+=1
                    print(f"Hugo acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            elif acao_ant=="defesa" and acao=="defesa":
                if jogador_atual=="lin":
                    pts_hugo+=1
                    print(f"Lin tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.")
                    print(f"Ponto para Hugo!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
                else:
                    pts_lin+=1
                    print(f"Hugo tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.")
                    print(f"Ponto para Lin!")
                    print(f"Placar do {sets} set : {pts_hugo} x {pts_lin}")
            acao_ant = acao  
            acao = "" 
            i=0
        if (pts_hugo>=7 or pts_lin>=7) and abs(pts_hugo-pts_lin)>=2:
            if pts_hugo>pts_lin:
                if pts_hugo-pts_lin==7:
                    print ("Fim de tie-break! Hugo arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!")
                else:
                    print("E o set vai para Hugo!")
                sets_hugo+=1
                sets+=1
                print(f"Placar do jogo: {sets_hugo} x {sets_lin}")
                set_em_andamento=False
            elif pts_lin>pts_hugo:
                if pts_lin-pts_hugo==7:
                    print ("Fim de tie-break! Lin arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!")
                else:
                    print("E o set vai para Lin!")
                sets_lin+=1
                sets+=1
                print(f"Placar do jogo: {sets_hugo} x {sets_lin}")
                set_em_andamento=False

#laço da partida

if sets_hugo>=3 and sets_lin<2:
    print("Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!")
elif sets_hugo>sets_lin and sets_lin==2:
    print("Hugo é o grande vencedor! Ele conquista o tie-break com uma performance impecável e leva a vitória!")
elif sets_hugo<sets_lin and sets_hugo==2:
    print("Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!")
elif sets_lin>=3 and sets_hugo<2:
    print("Hugo não conseguiu segurar a pressão e acabou perdendo sem precisar do tie-break. Foi uma grande final, mas hoje não foi o seu dia. Vitória do chinês!")

#prints finais