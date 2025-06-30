print("A partida de revanche de Hugo Calderano contra a China, Potência Mundial do Tênis de Mesa, está prestes a começar!")
nacionalidade_atleta=input()
nome_atleta=input()
while nacionalidade_atleta!="Chinês":
    print(f"O {nome_atleta} não poderá disputar a partida, pois sua nacionalidade não é chinesa!")
    nacionalidade_atleta=input()
    nome_atleta=input()
print(f"{nome_atleta} foi convocado para vingar o massacre feito durante o mundial de Tênis de Mesa!")

#input da nacionalidade e nome do adversário

pts_hugo=0
pts_adv=0

#variáveis dos pontos

while abs(pts_hugo-pts_adv)<3:
    nmr_adv=int(input())
    nmr_hugo=int(input())
    if nmr_adv/nmr_hugo>=2:
        print("Que bela jogada, essa merece ponto extra!")
        pts_adv+=2
    elif nmr_hugo/nmr_adv>=2:
        print("Que bela jogada, essa merece ponto extra!")
        pts_hugo+=2
    elif nmr_hugo>nmr_adv:
        print("Hugo Calderano marcou um ponto de maneira esplendida!")
        pts_hugo+=1
    elif nmr_adv>nmr_hugo:
        print("Vamos Hugo, não deixe ele vencer!")
        pts_adv+=1
    elif nmr_hugo==nmr_adv:
        print("A bola bateu na rede e felizmente caiu no lado adversário!!! Hugo marca mais um ponto!")
        pts_hugo+=1

#laço da partida

if pts_hugo==3:
    print("Hugo Calderano mostrou o porquê ele é o atual campeão mundial, uma partida relâmpago!")
elif pts_hugo>3 and pts_hugo<=10:
    print("Não demorou muito, mas o resultado era esperado, Hugo Calderano vence!")
elif pts_hugo>10:
    print("Demorou, mas o previsto aconteceu! Hugo Calderano não deixa dúvidas do porquê ele é o Campeão Mundial!")
print(f"Placar Final: {pts_hugo}x{pts_adv}")
print()

#resultado da partida

print("Aqui está o merecido prêmio de Hugo Calderano:")
if pts_adv<=2:
    pts_adv=3
elif pts_adv%2==0:
    pts_adv-=1
for i in range(pts_hugo-1):
    print("-", end="")
print("-")
for i in range((pts_adv//4)):
    print("|",end="")
    for i in range (pts_hugo-2):
        print(" ",end="")
    print("|")
print("|",end="")
for i in range(pts_hugo-2):
    print("#", end="")
print("|")
for i in range((pts_adv//4)):
    print("|",end="")
    for i in range (pts_hugo-2):
        print(" ",end="")
    print("|")
for i in range(pts_hugo):
    print("-", end="")
    