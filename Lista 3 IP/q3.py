nmr_armas=int(input())
armas=[]
for i in range(nmr_armas):
    arma=input()
    armas.append(arma) #insere a arma na lista

#variáveis iniciais e criação do arsenal

golpes=0 #variável dos golpes do Thanos
item="" #variável dos itens solicitados
qtd_armas=0 #quantidade de armas utilizadas
armas_usadas=[] #lista de armas utilizadas

while item!="fim": #condição de finalização do loop é a palavra "fim"
    item=input() #input do item
    if item!="fim":
        if item in armas_usadas:
            print(f"{item} já foi usado(a)!")
            golpes+=1
        elif item not in armas:
            print(f"{item} não está disponível!")
            golpes+=1
        else:
            print(f"{item} usado(a) com sucesso!")
            qtd_armas+=1
            armas_usadas.append(item)

#laço da batalha

print(f"Batalha encerrada! Os Vingadores utilizaram {qtd_armas} arma(s).")
if golpes==0: #print da vitória perfeita
    print("Vitória! Os Vingadores salvaram o UNIVERSO!")
    print("")
    print("Tony Stark:")
    print("Salvar o mundo de novo? Vou precisar de um aumento.")
    print("")
    print("Thor:")
    print("Espero que tenha cerveja depois disso!")
    print("")
    print("Homem-Aranha:")
    print("Posso dizer que ajudei, né? Tipo… oficialmente?")
    print("Dá pra postar isso no Insta dos Vingadores?")
elif golpes==1: #print da vitória apertada
    print("Os Vingadores sofreram um golpe do Thanos!")
    print("Vitória por pouco! Os Vingadores ganharam...")
    print("")
    print("Tony Stark:")
    print("Quase que eu fico sem troco para o cafezinho.")
    print("")
    print("Thor:")
    print("Esse quase foi o meu momento de “não consegui”. Mas consegui, então vale cerveja!")
    print("")
    print("Peter Quill (Star-Lord):")
    print("Cara, quase perdi o ritmo do meu walkman!")
else: #print da derrota
    print(f"Os Vingadores sofreram {golpes} golpes do Thanos!")
    print("Derrota... Os Vingadores não conseguiram todas as armas necessárias.")
    print("")
    print("Tony Stark:")
    print("Essa não foi das melhores ideias...")
    print("")
    print("Thor:")
    print("Culpa do humano. Eu sabia que devíamos ter chamado o Hulk.")

