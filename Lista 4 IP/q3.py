#print inicial

print("A saga de Vegeta começa!\n")

#controle da derrota

derrota=False

#função do dano

def dano(tipo_golpe, motivacao):
    dano_base=0
    if tipo_golpe=="Normal":
        dano_base=20
    elif tipo_golpe=="Potente":
        dano_base=40
    return int(dano_base*motivacao)

#função do bônus de motivação

def bonus(motivacao_vegeta, vida_inicial_oponente, vida_vegeta):
    motivacao_bonificada=motivacao_vegeta*(1+vida_vegeta/vida_inicial_oponente)
    return motivacao_bonificada

#função da batalha

def batalha(motivacao_vegeta,vida_vegeta,motivacao_oponente,nome_oponente,vida_inicial_oponente):
    print(f"--- Iniciando o combate contra {nome_oponente} ---\n")
    vida_oponente_atual=vida_inicial_oponente
    vida_vegeta_atual=vida_vegeta
    turno=1
    ultimo_golpe_vegeta=""
    while vida_vegeta_atual>0 and vida_oponente_atual>0:
            print(f"--- Turno {turno} ---")
            golpe_vegeta=input()
            if golpe_vegeta=="Potente" and ultimo_golpe_vegeta=="Potente":
                print("Vegeta usou dois Golpes Potentes seguidos e desmaiou com o esforço!")
                vida_vegeta_atual=0
            else:
                dano_causado_por_vegeta=dano(tipo_golpe=golpe_vegeta,motivacao=motivacao_vegeta)
                vida_oponente_atual-=dano_causado_por_vegeta
                print(f"Vegeta usou Golpe {golpe_vegeta} e causou {round(dano_causado_por_vegeta)} de dano!")
            ultimo_golpe_vegeta=golpe_vegeta
            if vida_oponente_atual>0 and vida_vegeta_atual>0:
                golpe_oponente=input()
                dano_causado_por_oponente=dano(tipo_golpe=golpe_oponente,motivacao=motivacao_oponente)
                vida_vegeta_atual-=dano_causado_por_oponente
                print(f"{nome_oponente} usou Golpe {golpe_oponente} e causou {round(dano_causado_por_oponente)} de dano!")
            vida_vegeta_display=round(max(0,vida_vegeta_atual))
            vida_oponente_display=round(max(0,vida_oponente_atual))
            print(f"|Vegeta: {vida_vegeta_display} HP vs {nome_oponente}: {vida_oponente_display} HP|\n")
            turno+=1
    return vida_vegeta_atual

#programa principal

#Piccolo

vida_vegeta=100
motivacao_vegeta=float(input())
vida_vegeta_atual=batalha(motivacao_vegeta,vida_vegeta,motivacao_oponente=float(input()),nome_oponente="Piccolo",vida_inicial_oponente=100)

#Gohan

if vida_vegeta_atual>0:
    print("Vitória de Vegeta!")
    print(f"Vegeta venceu a batalha contra Piccolo com {round(vida_vegeta_atual)} HP restantes!\n")
    motivacao_vegeta_bonificada=bonus(motivacao_vegeta,vida_inicial_oponente=100,vida_vegeta=vida_vegeta_atual)
    vida_vegeta_atual=batalha(motivacao_vegeta=motivacao_vegeta_bonificada,motivacao_oponente=float(input()),nome_oponente="Gohan",vida_inicial_oponente=100, vida_vegeta=100)
else:
    derrota=True
    print("Vegeta foi derrotado! A Terra está a salvo graças a Piccolo!")

#Goku

if vida_vegeta_atual>0:
    print("Vitória de Vegeta!")
    print(f"Vegeta venceu a batalha contra Gohan com {round(vida_vegeta_atual)} HP restantes!\n")
    motivacao_vegeta_bonificada=bonus(motivacao_vegeta_bonificada,vida_inicial_oponente=100,vida_vegeta=vida_vegeta_atual)
    vida_vegeta_atual=batalha(motivacao_vegeta=motivacao_vegeta_bonificada,motivacao_oponente=float(input()),nome_oponente="Goku",vida_inicial_oponente=200, vida_vegeta=100)
elif not derrota:
        derrota=True
        print("Vegeta foi derrotado! A Terra está a salvo graças a Gohan!")

#print da vitória de todas as batalhas ou a derrota na final

if vida_vegeta_atual>0:
    print("Vitória de Vegeta!")
    print(f"Vegeta venceu a batalha contra Goku com {round(vida_vegeta_atual)} HP restantes!\n")
    print("Vegeta derrotou todos os Guerreiros Z! A Terra foi conquistada!")
elif not derrota:
        print("Vegeta foi derrotado! A Terra está a salvo graças a Goku!")