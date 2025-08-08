#função da fusão

def fusao(nome1,nome2,herois,viloes):
    #variáveis iniciais

    nome_fusao=""
    parte1=""
    parte2=""

    #prints das mensagens iniciais

    print(f"{nome1} se elege para participar da fusão!")
    print(f"{nome2} se elege para participar da fusão!")

    #listas das vogais e consoantes

    vogais=['a','e','i','o','u']
    
    consoantes=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']

    #critérios de elegibilidade

    elegivel=True

    if nome1 not in viloes and nome1 not in herois:
        print(f"{nome1} já participou de uma fusão. Fusão inválida.")
        elegivel=False
    if nome2 not in viloes and nome2 not in herois:
        print(f"{nome2} já participou de uma fusão. Fusão inválida.")
        elegivel=False
    elif nome1 in herois and nome2 in viloes:
        elegivel=False
        print("Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.")
    elif nome1 in viloes and nome2 in herois:
        elegivel=False
        print("Heróis e vilões não se misturam! As auras dos dois participantes são incompatíveis.")
    
    #se elegível, realização da fusão

    if elegivel:
        if len(nome1)<=4:
            parte1=nome1[0]
        else:
            indice=(len(nome1)+1)//2
            parte1=nome1[:indice]
        if len(nome2)<=4:
            if len(nome2)==3:
                parte2=nome2[-2:]
            else:
                parte2=nome2[-3:]
        else:
            indice2=((len(nome2)+1)//2)-1
            parte2=nome2[-indice2:]
        nome_fusao=parte1+parte2
        if ("Goku" in nome1 or "Goku" in nome2) and ("Vegeta" in nome1 or "Vegeta" in nome2):
            nome_fusao="Vegito"
            print(f"Fusão realizada com sucesso! {nome_fusao} entra em combate para derrotar o exército de vilões!")
            herois.remove(nome1)
            herois.remove(nome2)
        elif ("Goten" in nome1 or "Goten" in nome2) and ("Trunks" in nome1 or "Trunks" in nome2):
            nome_fusao="Gotenks"
            print(f"Fusão realizada com sucesso! {nome_fusao} entra em combate para derrotar o exército de vilões!")
            herois.remove(nome1)
            herois.remove(nome2)
        elif len(nome_fusao)<=3 or (parte1[-1].lower() in vogais and parte2[0].lower() in vogais) or (parte1[-1].lower() in consoantes and parte2[0].lower() in consoantes):
            print(f"A sincronização foi um desastre... {nome_fusao} é uma fusão imperfeita!")
            if len(nome1)<=4:
                parte1=nome1[:2]
            else:
                indice=(len(nome1)+1)//2
                parte1=nome1[:indice+1]
            nome_fusao=parte1+parte2
            if len(nome_fusao)<=3 or (parte1[-1].lower() in vogais and parte2[0].lower() in vogais) or (parte1[-1].lower() in consoantes and parte2[0].lower() in consoantes):
                print(f"A sincronização foi um desastre... {nome_fusao} é uma fusão imperfeita!")
                if len(nome1)<=4:
                    parte1=nome1[:2]
                else:
                    indice=(len(nome1)+1)//2
                    parte1=nome1[:indice]
                if len(nome2)<=4:
                    parte2_maiuscula=nome2[-3:]
                    parte2=parte2_maiuscula.lower()
                else:
                    indice2=((len(nome2)+1)//2)
                    parte2=nome2[indice2:]
                nome_fusao=parte1+parte2
                if len(nome_fusao)<=3 or (parte1[-1].lower() in vogais and parte2[0].lower() in vogais) or (parte1[-1].lower() in consoantes and parte2[0].lower() in consoantes):
                    print(f"A sincronização foi um desastre... {nome_fusao} é uma fusão imperfeita!")
                    print("Aparentemente essa combinação é incompatível...")
                    nome_fusao=""
                else:
                    if nome1 in herois:
                        print(f"Fusão realizada com sucesso! {nome_fusao} entra em combate para derrotar o exército de vilões!")
                        herois.remove(nome1)
                        herois.remove(nome2)
                    elif nome1 in viloes:
                        print(f"Fusão realizada com sucesso! {nome_fusao} entra em combate com sede de destruir Satan City!")
                    viloes.remove(nome1)
                    viloes.remove(nome2)
            elif nome1 in herois:
                print(f"Fusão realizada com sucesso! {nome_fusao} entra em combate para derrotar o exército de vilões!")
                herois.remove(nome1)
                herois.remove(nome2)
            elif nome1 in viloes:
                print(f"Fusão realizada com sucesso! {nome_fusao} entra em combate com sede de destruir Satan City!")
                viloes.remove(nome1)
                viloes.remove(nome2)
        elif nome1 in herois:
                print(f"Fusão realizada com sucesso! {nome_fusao} entra em combate para derrotar o exército de vilões!")
                herois.remove(nome1)
                herois.remove(nome2)
        elif nome1 in viloes:
                print(f"Fusão realizada com sucesso! {nome_fusao} entra em combate com sede de destruir Satan City!")
                viloes.remove(nome1)
                viloes.remove(nome2)
    return nome_fusao

#lista de combatentes

herois=['Gohan','Goku','Goten','Kuririn','Piccolo','Tenshinhan','Trunks','Uub','Vegeta','Yamcha']

viloes=['Babidi','Baby','Broly','Buu','Cell','Cooler','Frieza','Hit','Janemba','Zamasu']

#função do incremento

def incremento(nome_fusao,nome1,poder_viloes,poder_herois):
    tamanho_fusao=len(nome_fusao)
    if nome1 in herois_loop:
        if tamanho_fusao==4:
            poder_herois+=2000
        elif tamanho_fusao==5:
            poder_herois+=2250
        elif tamanho_fusao==6:
            poder_herois+=2500
        elif tamanho_fusao==7:
            poder_herois+=2750
        elif tamanho_fusao>=8:
            poder_herois+=3000
    elif nome1 in viloes_loop:
        if tamanho_fusao==4:
            poder_viloes+=2000
        elif tamanho_fusao==5:
            poder_viloes+=2250
        elif tamanho_fusao==6:
            poder_viloes+=2500
        elif tamanho_fusao==7:
            poder_viloes+=2750
        elif tamanho_fusao>=8:
            poder_viloes+=3000
    return poder_viloes,poder_herois

#programa principal

poder_viloes=0
poder_herois=0

while poder_herois<=8000 and poder_viloes<=8000:

    #inputs e fusão

    nome1=input()
    nome2=input()
    nome_fusao=fusao(nome1,nome2,herois,viloes)

    #listas dos combatentes

    herois_loop=['Gohan','Goku','Goten','Kuririn','Piccolo','Tenshinhan','Trunks','Uub','Vegeta','Yamcha']

    viloes_loop=['Babidi','Baby','Broly','Buu','Cell','Cooler','Frieza','Hit','Janemba','Zamasu']

    #incremento de poder

    if nome_fusao!="":
        poder_viloes,poder_herois=incremento(nome_fusao,nome1,poder_viloes,poder_herois)

#outputs finais

if poder_herois>8000:
    print("O poder dos heróis... É mais de 8000! Eles derrotam os vilões e conseguem selar o portal.")
elif poder_viloes>8000:
    print("Os vilões são fortes demais! Satan City está em apuros!")