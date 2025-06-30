nome_aluno=input()
acertos_lista1=int(input())
acertos_lista2=int(input())
acertos_lista3=int(input())
questoes_lista4=int(input())
questoes_lista5=int(input())
questoes_lista6=int(input())
acertos_lista4=questoes_lista4*10/6
acertos_lista5=questoes_lista5*10/6
acertos_lista6=questoes_lista6*10/6
contador=0
#dados
media_geral=(acertos_lista1+acertos_lista2+acertos_lista3+acertos_lista4+acertos_lista5+acertos_lista6)/6
#cálculo da média
print("A média de "+nome_aluno+" é " f"{media_geral:.1f}")
if acertos_lista1<=acertos_lista2<=acertos_lista3<=acertos_lista4<=acertos_lista5<=acertos_lista6:
    print("Progresso constante! Parabéns pelo esforço!")
else: 
    print("Alerta! Queda no rendimento.")
if acertos_lista1==0:
    contador+=1
if acertos_lista2==0:
    contador+=1
if acertos_lista3==0:
    contador+=1
if acertos_lista4==0:
    contador+=1
if acertos_lista5==0:
    contador+=1
if acertos_lista6==0:
    contador+=1
if contador>=2:
    print ("Alerta! Múltiplas listas não respondidas.")
if media_geral>=8:
    print('Parabéns pelo excelente desempenho! Continue "au" sim.')
elif media_geral<8 and media_geral>=7:
    print("Parabéns pelo bom desempenho!")
else: 
    print("Alerta! Desempenho abaixo do esperado.")
#outputs

