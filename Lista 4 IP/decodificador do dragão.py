# função de verificação de número primo

def primo(numero):
    if numero<=1:
        return False
    
    for i in range(2,numero):
        if numero%i==0:
            return False
        
    return True

# função da notação polonesa pura

def notacao_polonesa(expressao):

    pilha=[]
    operadores=['+','-','*','/']
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

# programa principal