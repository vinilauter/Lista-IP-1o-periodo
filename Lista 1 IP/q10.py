
cidade1=input()
adversario1=input()
resultado1=input()
if resultado1=="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
    expressao_str=input()
    a,b,c=expressao_str
    n1=int(a)
    operador=(b)
    n2=int(c)
    if operador == '+':
        expressao = (n1 + n2)
    elif operador == '-':
        expressao = (n1 - n2)
    elif operador == '*':
        expressao = (n1 * n2)
    elif operador == '/':
        expressao = (n1 / n2)
#inputs 1
if resultado1!="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
    cidade2=input()
    adversario2=input()
    resultado2=input()
    if resultado2=="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
        expressao_str=input()
        a,b,c=expressao_str
        n1=int(a)
        operador=(b)
        n2=int(c)
        if operador == '+':
            expressao = (n1 + n2)
        elif operador == '-':
            expressao = (n1 - n2)
        elif operador == '*':
            expressao = (n1 * n2)
        elif operador == '/':
            expressao = (n1 / n2)
#inputs 2
cont_partidas=0
cont_win=0
cont_loose=0
cont_palmeiras="Não!!!! :D"
if resultado1=="VENCEU":
    cont_win+=1
if resultado1=="perdeu":
    cont_loose+=1
if resultado1!="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
    if resultado2=="VENCEU":
        cont_win+=1
    if resultado2=="perdeu":
        cont_loose+=1
    if resultado2=="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
        cont_palmeiras="sim :("
        cont_loose+=1
if resultado1=="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
    cont_palmeiras="sim :("
    cont_loose+=1
#contadores
print("Byte, o cachorro mais promissor do futebol nordestino, acaba de calçar suas quatro chuteiras e está pronto para entrar em campo!")
if cidade1=="Catende" or cidade1=="Tabira":
    print("É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.")
if "s" in adversario1 and "p" in adversario1 and "o" in adversario1 and "r" in adversario1 and "t" in adversario1:
    print("Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!")
if resultado1=="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
    print("Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!")
    print(f"A expressão resolvida é: {expressao:.2f}")
    print("Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!")
    cont_win+=1
    cont_loose-=1
    cont_partidas+=1
    print()
    print("RELATÓRIO DA PRÉ-TEMPORADA DO BYTE:")
    print(f"- Partidas jogadas: {cont_partidas}")
    print(f"- Vitórias: {cont_win}")
    print(f"- Derrotas: {cont_loose}")
    print(f"- Tentaram roubar o bixinho: {cont_palmeiras}")
    print(f"- Cidades visitadas: {cidade1}")
    print(f"- Adversários enfrentados: {adversario1}")
    print()
    print("E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)")    
elif resultado1!="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
    cont_partidas+=2
if resultado1=="VENCEU":
    print("TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!")
if resultado1=="perdeu":
    print("Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...")
#possibilidades do primeiro jogo
if resultado1!="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
    if cidade2=="Catende" or cidade2=="Tabira":
        print("É... mesmo com o Santa embalado, jogar em Catende ou Tabira é pedir pra sofrer. Byte, meu filho, você realmente tá no fundo do poço.")
    if (cidade1=="Catende" or cidade1=="Tabira") and (cidade2=="Catende" or cidade2=="Tabira"):
        print("Não dá mais! Jogar nessas duas cidades é sinal de que o Santa Cruz precisa mais de magia do que de reforços...")
    if "s" in adversario2 and "p" in adversario2 and "o" in adversario2 and "r" in adversario2 and "t" in adversario2:
        print("Alerta máximo! O adversário é o inimigo histórico, o Voldemort do futebol pernambucano... aquele cujo nome não deve ser pronunciado!")
    if resultado2=="Torcedores do Sport, disfarçados de lanterna, estão tentando sequestrar o Byte no meio da partida!":
        print("Urgente! Sequestradores estão tentando raptar nosso craque peludo! A única saída é resolver uma equação... Isso mesmo, agora isso aqui virou ENEM!")
        print(f"A expressão resolvida é: {expressao:.2f}")
        print("Chega! Vou voltar pra casa e passar o resto das férias no sofá, assistindo o RobôCIn na RoboCup. Futebol de verdade, sem sequestro!")
        cont_win+=1
        cont_loose-=1
    if resultado2=="VENCEU":
        print("TRI-COO-LOOOOR!!! Byte mostrou que tem faro de artilheiro e garantiu mais uma vitória do Santinha!")
    if resultado2=="perdeu":
        print("Dessa vez não deu... Até o Galhardo canino tem seus dias de luta...")
    print()
    print("RELATÓRIO DA PRÉ-TEMPORADA DO BYTE:")
    print(f"- Partidas jogadas: {cont_partidas}")
    print(f"- Vitórias: {cont_win}")
    print(f"- Derrotas: {cont_loose}")
    print(f"- Tentaram roubar o bixinho: {cont_palmeiras}")
    print(f"- Cidades visitadas: {cidade1} e {cidade2}")
    print(f"- Adversários enfrentados: {adversario1} e {adversario2}")
    print()
    print("E assim termina a pré-temporada do Byte pelos gramados. Anotar tudo isso na mão dá uma trabalheira! Nas próximas férias o Byte deve esperar saber laços, listas, funções e muito mais pra registrar tudo com mais facilidade :)")    
