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

def processar_coordenadas(numero_decimal,coordenadas_goku):
    coordenada_esfera=numero_decimal%coordenadas_goku
    return coordenada_esfera

# função de esfera mais próxima

def esfera_mais_proxima(coordenada_esfera_x,coordenada_esfera_y,coordenada_goku_x,coordenada_goku_y):
    distancia_euclidiana=((coordenada_goku_x-coordenada_esfera_x)**2+(coordenada_goku_y-coordenada_esfera_y)**2)**0.5
    return distancia_euclidiana

# função para processar a string

def processar_string(expressao):
    coordenada_esfera_x=[]
    coordenada_esfera_y=[]
    estado_atual="X"
    array_x=""
    array_y=""
    linhas=expressao.strip().split("\n")
    total_linhas=len(linhas)
    for i in range(total_linhas):
        linha=linhas[i].strip()
        ultima_linha=(i==total_linhas-1)
    
        # definição dos estados

        if linha[0:3]=="---":
            estado_atual="X"
            if array_y!="":
                coordenada_esfera_y.append(conversor_binario_decimal(array_y))
                array_y=""
        elif linha[0] in operadores:
            digito=notacao_polonesa(linha)
            if estado_atual=="X":
                array_x+=int(digito)
            elif estado_atual=="Y":
                array_y+=int(digito)
        elif linha[0]==" ":
            estado_atual="Y"
            coordenada_esfera_x.append(conversor_binario_decimal(array_x))
            array_x=""
        





# programa principal

print("🟠 Vamos conquistar as esferas do dragão! 🟠")
print("-"*74)
print()

# input da ordem quadrada da matriz e da coordenada do Goku

n=int(input())
coordenadas_goku=input()
coordenada_goku_x,coordenada_goku_y=coordenadas_goku.split()

# input da linha vazia

linha_vazia=input()

# input das expressões

expressao=""
while expressao!="Todos os bits foram decodificados!":
    expressao=input()