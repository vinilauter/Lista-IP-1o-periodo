# função do combate

def batalha(dificuldade,boss,vida,dps,dps_atual_boss,tentativas,vitalidade,msg):
    
    # definição de stats do boss a se enfrentar

    if boss=="Sif, a Grande Loba Cinzenta":
        vida_boss=3542
    elif boss=="Gwyn, Lorde das Cinzas":
        vida_boss=4185

    # batalha 

    vida,vida_boss,tentativas,msg=turnos(dps,vida,dps_atual_boss,vida_boss,boss,tentativas,msg)

    if vida<=0:
        vida=vitalidade*20
        if dificuldade=="Iniciante":
            dps_prox_tentativa=int(dps*1.05)
            dps_prox_tentativa_boss=int(dps_atual_boss*0.9)
        elif dificuldade=="Veterano":
            dps_prox_tentativa=int(dps*1.10)
            dps_prox_tentativa_boss=int(dps_atual_boss*0.8)
        elif dificuldade=="Mestre dos Souls":
            dps_prox_tentativa=int(dps*1.20)
            dps_prox_tentativa_boss=int(dps_atual_boss*0.67)
        if boss=="Gwyn, Lorde das Cinzas":
            return batalha(dificuldade, boss, vida, dps_prox_tentativa, dps_prox_tentativa_boss, tentativas, vitalidade, False)
        else:
            return batalha(dificuldade, boss, vida, dps_prox_tentativa, dps_prox_tentativa_boss, tentativas, vitalidade, msg)
            
    elif vida_boss<=0:
        print(f"Você precisou de {tentativas} tentativas para vencer o(a) {boss}!")

        if dificuldade=="Iniciante":

            if tentativas<=5:
                print("Esse iniciante teve muita sorte, no próximo boss ele vai conhecer a verdadeira DOR!!!")
            elif tentativas<=10 and tentativas>5:
                print("Até que não foi tão ruim assim, continue assim novato!")
            else:
                print("Bem vindo a Dark Souls.")

        elif dificuldade=="Veterano":

            if tentativas<=5:
                print("Você já andou por Lordran antes, não é? Impressionante.")
            elif tentativas<=10 and tentativas>5:
                print("Nada mal, guerreiro. Mas os próximos desafios não terão piedade.")
            else:
                print("Mesmo os veteranos sangram em Dark Souls...")

        elif dificuldade=="Mestre do Souls":

            if tentativas==1:
                print("Inacreditável. Um verdadeiro Mestre do Souls. Está destinado a se tornar o Dark Lord!")
            elif tentativas<=10 and tentativas>1:
                print("Seu conhecimento sobre o ciclo é profundo. Quase como se já tivesse vivido isso mil vezes...")
            else:
                print("Nem mesmo os Mestres escapam ilesos da chama...")
        
        if boss=="Sif, a Grande Loba Cinzenta":
            print("A grande loba cai com honra. No fundo dos seus olhos, havia apenas lealdade.")
        elif boss=="Gwyn, Lorde das Cinzas":
            print("A chama se apaga, e o silêncio reina em Lordran. Você derrotou o Senhor das Cinzas...")
            if tentativas==1:
                print("O ciclo foi quebrado... Você se tornou o verdadeiro Senhor das Cinzas. Um novo destino começa...")
            else:
                print("Mas o ciclo... o ciclo continua.")
        return
        
# função para os turnos cada tentativa

def turnos(dps,vida,dps_boss,vida_boss,boss,tentativas,msg):
    vida_boss-=dps
    if vida_boss>0:
        vida-=dps_boss

    if boss=="Sif, a Grande Loba Cinzenta" and vida_boss<=354 and not msg:
        msg=True
        dps_boss-=15
        print("Sif, a Grande Loba Cinzenta está gravemente ferida! Essa é sua chance, acabe com o sofrimento dela!")
    elif boss=="Gwyn, Lorde das Cinzas" and vida_boss<=2093 and not msg:
        msg=True
        dps_boss+=10

    if vida>0 and vida_boss>0:
        return turnos(dps,vida,dps_boss,vida_boss,boss,tentativas,msg)
    else:
        if vida<=0:
            tentativas+=1
            return vida,vida_boss,tentativas,msg
        elif vida_boss<=0:
            return vida,vida_boss,tentativas,msg
        
    
# programa principal

dificuldade=input()
str_forca,str_vitalidade=input().split()
forca=int(str_forca)
vitalidade=int(str_vitalidade)
boss=input()
vida=int(vitalidade*20)
dps_inicial=int(forca*5)
tentativas=1
msg=False

if boss=="Sif, a Grande Loba Cinzenta":
    print("Venha até mim guardiã do túmulo de Artorias... Vamos acabar logo com isso!")
    dps_inicial_boss=35
elif boss=="Gwyn, Lorde das Cinzas":
    print("Enfim estou de frente ao Senhor das Cinzas! Nossa batalha será lendária e ecoará em todos os cantos de Lordran!!!")
    dps_inicial_boss=55

batalha(dificuldade,boss,vida,dps_inicial,dps_inicial_boss,tentativas,vitalidade,msg)