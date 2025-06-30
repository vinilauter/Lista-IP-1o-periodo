nmr_rodadas=int(input())
vencedor_tomada=input()
nome_monitor=vencedor_tomada
n=1
pts_luv=0
pts_jaob=0

#variáveis iniciais

print("Vamos dar início à disputa!!! TOMADA!!!")
if vencedor_tomada=="Jaob":
    print("Jaob veio de Catende e está pronto para vencer!!!")
else:
    print("Nada se cria, tudo se transforma, então Luvusier irá se transformar em um vencedor!!!")
print(f"COMEÇA A {n}ª RODADA!")

#prints iniciais

while nmr_rodadas>0:
    objeto_acertado=input()
    if objeto_acertado!="mesa":
        n+=1
        print(f"{nome_monitor} jogou a bolinha no(a) {objeto_acertado}!")
        if objeto_acertado=="Baralho de UNO" and nome_monitor=="Jaob":
            pts_jaob+=2
            print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pts_jaob} pontos.")
        elif objeto_acertado=="Baralho de UNO" and nome_monitor=="Luvusier":
            pts_luv+=2
            print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pts_luv} pontos.")
        elif objeto_acertado=="Armário de Homero e Elena" and nome_monitor=="Jaob":
            pts_jaob+=3
            print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pts_jaob} pontos.")
        elif objeto_acertado=="Armário de Homero e Elena" and nome_monitor=="Luvusier":
            pts_luv+=3
            print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pts_luv} pontos.")
        elif objeto_acertado=="Peça de Dominó" and nome_monitor=="Jaob":
            pts_jaob+=3
            print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pts_jaob} pontos.")
        elif objeto_acertado=="Peça de Dominó" and nome_monitor=="Luvusier":
            pts_luv+=3
            print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pts_luv} pontos.")
        elif objeto_acertado=="Baralho de Coup Desaparecido" and nome_monitor=="Jaob":
            pts_jaob+=100
            print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pts_jaob} pontos.")
            print(f"{nome_monitor} achou o Coup!!! Ele merece a vitória sem dúvidas!")
            nmr_rodadas=0
        elif objeto_acertado=="Baralho de Coup Desaparecido" and nome_monitor=="Luvusier":
            pts_luv+=100
            print(f"{nome_monitor} teve uma grande pontaria e acertou {objeto_acertado}! Agora está com {pts_luv} pontos.")
            print(f"{nome_monitor} achou o Coup!!! Ele merece a vitória sem dúvidas!")
            nmr_rodadas=0
        elif objeto_acertado=="Projetor" and nome_monitor=="Jaob":
            pts_jaob-=2
            if pts_jaob<0:
                pts_jaob=0
            print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pts_jaob} pontos.")
            nome_monitor="Luvusier"
        elif objeto_acertado=="Projetor" and nome_monitor=="Luvusier":
            pts_luv-=2
            if pts_luv<0:
                pts_luv=0
            print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pts_luv} pontos.")
            nome_monitor="Jaob"
        elif objeto_acertado=="Computador" and nome_monitor=="Jaob":
            pts_jaob-=3
            if pts_jaob<0:
                pts_jaob=0
            print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pts_jaob} pontos.")
            nome_monitor="Luvusier"
        elif objeto_acertado=="Computador" and nome_monitor=="Luvusier":
            pts_luv-=3
            if pts_luv<0:
                pts_luv=0
            print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pts_luv} pontos.")
            nome_monitor="Jaob"
        elif objeto_acertado=="Cabeça do Amiguinho" and nome_monitor=="Jaob":
            pts_jaob-=5
            if pts_jaob<0:
                pts_jaob=0
            print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pts_jaob} pontos.")
            nome_monitor="Luvusier"
        elif objeto_acertado=="Cabeça do Amiguinho" and nome_monitor=="Luvusier":
            pts_luv-=5
            if pts_luv<0:
                pts_luv=0
            print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pts_luv} pontos.")
            nome_monitor="Jaob"
        elif objeto_acertado=="Nada" and nome_monitor=="Jaob":
            pts_jaob-=1
            if pts_jaob<0:
                pts_jaob=0
            print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pts_jaob} pontos.")
            nome_monitor="Luvusier"
        elif objeto_acertado=="Nada" and nome_monitor=="Luvusier":
            pts_luv-=1
            if pts_luv<0:
                pts_luv=0
            print(f"{nome_monitor} teve mãos de alface e acertou o(a) {objeto_acertado}. Agora está com {pts_luv} pontos.")
            nome_monitor="Jaob"
        nmr_rodadas-=1
        if nmr_rodadas>0:
            print(f"COMEÇA A {n}ª RODADA!")
    else:
        print(f"{nome_monitor} jogou a bolinha no(a) {objeto_acertado}!")
        if nome_monitor=="Jaob":
            nome_monitor="Luvusier"
        elif nome_monitor=="Luvusier":
            nome_monitor="Jaob"

#laço da partida

print("\nTEMOS O RESULTADO DA PARTIDA!")
if pts_jaob>pts_luv:
    print(f"Jaob deu orgulho à Catende e ganhou a disputa com {pts_jaob} pontos!")
elif pts_luv>pts_jaob:
    print(f"A química está em festa, Luvusier ganha a disputa com {pts_luv} pontos!")
else:
    print("Jaob usou a sua autoridade como monitor-chefe e ganhou a disputa mesmo com o empate!")

