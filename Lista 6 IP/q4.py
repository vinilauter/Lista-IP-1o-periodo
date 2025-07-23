# função do cálculo da pontuação total
def calculo_pontuacao(continentais, nacionais, aproveitamento, nacionalidade):
    pontuacao_total = (continentais*100+nacionais*50)*aproveitamento

    # checagem de nacionalidade
    if nacionalidade=="brasileiro":
        pontuacao_total+=pontuacao_total*0.1
    elif nacionalidade=="alemão":
        pontuacao_total-=pontuacao_total*0.1

    # checagem de continentais
    if continentais==0:
        pontuacao_total-=pontuacao_total*0.5

    return pontuacao_total

# função auxiliar para o ordenamento

def buscar_candidato_pela_pontuacao(pontuacao_alvo, dicionario_candidatos):
    # Iteramos sobre as chaves (nomes) do dicionário
    for nome_candidato in dicionario_candidatos:
        dados=dicionario_candidatos[nome_candidato]
        if dados['pontuacao']==pontuacao_alvo:
            return nome_candidato
        
# programa principal 

candidatos_dados={}
candidatos=int(input())

for i in range(candidatos):

    # leitura das informações do candidato

    nome=input()

    if nome=="Ancelotti":
        print("Será que Carleto irá continuar no cargo?")
    elif nome=="Jorge Jesus":
        print("O mister finalmente retornará ao Brasil?")

    nacionalidade=input()

    if nacionalidade=="alemão":
        print("Iremos mesmo perdoar o 7x1?")
    if nacionalidade=="argentino":
        print("Um hermano comandando a seleção? Sai fora!")
    if nacionalidade!="argentino":
        continentais=int(input())
        nacionais=int(input())
        aproveitamento=float(input())
        interesse=input()

        # calculo e armazenamento das informações

        pontuacao=calculo_pontuacao(continentais, nacionais, aproveitamento, nacionalidade)

        candidatos_dados[nome]={
            'nacionalidade': nacionalidade,
            'pontuacao': pontuacao,
            'interesse': interesse
        }

# ordenamento das pontuações 

pontuacoes_extraidas={}

for nome_candidato in candidatos_dados:
    dados=candidatos_dados[nome_candidato]
    pontuacoes_extraidas[dados['pontuacao']]=True

pontuacoes_ordenadas={}
copia_pontuacoes=pontuacoes_extraidas.copy()
indice=0

while copia_pontuacoes:
    maior_pontuacao=-1000.0
    for pontuacao in copia_pontuacoes:
        if pontuacao>maior_pontuacao:
            maior_pontuacao=pontuacao
    
    pontuacoes_ordenadas[indice]=maior_pontuacao
    indice=indice+1
    del copia_pontuacoes[maior_pontuacao]

print("Lista de treinadores - CBF")
for i in range(3):
    pontuacao_atual=pontuacoes_ordenadas[i]
    nome_do_candidato=buscar_candidato_pela_pontuacao(pontuacao_atual, candidatos_dados)
    
    dados_do_candidato=candidatos_dados[nome_do_candidato]
    nacionalidade_candidato=dados_do_candidato['nacionalidade']
    interesse_candidato=dados_do_candidato['interesse']
    
    pontuacao_formatada=f"{pontuacao_atual:.2f}"
    
    print(f"{i+1}º {nome_do_candidato} - {nacionalidade_candidato} - {pontuacao_formatada} pontos")

# escolha do técnico

tecnico_escolhido=False

# checagem do ancelotti

ancelotti=False

i=0

while not tecnico_escolhido and i<3:
    pontuacao_atual=pontuacoes_ordenadas[i]
    nome_do_candidato=buscar_candidato_pela_pontuacao(pontuacao_atual, candidatos_dados)
    dados_do_candidato=candidatos_dados[nome_do_candidato]
    interesse_candidato=dados_do_candidato['interesse']
    nacionalidade_candidato=dados_do_candidato['nacionalidade']
    if interesse_candidato=="sim":
        if nome_do_candidato=="Ancelotti":
            ancelotti=True
            print(f"{nome_do_candidato} será o quarto estrangeiro a treinar o Brasil. Que honra para o {nacionalidade_candidato}!")
            print("Depois de uma longa novela, Carlo Ancelotti continuará como o treinador da Seleção Brasileira! Estamos bem servidos!")
            tecnico_escolhido=True
    i=i+1

i=0 

while not tecnico_escolhido and i<3:

    pontuacao_atual=pontuacoes_ordenadas[i]
    nome_do_candidato=buscar_candidato_pela_pontuacao(pontuacao_atual, candidatos_dados)
    dados_do_candidato=candidatos_dados[nome_do_candidato]
    interesse_candidato=dados_do_candidato['interesse']
    nacionalidade_candidato=dados_do_candidato['nacionalidade']

    # checagem do ancelotti
    
    if interesse_candidato=="sim":

        # prints do estrangeiro
        if nacionalidade_candidato!="brasileiro" and not ancelotti:
            print(f"{nome_do_candidato} será o quarto estrangeiro a treinar o Brasil. Que honra para o {nacionalidade_candidato}!")
            tecnico_escolhido=True
        # casos especiais
        if nome_do_candidato=="Jorge Jesus":
            print("JESUS VOLTOU!!! Será que ele conseguirá repetir na seleção o sucesso que obteve no Flamengo?")
            tecnico_escolhido=True
        elif nome_do_candidato=="Felipão":
            print("FELIPÃO DE NOVO!? Vem mais um 7x1 por aí?")
            tecnico_escolhido=True
        # caso genérico de técnicos
        else:
            print(f"O técnico {nacionalidade_candidato} {nome_do_candidato} irá treinar o Brasil. Não era o nome que esperávamos, mas torcemos para que faça um bom trabalho!")
            tecnico_escolhido=True

    elif interesse_candidato=="não" and not tecnico_escolhido: 
        print(f"O {nome_do_candidato} não aceitou a proposta da CBF e outros nomes serão analisados. Cuida, CBF!")
    
    i=i+1

if not tecnico_escolhido:
    print("Nenhum técnico aceitou a maior seleção do mundo!? Que humilhação, Sr. Samir Xaud!!!")