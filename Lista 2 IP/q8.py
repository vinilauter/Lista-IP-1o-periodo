acao=""
p1=input()
p2=input()
sets=int(input())
cont_sets=sets
nivel=input()

if nivel=="aprendizes":
    rebatidas_max=1
elif nivel=="básicos":
    rebatidas_max=2
else:
    rebatidas_max=3
sacador=p1
oponente=p2
pts_p1=0
pts_p2=0
saque=""
rebatidas=0
sets_p1=0
sets_p2=0

#variáveis iniciais

sets=1
if (p1=="Luis" or p1=="Lavoisier" or p1=="Joab" or p1=="Renan") and (p2=="Luis" or p2=="Lavoisier" or p2=="Joab" or p2=="Renan"):
        print("Essa partida vai ser épica! O jogo vai ser emocionante!")
print(f"Iniciando o {sets}º set")
while cont_sets>0:
    rebatidas=0
    acao=input()
    if acao=="saque":
        print(f"O saque é de {sacador}")
        entrada1=input()
        entrada2=input()
        if entrada1=="REDE" or entrada2=="REDE":
            print("Vish, ainda bateu na rede")
            if sacador==p1:
                pts_p2+=1
                sacador=p2
                oponente=p1
            else:
                pts_p1+=1
                sacador=p1
                oponente=p2
        elif entrada1=="SA" and entrada2=="AO":
            print("Um saque PERFEITO!!")
            saque="válido"
        elif entrada1=="AO" and entrada2=="AO":
            print(f"Boa, {sacador}! Deu ponto de graça pro oponente!! Agora quem saca é {oponente}")
            if sacador==p1:
                pts_p2+=1
                sacador=p2
                oponente=p1
            else:
                pts_p1+=1
                sacador=p1
                oponente=p2
        elif entrada1=="SA" and entrada2=="SA":
            print(f"{sacador}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??")
            if sacador==p1:
                pts_p2+=1
                sacador=p2
                oponente=p1
            else:
                pts_p1+=1
                sacador=p1
                oponente=p2
    while saque=="válido" and rebatidas<=rebatidas_max:
        entrada_acao=input()
        if entrada_acao=="oponente rebateu":
            rebatidas+=1
            if rebatidas==rebatidas_max:
                velocidade_p1=int(input())
                velocidade_p2=int(input())
                if velocidade_p1<velocidade_p2:
                    pts_p1+=1
                    saque="inválido"
                    sacador=p1
                    oponente=p2
                    rebatidas=0
                else:
                    pts_p2+=1
                    saque="inválido"
                    sacador=p2
                    oponente=p1
                    rebatidas=0
        elif entrada_acao==(f"{p2} deixou a bola cair"):
            sacador=p1
            oponente=p2
            pts_p1+=1
            saque="inválido"
        elif entrada_acao==(f"{p1} deixou a bola cair"):
            sacador=p2
            oponente=p1
            pts_p2+=1
            saque="inválido"
    if (pts_p1>=3 or pts_p2>=3) and abs(pts_p1-pts_p2)>=2:
        sets+=1
        cont_sets-=1
        if pts_p1>=3 and (pts_p1-pts_p2)>=2:
            sets_p1+=1
        else:
            sets_p2+=1
        if cont_sets>0:
            pts_p1=0
            pts_p2=0
            print(f"Iniciando o {sets}º set")
            sacador=p1
            oponente=p2

#laço da partida

if sets_p1>sets_p2:
    vencedor=p1
else:
    vencedor=p2
print(f"Depois de {sets-1} set(s) vibrante(s), o grande vencedor é {vencedor}!!\nFim do jogo!")
    
