# Função de descriptografia

def descriptografar(nome_criptografado):

    # caracteres ascii

    ascii_chars = [' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?','@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I','J','K', 'L', 'M', 'N', 'O','P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y','Z', '[', '\\', ']', '^', '_','`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

    # passo 1 (inversão do passo 7): transformar em lista
    
    lista_nome_criptografado=list(nome_criptografado)

    # passo 2 (inversão do passo 6): desconcatenar cada metade

    meio=len(lista_nome_criptografado)//2
    primeira_metade=lista_nome_criptografado[:meio]
    segunda_metade=lista_nome_criptografado[meio:]
    
    # passo 3 (inversão do passo 5): deslocamento de +1 posição ascii

    tamanho_ascii = len(ascii_chars)

    for i in range(len(segunda_metade)):
        indice_atual=ascii_chars.index(segunda_metade[i])
        novo_indice=(indice_atual + 1)%tamanho_ascii
        segunda_metade[i]=ascii_chars[novo_indice]
    
    # passo 4 (inversão do passo 4): juntar a lista

    lista_nome_criptografado=primeira_metade+segunda_metade

    # passo 5 (inversão do passo 3): inversão da lista

    lista_nome_criptografado.reverse()

    # passo 6 (inversão do passo 2): deslocamento -3 posição ascii

    for i in range(len(lista_nome_criptografado)):
        indice_atual=ascii_chars.index(lista_nome_criptografado[i])
        novo_indice=(indice_atual-3)%tamanho_ascii
        lista_nome_criptografado[i]=ascii_chars[novo_indice]

    # passo 7 (inversão do passo 1): transformar em uma string

    nome_descriptografado=""
    nome_descriptografado = "".join(lista_nome_criptografado)

    return nome_descriptografado

# Programa principal

nmr_jogadores=int(input())
escalacao_br={}

# fase de descriptografia

for i in range(nmr_jogadores):
    nome_criptografado=input()
    nome_descriptografado=descriptografar(nome_criptografado)
    print(f"Criptografada: {nome_criptografado}")
    print(f"Descriptografada: {nome_descriptografado}")
    print("-"*50)
    escalacao_br[nome_criptografado]=nome_descriptografado

# mensagens de status

tecnico=False

for nome_jogador in escalacao_br.values():
    if nome_jogador=="Ronaldo":
        print("Ronaldo Fenômeno detectado! Autor dos gols na final!")
    elif nome_jogador=="Ronaldinho":
        print("Ronaldinho Gaúcho chegou! Chamem o inglês que ele vai chutar do meio-campo...")
    elif nome_jogador=="Cafu":
        print("Capitão Cafu presente! O único a jogar 3 finais de Copa seguidas!")
    elif nome_jogador=="Marcos":
        print("Marcos está na área! O paredão do Brasil em 2002!")
    elif nome_jogador=="Luiz Felipe Scolari":
        print("Técnico reconhecido: Luiz Felipe Scolari — o comandante do penta!")
        tecnico=True
    else:
        print(f"{nome_jogador} está confirmado na escalação!")

print()

# sumário final

if tecnico:
    nmr_jogadores-=1

# checagem do número de jogadores

if nmr_jogadores<11:
    print("!!!!!!!!!! Escalação incompleta! !!!!!!!!!!")
    print(f"Só foram encontrados {nmr_jogadores} jogadores. Faltam jogadores para completar o time.")
else:
    print("++++++++++ Escalação Confirmada ++++++++++")
    print("Escalação Oficial da Seleção Brasileira — Copa do Mundo 2002")

# print dos jogadores

    print("==================================================")

    for nome_jogador in escalacao_br.values():
        if nome_jogador!="Luiz Felipe Scolari":
            print(f"->{nome_jogador}")

    print("==================================================")

# verificação do técnico

if not tecnico:
    print("!!!!!!!!!! Técnico não encontrado! !!!!!!!!!!")
    print("Como vamos jogar sem treinar? Como vamos ganhar o penta?")
elif tecnico:
    print("========== Técnico ==========")
    print("Luiz Felipe Scolari (Felipão)") 

if tecnico and nmr_jogadores>=11:
    print("===== Tudo pronto! Rumo ao Penta! =====")
    print("Escalação completa com técnico confirmado.")
    print("Que comece o espetáculo, Brasil rumo ao penta!")
    