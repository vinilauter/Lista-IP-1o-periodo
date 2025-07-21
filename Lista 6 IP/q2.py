# variáveis iniciais

jogador=""
dados_jogadores={}
qtd_atletas_prontos=0
qtd_mei_def_prontos=0

# loop recebimento de jogador

while jogador!="FIM":
    jogador=input()
    if jogador!="FIM":
        dados_jogadores[jogador]={}

        dados_jogadores[jogador]["disposicao"]=int(input())

        dados_jogadores[jogador]["posicao"]=input()
    
        if dados_jogadores[jogador]["disposicao"]>=85:

            dados_jogadores[jogador]["desempenho"]=int(input())

            if dados_jogadores[jogador]["posicao"]=="atacante":

                if dados_jogadores[jogador]["desempenho"]>10:
                    print(f"{jogador} está com um bom desempenho ofensivo.")
                    qtd_atletas_prontos+=1
                else:
                    print(f"{jogador} pode melhorar, Ancelotti pode usá-lo no segundo tempo.")

            else:

                if dados_jogadores[jogador]["desempenho"]>=20:
                    print(f"{jogador} está com um bom desempenho de passes.")
                    qtd_mei_def_prontos+=1

                else:
                    print(f"{jogador} pode melhorar, Ancelotti pode não colocá-lo no primeiro tempo.")

        elif dados_jogadores[jogador]["disposicao"]<85 and dados_jogadores[jogador]["disposicao"]>=50:

            dados_jogadores[jogador]["desempenho"]=int(input())

            if dados_jogadores[jogador]["desempenho"]>80:
                print(f"O jogador {jogador} pode ser escalado para a próxima partida.")
                if  dados_jogadores[jogador]["posicao"]=="atacante":
                    qtd_atletas_prontos+=1
                else:
                    qtd_mei_def_prontos+=1

            else:
                print(f"Ancelotti precisa analisar o desempenho do {jogador} na partida.")

        else:

            dados_jogadores[jogador]["desempenho"]=int(input())

            if dados_jogadores[jogador]["desempenho"]>70:
                print(f"Ancelotti deve colocar {jogador} para treinar mais.")
                
            else:
                print(f"{jogador} não deveria estar na próxima convocação.")

# relatório da comissão técnica

print()
print("Relatório dos jogadores:")
qtd_jogadores=len(dados_jogadores)
print(f"Total de jogadores analisados: {qtd_jogadores}")
print(f"Atacantes prontos para começar: {qtd_atletas_prontos}")
print(f"Meio-campistas e Defensores prontos para começar: {qtd_mei_def_prontos}")