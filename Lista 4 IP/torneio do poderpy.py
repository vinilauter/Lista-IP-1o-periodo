# função do cálculo da força

def forca(tecnica):
    pontuacao=len(tecnica)%8
    return pontuacao

#função para verificar a necessidade de um terceiro lutador

def reforco(lutador1,lutador2):
    p3=""
    if 'Goku' in lutador1 or 'Goku' in lutador2 or 'Frieza' in lutador1 or 'Frieza' in lutador2:
        if 'Jiren' in lutador1 or 'Jiren' in lutador2:
            p3=input()
    if 'Gohan' in lutador1 or 'Gohan' in lutador2:
        if 'Namekuseijins' in lutador1 or 'Namekuseijins' in lutador2:
            p3=input()
    if 'Androide 17' in lutador1 or 'Androide 17' in lutador2:
        if 'Ribrianne' in lutador1 or 'Ribrianne' in lutador2:
            p3=input()
    return p3

#programa principal

qtd_batalhas=int(input())
print(f"O torneio do poder irá começar com {qtd_batalhas} batalhas no dia de hoje! Vamos ver quais universos vão conseguir se manter vivos até o final do dia!")
for i in range(qtd_batalhas):
    p1=input()
    lutador1,tecnica1=p1.split(" - ")
    p2=input()
    lutador2,tecnica2=p2.split(" - ")
    p3=reforco(lutador1,lutador2)
    if p3!='':
        lutador3,tecnica3=p3.split(" - ")
        print(f"A intensidade dos dois lutadores motivou {lutador3} a entrar na batalha também!")
        poder1=forca(tecnica1)
        poder2=forca(tecnica2)
        poder3=forca(tecnica3)
        if "Goku" in lutador1 or "Frieza" in lutador1 or "Gohan" in lutador1 or "Androide 17" in lutador1:
            poder_combinado=poder1+poder3
            if poder_combinado>poder2:
                vencedor=f"{lutador1} e {lutador3}"
            else:
                vencedor=lutador2
        else:
            poder_combinado=poder2+poder3
            if poder_combinado>poder1:
                vencedor=f"{lutador2} e {lutador3}"
            else:
                vencedor=lutador1
        print(f"Uma batalha brutal entre 3 lutadores! Os espectadores vão à loucura com essas amostras de {tecnica1}, {tecnica2} e {tecnica3}! A batalha acaba com {vencedor} no topo!")
    else:
        poder1=forca(tecnica1)
        poder2=forca(tecnica2)
        if poder1>poder2:
            vencedor=lutador1
        elif poder2>poder1:
            vencedor=lutador2
        print(f"Incrível! {vencedor} mostrou sua força e defenderá seu universo até o final!")
    

