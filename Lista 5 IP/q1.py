#função recursiva da batalha

def batalha(vitalidade_lobo,postura_lobo,cabacas_lobo,vitalidade_genichiro,postura_genichiro,turno):

    #listas de golpes

    golpes_genichiro=["ataque","defesa","recuperação de postura","ataque kanji"]
    golpes_lobo=["ataque","defesa","defesa perfeita","usar cabaça","desviar","contra ataque mikiri"]
    
    # batalha de fato

    print(f"--- Turno {turno} ---")

        #inputs das ações

    acao_genichiro=input()
    if acao_genichiro not in golpes_genichiro:
        while acao_genichiro not in golpes_genichiro:
            print("Genichiro não tem esse movimento em seu arsenal.")
            acao_genichiro=input()
        
    acao_lobo=input()
    if acao_lobo not in golpes_lobo:
        while acao_lobo not in golpes_lobo:
            print("O lobo não adquiriu esse movimento ainda.")
            acao_lobo=input()
        
        #resultados da ações

    if acao_genichiro=="ataque":
        if acao_lobo=="ataque":
            print("Clima de tensão! Os dois atacam numa luta implacável!")
            vitalidade_lobo-=25
            vitalidade_genichiro-=10
            postura_genichiro+=15
        elif acao_lobo=="defesa":
            print("Sekiro firma sua espada e se defende, absorvendo o impacto em sua postura!")
            vitalidade_lobo-=10
            postura_lobo+=20
        elif acao_lobo=="defesa perfeita":
            print("Lâminas se encontram! Um desvio perfeito de Sekiro desequilibra Genichiro!")
            postura_genichiro+=25
        elif acao_lobo=="usar cabaça" and cabacas_lobo>0:
            print("Sekiro tenta curar, mas é punido pelo ataque impiedoso de Genichiro!")
            vitalidade_lobo-=25
            cabacas_lobo-=1
        elif acao_lobo=="usar cabaça" and cabacas_lobo==0:
            print("Sekiro busca sua cabaça, mas ela está vazia!\nEnquanto Sekiro se distrai, Genichiro avança com um ataque certeiro!")
            vitalidade_lobo-=25
        elif acao_lobo=="desviar":
            print("O lobo desvia agilmente do ataque comum de Genichiro!")
        elif acao_lobo=="contra ataque mikiri":
            print("O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro faz um movimento comum.")
            postura_genichiro+=10
        
    elif acao_genichiro=="defesa":
        if acao_lobo=="ataque":
            print("Genichiro prevê o movimento e apara o golpe de Sekiro com sua lâmina!")
            postura_genichiro+=5
        elif acao_lobo=="defesa":
            print("Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.")
        elif acao_lobo=="defesa perfeita":
            print("Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.")
        elif acao_lobo=="usar cabaça" and cabacas_lobo>0:
            print("Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.")
            vitalidade_lobo+=25
            cabacas_lobo-=1
        elif acao_lobo=="usar cabaça" and cabacas_lobo==0:
            print("Sekiro busca sua cabaça, mas ela está vazia!\nGenichiro mantém a guarda, enquanto o lobo percebe seu erro.")
        elif acao_lobo=="desvio":
            print("O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.")
        elif acao_lobo=="contra ataque mikiri":
            print("O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.")
        
    elif acao_genichiro=="recuperação de postura":
        if acao_lobo=="ataque":
            print("Genichiro ia recuperar sua postura mas o lobo foi mais rápido, um grande ataque por parte do lobo!")
            vitalidade_genichiro-=10
            postura_genichiro+=15
        elif acao_lobo=="defesa":
            print("Os guerreiros se encaram, medindo um ao outro. Nenhum avanço.\nGenichiro consegue recuperar sua postura, cuidado lobo!")
            postura_genichiro=0
        elif acao_lobo=="defesa perfeita":
            print("Sekiro se prepara para o desvio, mas Genichiro permanece na defensiva.\nGenichiro consegue recuperar sua postura, cuidado lobo!")
            postura_genichiro=0
        elif acao_lobo=="usar cabaça" and cabacas_lobo>0:
            print("Genichiro hesita! Sekiro aproveita a brecha para usar sua Cabaça Curativa.\nGenichiro consegue recuperar sua postura, cuidado lobo!")
            vitalidade_lobo+=25
            cabacas_lobo-=1
            postura_genichiro=0
        elif acao_lobo=="usar cabaça" and cabacas_lobo==0:
            print("Sekiro busca sua cabaça, mas ela está vazia!\nGenichiro aproveita a hesitação do lobo para recuperar sua postura.\nGenichiro consegue recuperar sua postura, cuidado lobo!")
            postura_genichiro=0
        elif acao_lobo=="desvio":
            print("O lobo tenta prever um possível ataque de Genichiro desviando antecipadamente, mas ele não faz nada.\nGenichiro consegue recuperar sua postura, cuidado lobo!")
            postura_genichiro=0
        elif acao_lobo=="contra ataque mikiri":
            print("O lobo utiliza a técnica de contra-ataque mikiri, mas Genichiro não realizou nenhum movimento de ataque.\nGenichiro consegue recuperar sua postura, cuidado lobo!")
            postura_genichiro=0
    elif acao_genichiro=="ataque kanji":
        if acao_lobo=="contra ataque mikiri":
            print("O lobo utiliza a técnica de contra ataque mikiri e pisa na arma de Genichiro!")
            postura_genichiro+=25
        elif acao_lobo=="desvio":
            print("O lobo desvia do ataque especial de Genichiro com muita agilidade!")
        elif acao_lobo=="usar cabaça" and cabacas_lobo>0:
            print("O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!")
            vitalidade_lobo-=50
            postura_lobo+=20
            cabacas_lobo-=1
        elif acao_lobo=="usar cabaça" and cabacas_lobo==0:
            print("O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!\nPara piorar, Sekiro nem sequer tinha uma cabaça para usar!")
            vitalidade_lobo-=50
            postura_lobo+=20
        else:
            print("O lobo não consegue desviar do ataque especial de Genichiro, foco na batalha lobo!")
            vitalidade_lobo-=50
            postura_lobo+=20

    #casos especiais

    if vitalidade_genichiro<=0 or postura_genichiro>=100:
        turno+=1
        print(f"--- Turno {turno} ---")
        print("Genichiro está de joelhos e vulnerável! Acabe com isso, Lobo!")
        acao_genichiro_golpe_mortal=input()
        if acao_genichiro_golpe_mortal!="ataque":
            print("O lobo hesitou no seu golpe final, Genichiro recupera sua postura! Cuidado, Lobo!")
            if postura_genichiro>=100:
                postura_genichiro=50
                if vitalidade_genichiro<50:
                        vitalidade_genichiro=50
            elif vitalidade_genichiro<=0:
                postura_genichiro=50
                vitalidade_genichiro=50
        else:
            print("Sekiro executa um Golpe Mortal em Genichiro!")
    
    # parte recursiva

    if vitalidade_lobo<=0:
        print("Sekiro cai de joelhos, derrotado...\n====================================\nVitória de Genichiro: Morte.")
        return 
    elif postura_lobo>=100:
        print("A postura do lobo foi quebrada! Ele não consegue se defender e é derrotado!\n====================================\nVitória de Genichiro: Morte.")
        return 
    elif vitalidade_genichiro<=0 or postura_genichiro>=100:
        print("====================================\nVitória de Sekiro: Golpe Mortal!")
        return 
    else:
        turno+=1
        batalha(vitalidade_lobo,postura_lobo,cabacas_lobo,vitalidade_genichiro,postura_genichiro,turno)
        

            
# programa principal

print("O duelo começa! Suas decisões determinarão o vencedor.")
batalha(vitalidade_lobo=100,postura_lobo=0,cabacas_lobo=2,vitalidade_genichiro=100,postura_genichiro=0,turno=1)
