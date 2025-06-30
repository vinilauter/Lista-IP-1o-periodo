ataque=0
defesa=0

#variáveis de atributos

errou=0

#variaveis da contagem do output

relatorio=""

#variável do relatório

bolas=int(input())

while bolas!=0:
    tipo=input()
    golpe=input()
    if golpe=="Topspin":
        ataque+=5
    elif golpe=="Smash":
        ataque+=10
    elif golpe=="Push":
        defesa+=5
    elif golpe=="Chop":
        defesa+=10
    if tipo=="Defesa" and golpe=="Errou":
        defesa-=10
    if tipo=="Ataque" and golpe=="Errou":
        ataque-=10
    if golpe!="Errou":
        relatorio+=f"Você conseguiu rebater uma bola de {tipo}! Golpe executado: {golpe}.\n"
    elif golpe=="Errou":
        relatorio+="Você errou! Levanta a cabeça que ainda tem mais.\n"
        errou+=1
    bolas-=1

#loop dos golpes 

if ataque<0:
    ataque=0
if defesa<0:
    defesa=0

#condicionais para não negativar nenhum atributo

print("------- Início do Treino -------")
if ataque>defesa:
    relatorio+=("Ter um bom jogo ofensivo será fundamental para ganhar o InterCin!")
elif defesa>ataque:
    relatorio+=("Defesa ganha campeonatos! Agora sim estou preparado.")
else:
    relatorio+=("Foi um treino equilibrado.")
print(relatorio)
if errou>0:
    print("Infelizmente não foi um treino perfeito, mas pude melhorar muito.")
print("------- Atributos -------")
print(f"Ataque: {ataque}")
print(f"Defesa: {defesa}")

#relatório