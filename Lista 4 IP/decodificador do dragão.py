# função de verificação de número primo

def primo(numero):
    if numero<=1:
        return False
    
    for i in range(2,numero):
        if numero%i==0:
            return False
        
    return True

# função da notação polonesa pura

operadores=['+','-','*','/']
def notacao_polonesa(expressao):

    pilha=[]
    elementos=expressao.split()

    # Iterar sobre os elementos da direita para a esquerda

    for elemento in reversed(elementos):
        if elemento not in operadores:
            pilha.append(elemento)
        elif elemento in operadores:
            op1=pilha.pop()
            op2=pilha.pop()

            if elemento=='+':
                resultado=int(op1)+int(op2)
            elif elemento=='-':
                resultado=int(op1)-int(op2)
            elif elemento=='*':
                resultado=int(op1)*int(op2)
            elif elemento=='/':
                if op1==0 or op2==0:
                    resultado=0
                else:
                    resultado=int(op1)//int(op2)
            pilha.append(resultado) 
    
    if primo(pilha[0]):
        return 1
    else:
        return 0

# função de conversão binário-decimal

def conversor_binario_decimal(numero_binario):
    numero_decimal=int(numero_binario,2)
    return numero_decimal

# função para processar as coordenadas

def processar_coordenadas(numero_decimal,N):
    coordenada_esfera=numero_decimal%N
    return coordenada_esfera

# função de esfera mais próxima

def distancia_esfera(coordenadas_esferas_x,coordenadas_esferas_y,coordenada_goku_x,coordenada_goku_y):
    distancia_euclidiana=((coordenada_goku_x-coordenadas_esferas_x)**2+(coordenada_goku_y-coordenadas_esferas_y)**2)**0.5
    return distancia_euclidiana

# programa principal

print("🟠 Vamos conquistar as esferas do dragão! 🟠")
print("-"*74)
print()

# input da ordem quadrada da matriz e da coordenada do Goku

N=int(input())
coordenadas_goku=input()
coordenadas_goku_str=coordenadas_goku.strip("()")
coordenada_goku_x,coordenada_goku_y=coordenadas_goku_str.split(", ")

# input da linha vazia

linha_vazia=input()

# input das expressões e outputs das coordenadas das esferas

coordenadas_esferas_x=[]
coordenadas_esferas_y=[]

lista_array_x=[]
lista_array_y=[]

n_esfera=0

expressao=""
estado_atual=""

array_x=""
array_y=""


while expressao!="Todos os bits foram decodificados":
    expressao=input()
    if expressao[0:3]=="---":
        estado_atual="X"
    elif expressao=='':
        if estado_atual=="X": 
            estado_atual="Y"
            coordenadas_esferas_x.append(processar_coordenadas(conversor_binario_decimal(array_x),N))
            lista_array_x.append(array_x)
            array_x=""
        if estado_atual=="Y":
            if array_y!="":
                coordenadas_esferas_y.append(processar_coordenadas(conversor_binario_decimal(array_y),N))
                lista_array_y.append(array_y)
                array_y=""
    elif expressao[0] in operadores:
        digito=notacao_polonesa(expressao)
        if estado_atual=="X":
            array_x+=str(digito)
        elif estado_atual=="Y":
            array_y+=str(digito)


for i in range(len(coordenadas_esferas_x)):
    n_esfera+=1
    print(f"Coordenada x da {n_esfera}ª esfera do dragão obtida pelo código binário {lista_array_x[i]}: {coordenadas_esferas_x[i].strip("()")})")
    print(f"Coordenada y da {n_esfera}ª esfera do dragão obtida pelo código binário {lista_array_y[i]}: {coordenadas_esferas_y[i].strip("()")})")
    print(f"As coordenadas da {n_esfera}ª esfera do dragão são: ({coordenadas_esferas_x[i]}, {coordenadas_esferas_y[i]})\n")
print("-"*74)
print()

# criação do terreno 

terreno=[["." for _ in range(N)] for _ in range(N)]

terreno[int(coordenada_goku_x)][int(coordenada_goku_y)]="G"

for i in range(n_esfera):
    terreno[coordenadas_esferas_x[i]][coordenadas_esferas_y[i]]="☆"

for i in range(N):
    for j in range(N):
        print(terreno[i][j],end=" ")
    print()

# análise e print do caminho percorrido

distancias=[]
trajeto=f"({coordenada_goku_x},{coordenada_goku_y})"
while n_esfera>0:
    for i in range(len(coordenadas_esferas_x)):
        distancias.append(distancia_esfera(coordenadas_esferas_x[i],coordenadas_esferas_y[i],int(coordenada_goku_x),int(coordenada_goku_y)))
    indice_menor=distancias.index(min(distancias))
    trajeto+=f" -> ({coordenadas_esferas_x[indice_menor]},{coordenadas_esferas_y[indice_menor]})"
    coordenada_goku_x=coordenadas_esferas_x[indice_menor]
    coordenada_goku_y=coordenadas_esferas_y[indice_menor]
    coordenadas_esferas_x.pop(indice_menor)
    coordenadas_esferas_y.pop(indice_menor)
    distancias.pop(indice_menor)
    n_esfera-=1

print(f"Trajetória completa de Goku: {trajeto}")
print("Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉")




