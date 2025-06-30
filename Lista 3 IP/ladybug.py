lugares=["Torre Eiffel","Museu do Louvre","Catacumbas de Paris","Biblioteca Nacional","Galeria Lafayette","Parque dos Príncipes","Catedral de Notre-Dame","Jardim de Luxemburgo","Padaria Dupain Cheng"]
#lista de lugares
hora_abertura=[900,800,1000,700,1000,600,800,700,400] 
hora_fechamento=[2300,1800,2000,2200,2100,2300,1830,1900,2000]
#transformação para horas militares para facilitar de comparar
seguranca=["Média","Alta","Baixa","Média","Alta","Baixa","Alta","Média","Baixa"]
#lista da segurança dos lugares

lugares_suspeitos=[] #lista para contagem de mais de uma pessoa em local que não existe
nomes_lugares_suspeitos=[] #lista para contagem do nome de uma pessoa em local que não existe
funcionamento_suspeito=[] #lista para contagem de mais de uma pessoa em funcionamento fora da hora
nomes_funcionamento_suspeito=[] #lista para contagem do nome de uma pessoa em horário de funcionamento errado
horario_suspeito=[]
nomes_seguranca_suspeita=[] #lista para contagem do nome de uma pessoa em segurança baixa
sem_alibi=[] #lista de pessoas sem alibi

for i in range(6):
    linha=input()
    nome,horario,lugar,alibi=linha.split(" - ")
    horario_24h=horario
    horario=horario.replace(":","")
    horario_militar=int(horario)
    if lugar not in lugares:
        lugares_suspeitos.append(lugar)
        nomes_lugares_suspeitos.append(nome)
    else:
        indice=lugares.index(lugar)
        if horario_militar<hora_abertura[indice] or horario_militar>hora_fechamento[indice]:
            funcionamento_suspeito.append(lugar)
            nomes_funcionamento_suspeito.append(nome)
            horario_suspeito.append(horario_24h)
        elif seguranca[indice]=="Baixa":
            nomes_seguranca_suspeita.append(nome)
        elif alibi=="nenhuma":
            sem_alibi.append(nome)

#laço da investigação

lugares_suspeitos.sort()
nomes_lugares_suspeitos.sort()
funcionamento_suspeito.sort()
nomes_funcionamento_suspeito.sort()
nomes_seguranca_suspeita.sort()
sem_alibi.sort()

#ordenação em ordem alfabética das listas de suspeitos

if len(lugares_suspeitos)==1: #condicional de lugares suspeitos
    print(f"Esse lugar {lugares_suspeitos[0]} nem existe! {nomes_lugares_suspeitos[0]} com certeza foi akumatizado!")
elif len(lugares_suspeitos)>1:
    print(f"{', '.join(lugares_suspeitos)} nem existem! {', '.join(nomes_lugares_suspeitos)} estão mentindo!") 
else: #se não houver lugares suspeitos
    if len(funcionamento_suspeito)==1: #condicional de presença fora de horário de funcionamento
        print(f"{funcionamento_suspeito[0]} nem estava aberto às {horario_suspeito[0]}! {nomes_funcionamento_suspeito[0]} recebeu memórias falsas!")
    elif len(funcionamento_suspeito)>1:
        print(f"{', '.join(funcionamento_suspeito)} estavam fechados nesse horário! {', '.join(nomes_funcionamento_suspeito)} podem ter sido manipulados pelo Hawk Moth!")
    else: #se todos estiverem nos horários certos
        if len(nomes_seguranca_suspeita)==1: #condicional de locais de segurança baixa
            print(f"{nomes_seguranca_suspeita[0]} estava em um local de segurança baixa... Ele pode ter mentido!")
        elif len(nomes_seguranca_suspeita)>1:
            print(f"{', '.join(nomes_seguranca_suspeita)} estavam em locais de segurança baixa... Eles podem estar forjando um álibi!")
        else: #caso todos estejam em locais de boa segurança
            if len(sem_alibi)==1: #condicional de pessoas sem alibi
                print(f"{sem_alibi[0]} não teve testemunha para confirmar o álibi. É o mais suspeito até agora.")
            elif len(sem_alibi)>1 and len(sem_alibi)<6:
                print(f"{', '.join(sem_alibi)} não foram confirmados por ninguém. O Hawk Moth pode vir atrás deles de novo")
            elif len(sem_alibi)==6:
                print("Ninguém viu ninguém… estranho!!")
            else: #caso não haja nenhum suspeito
                print("Poxa vida, todos os àlibis parecem válidos… mas algo continua errado")