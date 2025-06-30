uniformes=0
isotonicos=0
raquetes=0
toalhas=0
sabotagem="False"
entrada=""

#contadores

while entrada!="FIM":
    entrada=input()
    if entrada=="Uniforme":
        uniformes+=1
        print(f"Tava faltando camisa! Agora temos {uniformes} uniforme(s)")
    elif entrada=="Isotônico":
        isotonicos+=1
        print(f"Bora garantir a hidratação! Agora temos {isotonicos} isotônico(s)")
    elif entrada=="Raquete":
        raquetes+=1
        print(f"Mais uma raquete saindo! Agora temos {raquetes} raquete(s)")
    elif entrada=="Toalha":
        toalhas+=1
        print(f"Mais uma toalha saindo! Agora temos {toalhas} toalha(s)")
    elif entrada=="Sabotagem":
        sabotagem="True"
        item_sabotado=input()
        if item_sabotado=="Uniforme":
            uniformes-=1
            print("O sueco está roubando as camisas de Hugo!")
        elif item_sabotado=="Isotônico":
            isotonicos-=1
            print("O sueco está sabotando a hidratação de Hugo!")
        elif item_sabotado=="Raquete":
            raquetes-=1
            print("O sueco está roubando as raquetes de Hugo!")
        elif item_sabotado=="Toalha":
            toalhas-=1
            print("O sueco está roubando as toalhas de Hugo!")

#laço dos materiais

if uniformes<0:
    uniformes=0
if isotonicos<0:
    isotonicos=0
if raquetes<0:
    raquetes=0
if toalhas<0:
    toalhas=0

#zeradores

print("Bora ver o relatório final dos materiais!")
print(f"Uniforme: {uniformes} unidade(s).")
print(f"Isotônico: {isotonicos} unidade(s).")
print(f"Raquete: {raquetes} unidade(s).")
print(f"Toalha: {toalhas} unidade(s).")
if uniformes+isotonicos+raquetes+toalhas==0 and sabotagem=="True":
    print("Droga... Truls Möregårdh conseguiu sabotar os materiais completamente!")
elif uniformes+isotonicos+raquetes+toalhas==0 and sabotagem=="False":
    print("Vish... Parece que vão faltar materiais para garantir a vitória do nosso atleta.")
elif uniformes+isotonicos+raquetes+toalhas>0 and (uniformes==0 or isotonicos==0 or raquetes==0 or toalhas==0):
    print("Ta faltando algumas coisas, mas para Hugo Calderano tudo é possível!!!")
else: 
    print("Tudo pronto! Não vai faltar nada para mais um título de Hugo Calderano!")

#outputs 

