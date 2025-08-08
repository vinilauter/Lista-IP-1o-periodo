fatorial=1
print("🎾🏆 Bem-vindo ao Torneio Fatorial Ping Pong Championship! 🧮🏓")
print("Hoje, o jovem Lavoi enfrentará seu maior desafio: CÁLCULOS!")
print()

#prints iniciais

print("Qual será o número que marcará o INÍCIO dessa tabuada fatorial?")
nmr_inicio=int(input())
if nmr_inicio>=0:
    print(f"O número {nmr_inicio} é ótimo como número inicial!")
else:
    while nmr_inicio<0:
        print(f"O número {nmr_inicio} é inválido! O INÍCIO NÃO pode ser NEGATIVO.")
        nmr_inicio=int(input())
        if nmr_inicio>=0:
            print(f"O número {nmr_inicio} é ótimo como número inicial!")
print()

#valor inicial

print("Qual será o número que marcará o FIM dessa tabuada fatorial?")
nmr_fim=int(input())
if nmr_fim>=nmr_inicio:
    print(f"O número {nmr_fim} é ótimo como número final!")
else:
    while nmr_fim<nmr_inicio:
        print(f"O número {nmr_fim} é inválido! O FIM NÃO pode ser MENOR que o número inicial {nmr_inicio}.")
        nmr_fim=int(input())
        if nmr_fim>=nmr_inicio:
            print(f"O número {nmr_fim} é ótimo como número final!")
print()

#valor final

print("Qual será o número cujo FATORIAL será calculado?")
nmr_sagrado=int(input())
if nmr_sagrado>=0:
    print(f"O número {nmr_sagrado} é ótimo para o cálculo do fatorial!")
else:
    while nmr_sagrado<0:
        print(f"O número {nmr_sagrado} é inválido! Números válidos são maiores ou iguais a zero.")
        nmr_sagrado=int(input())
        if nmr_sagrado>=0:
            print(f"O número {nmr_sagrado} é ótimo para o cálculo do fatorial!")
print()

#número sagrado

for estagio in range(nmr_inicio,nmr_fim + 1):
    valor=estagio*nmr_sagrado
    for i in range(1,valor+1):
        fatorial*=i
    print(f"({estagio} * {nmr_sagrado})! = {fatorial}")
    fatorial=1

#laço do fatorial

print()
print("🏁 Jornada Finalizada! Lavoi completou todos os estágios do desafio!")
print("🏓 Que sua energia vital continue brilhando nas próximas batalhas!")