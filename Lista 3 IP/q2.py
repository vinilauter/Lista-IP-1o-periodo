lista=True #variável booleana do loop
compras=[] #lista de compras

while lista: #laço de inserção dos ingredientes
    acao=input()
    if acao=="Anotar ingrediente": #insere na última posição da lista
        ingrediente=input()
        compras.append(ingrediente) 
    elif acao=="Ingrediente Urgente!": #insere na posição 0 da lista
        ingrediente=input()
        compras.insert(0,ingrediente)
    elif acao=="Saci disse que já tem": #tira um elemento da lista
        ingrediente=input()
        compras.remove(ingrediente)
    elif acao=="Saci trocou a ordem": #reordena um elemento na lista
        i1=int(input())
        i2=int(input())
        compras[i1],compras[i2]=compras[i2],compras[i1]
    elif acao=="Organizar a lista": #troca de posição dois elementos da lista, um pelo outro
        ingrediente1=input()
        ingrediente2=input()
        i1=compras.index(ingrediente1)
        i2=compras.index(ingrediente2)
        compras[i1],compras[i2]=compras[i2],compras[i1]
    elif acao=="Deixar para depois": #coloca um ingrediente no final da lista
        ingrediente=input()
        compras.remove(ingrediente)
        compras.append(ingrediente)
    elif acao=="Ler a lista para a vovó": #imprime todos os elementos da lista
        print(", ".join(compras))
    elif acao=="E por hoje é só, pessoal!": #finaliza o loop
        lista=False
    acao="" #zera a ação
    ingrediente="" #zera os ingredientes
    ingrediente1="" #zera os ingredientes
    ingrediente2="" #zera os ingredientes

print(f"Pronto, vovó! A lista de compras para o bolo de Narizinho está pronta. Podemos ir ao mercado. A lista final é: {', '.join(compras)}") #print final
    
