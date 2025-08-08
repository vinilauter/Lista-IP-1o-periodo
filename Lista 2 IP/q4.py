F_max=int(input())
forca_inicial=int(input())
nivel=input()
forca_media_jogador=int(input())
tempo=0
n=0

#inputs

print("Robô Hugo 4.0 foi inicializado…")
if nivel=="facil":
    incremento=1
    print("Iniciando no modo iniciante... Ótimo para aquecer os motores!")
elif nivel=="medio":
    incremento=3
    print("Você escolheu o modo intermediário. Hora de mostrar técnica e estratégia!")
else:
    incremento=5
    print("Modo lendário ativado! Hugo 4.0 está a todo vapor — prepare-se para o combate definitivo!")

#prints de inicialização e dificuldade

forca_total=0
F_rebatida=0

#Variáveis de força

while forca_total<=F_max and F_rebatida<=150:
    tempo+=1
    n+=1
    F_rebatida=forca_inicial+(tempo*incremento)
    if F_rebatida<=150:
        forca_total+=F_rebatida
        print(f"Rebatida {n}: força = {F_rebatida}, força acumulada = {forca_total}")
    forca_media_robo=forca_total//tempo

#laço da partida

if forca_total>F_max:
    print("Energia do robô esgotada! Encerrando o confronto…")
if F_rebatida>=150:
    print("Bola fora! A força da rebatida excedeu os limites da mesa.")
print("Partida finalizada! Estas são as estatísticas do embate:")
print(f"O robô realizou {n} rebatidas em {tempo} segundos, com força total de {forca_total}.")
print(f"Força média do robô: {forca_media_robo}")
print(f"Força média do jogador: {forca_media_jogador}")
if forca_media_robo>forca_media_jogador:
    print("Vitória do Hugo 4.0! O robô mostrou quem manda na quadra!")
elif forca_media_robo<forca_media_jogador:
    print("Vitória do jogador! O talento humano ainda é imbatível!")
else:
    print("Empate técnico! Um duelo digno de mestres do tênis de mesa.")