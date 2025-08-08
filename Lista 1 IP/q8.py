humor=input()
quantidade_senta=int(input())
quantidade_patinha=int(input())
quantidade_fica=int(input())
quantidade_pega=int(input())
prox_comando=input()
#inputs
if prox_comando=="Senta":
    quantidade_senta+=1
    if quantidade_senta>=3 and humor!="Brincalhão":
        print("Byte é o melhor")
    elif humor=="Brincalhão" and quantidade_senta>=3:
        print("Ele parece estar muito animado para isso!")
    else:
        print("Parece que ele não aprendeu esse truque ainda")
#comando senta
if prox_comando=="Dá a patinha":
    quantidade_patinha+=1
    if quantidade_patinha>=3:
        print("Ele é um bom garoto!")
    else:
        print("Parece que ele não aprendeu esse truque ainda")
#comando patinha
if prox_comando=="Fica":
    quantidade_fica+=1
    if quantidade_fica>=3 and humor!="Brincalhão":
        print("Ele está aprendendo")
    elif humor=="Brincalhão" and quantidade_fica>=3:
        print("Ele não consegue ficar parado")
    else:
        print("Parece que ele não aprendeu esse truque ainda")
#comando fica
if prox_comando=="Pega":
    quantidade_pega+=1
    if quantidade_pega>=3 and humor!="Preguiçoso":
        print("Ele é muito ágil!")
    elif humor=="Preguiçoso" and quantidade_pega>=3:
        print("Quem não tem seu momento de preguiça?")
    else:
        print("Parece que ele não aprendeu esse truque ainda")
#comando pega
if quantidade_senta>=3 or quantidade_patinha>=3 or quantidade_fica>=3 or quantidade_pega>=3:
    print(f"O nosso novo mascote estava {humor} e aprendeu o(s) seguinte(s) truque(s):")
    if quantidade_senta>=3:
        print("Senta")
    if quantidade_patinha>=3:
        print("Dá a patinha")
    if quantidade_fica>=3:
        print("Fica")
    if quantidade_pega>=3:
        print("Pega")
