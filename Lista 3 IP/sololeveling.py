n_jinwoo=int(input())
qtd=int(input())
exercito=[]
vivo=True
i=0

#variáveis iniciais

while i<qtd and vivo:
    nome=input() 
    nivel=int(input())
    if nivel<n_jinwoo: #condicional de adição de criatura ao exército
        resposta=input()
        if resposta=="Erga-se":
            exercito.append(nome) #adição
            n_jinwoo+=nivel//3 #aumento de nível
    elif nivel>=n_jinwoo: #condicional da derrota 
        print(f"Jin-Woo foi derrotado por {nome}...")
        vivo=False
    nome="" #reset do nome
    nivel="" #reset do nível da criatura
    i+=1

#laço da caçada

if vivo: 
    print("Jin-Woo sobreviveu à caçada, um verdadeiro Monarca das Sombras mesmo!") #print se tiver derrotado todas as criaturas
print("===== Exército das Sombras de Jin-Woo =====") #print do exército
if len(exercito)==0:
    print("Jin-Woo não conseguiu formar seu exército...") #print se não tiver exército
else:
    contador = {}
    ordem_original = []
    for elemento in exercito:
        if elemento not in contador:
            contador[elemento] = 0
            ordem_original.append(elemento)
        contador[elemento] += 1
    for elemento in ordem_original:
        print(f"{elemento}: {contador[elemento]}")
                