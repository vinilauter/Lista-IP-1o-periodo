ondas=int(input()) #input das ondas
vit_viloes=0 #número de vitórias dos vilões para o cálculo final
vit_herois=0 #número de vitórias dos heróis para o cálculo final
diferenca_maior=[] #lista da rodada mais dispar 
diff_maior=0 #diferença maior apenas para comparação
contador_ondas=0 #contador para ser o índice da onda mais dispar
vencedores=False

#variáveis globais

for i in range(ondas): #laço das ondas
    contador_ondas+=1 #adição no contador
    herois=0 #variáveis para a verificação do número de heróis
    viloes=0 #variáveis para a verificação do número de vilões
    sequencia=input() #input da sequência de vilões e heróis
    grande_lista=sequencia.split(', ') #armazenamento dos heróis e vilões em uma lista
    lista_combate=grande_lista[1:-1] #retirada do primeiro e do último
    for nome in lista_combate: #análise do primeiro caracter de cada palavra
        if nome[0]=="H": #condição para ser herói 
            herois+=1 
        else: #se não for herói, é vilão
            viloes+=1 
    diff=herois-viloes #variável da diferença
    if diff>0: #condição de vitória dos heróis
        vit_herois+=1
    elif diff<0: #condição de vitória dos vilões
        vit_viloes+=1
    if len(diferenca_maior)==0 and diff!=0: #condição caso não haja nenhuma onda com com resultado decisivo na lista de diferença maior
        vencedores=True
        diferenca_maior=grande_lista
        diff_maior=diff
        indice=contador_ondas
    elif diff!=0 and abs(diff)>abs(diff_maior): #condição de análise quando já há uma onda na lista
        diferenca_maior=grande_lista
        diff_maior=diff
        indice=contador_ondas

#loop das batalhas

if vencedores:
    if diff_maior>0:
        print(f"🌀Onda {indice} foi a menos acirrada e a mais favorável para os heróis!")
        print(f"Participantes analisados: {', '.join(diferenca_maior)}")
    else:
        print(f"🌀Onda {indice} foi a menos acirrada e a mais favorável para os vilões!")
        print(f"Participantes analisados: {', '.join(diferenca_maior)}")
else:
    print("🌀Nenhuma onda foi selecionada como a menos acirrada e a mais favorável para nenhum do dois lados!")

#prints dos resultados das ondas dispares (ou a falta delas)

print("Agora vamos ao resultado geral das ondas...")
print(f"Heróis: {vit_herois} | Vilões: {vit_viloes}")
if vit_herois>vit_viloes:
    print("Ufa, os heróis dominaram! Central City está seguro outra vez")
elif vit_viloes>vit_herois:
    print("Ah, não. Os vilões vão dominar Central City e mandar todos os heróis embora!")
else:
    print("Ninguém é mais forte que ninguém. Heróis e vilões vão ter que entrar em consenso para viverem no mesmo espaço")