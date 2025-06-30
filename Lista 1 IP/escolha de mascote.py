cao_vencedor="indefinido"
nome_cao1=input()
cao1_pont_prova_1=int(input())
cao1_pont_prova_2=int(input())
cao1_pont_prova_3=int(input())
cao1_total=cao1_pont_prova_1+cao1_pont_prova_2+cao1_pont_prova_3
if nome_cao1=="Byte" or nome_cao1=="byte":
    cao_vencedor=nome_cao1
    print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
elif cao1_total==30: 
    cao_vencedor=nome_cao1
    print(f"Com uma pontuação perfeita, {cao_vencedor} conquista o título de mascote do CIn!")
if cao_vencedor=="indefinido":
  nome_cao2=input()
  cao2_pont_prova_1=int(input())
  cao2_pont_prova_2=int(input())
  cao2_pont_prova_3=int(input())
  cao2_total=cao2_pont_prova_1+cao2_pont_prova_2+cao2_pont_prova_3
  if nome_cao2=="Byte" or nome_cao2=="byte":
    cao_vencedor=nome_cao2
    print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
  elif cao_vencedor=="indefinido": 
    if cao2_total==30: 
      cao_vencedor=nome_cao2
      print(f"Com uma pontuação perfeita, {cao_vencedor} conquista o título de mascote do CIn!")
if cao_vencedor=="indefinido":
  nome_cao3=input()
  cao3_pont_prova_1=int(input())
  cao3_pont_prova_2=int(input())
  cao3_pont_prova_3=int(input())
  cao3_total=cao3_pont_prova_1+cao3_pont_prova_2+cao3_pont_prova_3
  if nome_cao3=="Byte" or nome_cao3=="byte":
    cao_vencedor=nome_cao3
    print("Byte está na disputa! Não há dúvidas, o novo mascote do CIn é ele mesmo!")
  elif cao_vencedor=="indefinido": 
    if cao3_total==30: 
      cao_vencedor=nome_cao3
      print(f"Com uma pontuação perfeita, {cao_vencedor} conquista o título de mascote do CIn!") #dados cachorro 3
  if cao1_total<15:
    print(f"Infelizmente {nome_cao1} está fora da disputa")
  if cao2_total<15:
    print(f"Infelizmente {nome_cao2} está fora da disputa")
  if cao3_total<15:
    print(f"Infelizmente {nome_cao3} está fora da disputa")
  if cao1_total>cao2_total and cao1_total>cao3_total:
    print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_cao1}!")
  if cao1_total<cao2_total and cao2_total>cao3_total:
    print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_cao2}!")
  if cao3_total>cao2_total and cao1_total<cao3_total:
    print(f"Após uma disputa acirrada, o novo mascote do CIn é {nome_cao3}!")
