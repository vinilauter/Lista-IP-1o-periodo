dia=input()
turno=input()
if dia=="segunda-feira" or dia=="sexta-feira":
    hora=int(input())
local=input()
humor=input()
#dados
if dia=="segunda-feira" and hora<=7:
    print("Byte acordou em plena madrugada, quem tá acordado(a) pra levar ele essa hora?!")
if dia=="sexta-feira" and hora>=16:
    print("SEXTOU, quem vai levar Byte pra bater pata por aí??")
if local=="labirinto":
    print("Byte quer passear num labirinto, cuidado pra não se perder!")
if humor=="pura energia":
    print("Byte está energizado com a ideia de passear, leve uma bolinha pra ele!")
if humor=="calminho":
    print("Byte está calminho, o passeio vai ser na paz, pode confiar!")
if humor=="rebelde":
    print("Byte está se comportando mal hoje, vamos ver quem terá coragem para acompanhá-lo em seu passeio")
if local=="labirinto" and humor!="rebelde":
    print("A prof. Fernanda Madeiral aceitou o desafio: labirinto caótico, uma Python no caminho… e Byte como companheiro. Afinal, o que pode dar errado?")
if local=="labirinto" and humor=="rebelde":
    print("Mestre Iyoda e Byte adentram o labirinto. Uma missão ousada e um destino desconhecido.") 
if local!="labirinto" and turno=="manhã" and dia!="segunda-feira":
    print(f"Nesta manhã de {dia}, é o Prof. Sergio Soares quem comanda o passeio com Byte")
if local!="labirinto" and turno== "manhã" and dia=="segunda-feira":
    print(f"{dia}: uns indo pro trabalho, outros lidando com o Byte. Prof. Ricardo Massa escolheu a segunda opção. Força, guerreiro. {local}, aí vamos nós.")
if turno=="tarde" and local!="labirinto":
    print("Sol da tarde, coleira na mão: prof. Ricardo Massa entra em cena para o passeio com Byte.")
if turno=="noite" and local=="parque":
    print(f"Quando a noite cai e Byte chama, Mestre Iyoda atende. Que o {local} esteja preparado para essa dupla!")
if turno=="noite" and local=="bosque":
    print(f"Quando a noite cai e Byte chama, Mestre Iyoda atende. Que o {local} esteja preparado para essa dupla!")


