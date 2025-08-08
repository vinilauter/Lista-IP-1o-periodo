qnt_pessoas=int(input())
classica=0
classineta=0
caneta=0

primeiro_lugar=""
segundo_lugar=""
terceiro_lugar=""

#variáveis

for i in range(qnt_pessoas):
    voto=input()
    if voto=="Clássica":
        classica+=1
    elif voto=="Classineta":
        classineta+=1
    elif voto=="Caneta":
        caneta+=1

#laço dos votos

pts_primeiro=max(classica,classineta,caneta)
if max(classica,classineta,caneta)==classica:
    primeiro_lugar="Clássica"
elif max(classica,classineta,caneta)==classineta:
    primeiro_lugar="Classineta"
else:
    primeiro_lugar="Caneta"

pts_terceiro=min(classica,classineta,caneta)
if min(classica,classineta,caneta)==classica:
    terceiro_lugar="Clássica"
    if primeiro_lugar=="Classineta":
        segundo_lugar="Caneta"
    elif primeiro_lugar=="Caneta":
        segundo_lugar="Classineta"
elif min(classica,classineta,caneta)==classineta:
    terceiro_lugar="Classineta"
    if primeiro_lugar=="Clássica":
        segundo_lugar="Caneta"
    elif primeiro_lugar=="Caneta":
        segundo_lugar="Clássica"
else:
    terceiro_lugar="Caneta"
    if primeiro_lugar=="Clássica":
        segundo_lugar="Classineta"
    elif primeiro_lugar=="Classineta":
        segundo_lugar="Clássica"

pts_segundo=classica+classineta+caneta-pts_primeiro-pts_terceiro

#ranking

print("Estamos calculando... tão rápido quanto dar Run no Dikastis...")
print(f"1º lugar: {primeiro_lugar} ({pts_primeiro} votos)")
print(f"2º lugar: {segundo_lugar} ({pts_segundo} votos)")
print(f"3º lugar: {terceiro_lugar} ({pts_terceiro} votos)")

if primeiro_lugar=="Clássica" and (pts_primeiro-pts_segundo)>=5:
    print("Podemos ver que a influência do grande Hugo Calderano foi disseminada pelos corredores do CIn!")

#prints
