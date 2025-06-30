mediahora_arthur=int(input())
mediahora_luiz=int(input())
mediahora_pedro=int(input())
horas_competição=int(input())
#dados brutos da competição
diamantes_arthur=mediahora_arthur*horas_competição
diamantes_luiz=mediahora_luiz*horas_competição
diamantes_pedro=mediahora_pedro*horas_competição
#cálculo do total de diamantes de cada
max_arthur_luiz= int((diamantes_arthur + diamantes_luiz +abs(diamantes_arthur - diamantes_luiz)) / 2)
max_total=int((max_arthur_luiz + diamantes_pedro + abs(diamantes_pedro - max_arthur_luiz)) / 2)
print(max_total)