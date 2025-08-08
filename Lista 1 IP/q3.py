valor_mensal_dolar=int(input())
cotacao_dolar=float(input())
valor_mensal_reais=valor_mensal_dolar*cotacao_dolar
gasto_racao=int(input())
gasto_aluguel=int(input())
gasto_bus=int(input())
saldo_final=valor_mensal_reais-gasto_aluguel-gasto_racao-gasto_bus
#dados
if saldo_final==0:
    print ("Vai dar pra alugar sua casa, mas sugiro que você vá trabalhar se quiser gastar com outra coisa!")
elif saldo_final>0:
    print ("Me chama pra sua casa um dia pra gente comer Pedigree! Com essa grana dá pra alugar uma ManCão!")
elif saldo_final<0:
    print("Eu acho melhor você ir morar comigo no Cin! O RU é só 4 reais e lá no DA tem saco de dormir!")
#output de saldo
if gasto_racao>gasto_aluguel and gasto_racao>gasto_bus:
    print("A inflaCão deu pros cachorros, viu! Sugiro que você vá no Coffee Break dos calouros e leve toda a comida!")
    maior_gasto="Ração"
elif gasto_aluguel>gasto_racao and gasto_aluguel>gasto_bus:
    print("Não está fácil pra ninguém... Tenta dividir o aluguel com algum estudante aí!")
    maior_gasto="Aluguel"
elif gasto_bus>gasto_aluguel and gasto_bus>gasto_racao:
    print("Você consegue voar, por que quer orçamento de ônibus? Vai ser feliz!")
    maior_gasto="Ônibus"
#output do maior gasto
print(f"MESADA (dólares): {valor_mensal_dolar:.2f} dólares")
print(f"MESADA (reais): {valor_mensal_reais:.2f} reais")
print(f"MAIOR GASTO: {maior_gasto}")
      