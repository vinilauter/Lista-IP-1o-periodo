#função da distância euclidiana

def distancia_euclidiana(x,y):
    distancia=(x**2)+(y**2)
    return distancia**0.5

#programa principal

#listas de objetos e distâncias respectivas

objetos=[]
indices_esferas=[]
distancias=[]

#input dos objetos

n_objetos=int(input())

#laço da detecção do radar

for i in range(n_objetos):
    nome_objeto=input()
    objetos.append(nome_objeto)
    x_objeto=int(input())
    y_objeto=int(input())
    if nome_objeto=="rocha":
        print("Radar: Rocha detectada! Bulma resmunga: 'Só um pedregulho cósmico... Sem valor para mim!'")
    elif nome_objeto=="árvore":
        print("Radar: Árvore à vista! Bulma comenta: 'Interessante, mas não brilha como uma esfera. Próximo alvo!'")
    elif nome_objeto=="nave":
        print("Radar: Sinal de nave! Bulma alerta: 'Pode ser Pilaf ou a Patrulha Vermelha! Melhor ficar atenta, mas o foco são as esferas!'")
    elif nome_objeto!="esfera" and nome_objeto!="rocha" and nome_objeto!="árvore" and nome_objeto!="nave":
        print(f"Radar: Detectado um(a) {nome_objeto}. Não parece ser uma esfera... Continuando a busca.")
    if nome_objeto=="esfera" and distancia_euclidiana(x_objeto,y_objeto) not in distancias:
        indices_esferas.append(i)
        distancias.append(distancia_euclidiana(x_objeto,y_objeto))

#outputs finais

if len(distancias)>0:
    posicao_no_radar=indices_esferas[(distancias.index(min(distancias)))]+1
    print(f"ALVO PRIORITÁRIO: Esfera | Distância: {min(distancias):.2f}m | Detecção Original: {posicao_no_radar}°")
else: 
    print("Radar varreu a área. Nenhuma esfera do dragão à vista desta vez!")