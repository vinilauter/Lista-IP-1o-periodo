cin1="false"
cin2="false"
cin3="false"
espião1="false"
espião2="false"
espião3="false"
nome_1=input()
quem_indicou_1=input()
pontos_1=0+len(nome_1)
if "cin" in nome_1:
    cin1="true"
    pontos_1+=10
if "gato" in nome_1:
    pontos_1=0
if quem_indicou_1=="felino espião":
    pontos_1=0
    espião1="true"
#dados e análise nome 1
nome_2=input()
quem_indicou_2=input()
pontos_2=0+len(nome_2)
if "cin" in nome_2:
    cin3="true"
    pontos_2+=10
if "gato" in nome_2:
    pontos_2=0
if quem_indicou_2=="felino espião":
    pontos_2=0
    espião2="true"
#dados e análise nome 2
nome_3=input()
quem_indicou_3=input() 
pontos_3=0+len(nome_3)
if "cin" in nome_3:
    cin3="true"
    pontos_3+=10
if "gato" in nome_3:
    pontos_3=0
if quem_indicou_3=="felino espião":
    pontos_3=0
    espião3="true"
#dados e análise nome 3
if pontos_1>pontos_2 and pontos_1>pontos_3:
    primeiro_lugar=nome_1
    if pontos_2>pontos_3:
        segundo_lugar=nome_2
        terceiro_lugar=nome_3
    else:
        segundo_lugar=nome_3
        terceiro_lugar=nome_2
# caso primeiro nome ganhe
if pontos_2>pontos_1 and pontos_2>pontos_3:
    primeiro_lugar=nome_2
    if pontos_1>pontos_3:
        segundo_lugar=nome_1
        terceiro_lugar=nome_3
    else:
        segundo_lugar=nome_3
        terceiro_lugar=nome_1
#caso segundo nome ganhe
if pontos_3>pontos_1 and pontos_3>pontos_2:
    primeiro_lugar=nome_3
    if pontos_2>pontos_1:
        segundo_lugar=nome_2
        terceiro_lugar=nome_1
    else:
        segundo_lugar=nome_1
        terceiro_lugar=nome_2
#caso terceiro nome ganhe
if cin1=="true" and espião1!="true":
    print("Os melhores nomes são aqueles que fazem referência a minha casinha :)")
if cin2=="true" and espião2!="true":
    print("Os melhores nomes são aqueles que fazem referência a minha casinha :)")
if cin3=="true" and espião3!="true":
    print("Os melhores nomes são aqueles que fazem referência a minha casinha :)")
if espião1=="true":
    print("Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.")
if espião2=="true":
    print("Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.")
if espião3=="true":
    print("Essa não! Os gatos querem arruinar o aniversário de Byte. Não deixe isso acontecer.")
print(f"RANKING DOS NOMES:\nPrimeiro lugar: {primeiro_lugar}\nSegundo lugar: {segundo_lugar}\nTerceiro lugar: {terceiro_lugar}")