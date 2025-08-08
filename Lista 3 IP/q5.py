recurso=""
roda=[]
qualidade_roda=[]
chassi=[]
qualidade_chassi=[]
volante=[]
qualidade_volante=[]
doces_descartados=[]
rei_doce=False


#variável de recurso e listas iniciais


while recurso!="Recursos Esgotados": #laço dos recursos
    recurso=input()
    if recurso=="O REI DOCE ESTÁ ROUBANDO TODOS OS INGREDIENTES!": #roubo dos doces
        rei_doce=True
        if len(roda)>0:
            doces_descartados.append(roda[0]) #adição na lista de descartados
        if len(chassi)>0:
            doces_descartados.append(chassi[0]) #adição na lista de descartados
        if len(volante)>0:
            doces_descartados.append(volante[0]) #adição na lista de descartados
        roda=[] #limpeza da lista
        qualidade_roda=[] #limpeza da lista 
        chassi=[] #limpeza da lista
        qualidade_chassi=[] #limpeza da lista
        volante=[] #limpeza da lista
        qualidade_volante=[] #limpeza da lista
    elif recurso!="Recursos Esgotados":
        separacao=recurso.split('-') #separação dos elementos do input para análise
        separacao[0]=separacao[0].rstrip()
        separacao[1]=separacao[1].lstrip()
        if "estragado" in separacao[1]: #verificação de doce estragado
            doces_descartados.append(separacao[0])
        elif "Mentos" in separacao[0] or "Jujuba" in separacao[0]: #análise se for um doce para roda
            if len(roda)>0: #condicional de análise quando já existe um elemento na lista
                if "alta qualidade" in separacao[1] and not "alta qualidade" in qualidade_roda[0]: #verificação de qualidade
                    doces_descartados.append(roda[0])
                    roda=[]
                    qualidade_roda=[]
                    roda.append(separacao[0]) #adição do doce 
                    qualidade_roda.append(separacao[1]) #adição da qualidade do doce 
                else: #caso de doce mediano se a lista já tiver algo
                    doces_descartados.append(separacao[0])
            elif len(roda)==0: #condicional se a lista estiver vazia
                roda.append(separacao[0]) #adição do doce 
                qualidade_roda.append(separacao[1]) #adição da qualidade do doce 
        elif "Bolo de rolo" in separacao[0] or "Barra de chocolate" in separacao[0] or "Banda de ovo de Páscoa" in separacao[0]: #análise se for um doce para chassi
            if len(chassi)>0: #condicional de análise quando já existe um elemento na lista
                if "alta qualidade" in separacao[1] and not "alta qualidade" in qualidade_chassi[0]: #verificação de qualidade
                    doces_descartados.append(chassi[0])
                    chassi=[]
                    qualidade_chassi=[]
                    chassi.append(separacao[0]) #adição do doce 
                    qualidade_chassi.append(separacao[1]) #adição da qualidade do doce 
                else: #caso de doce mediano se a lista já tiver algo
                    doces_descartados.append(separacao[0])
            elif len(chassi)==0: #condicional se a lista estiver vazia
                chassi.append(separacao[0]) #adição do doce 
                qualidade_chassi.append(separacao[1]) #adição da qualidade do doce 
        elif "Pretzel" in separacao[0] or "Donuts" in separacao[0]: #análise se for um doce para volante
            if len(volante)>0: #condicional de análise quando já existe um elemento na lista
                if "alta qualidade" in separacao[1] and not "alta qualidade" in qualidade_volante[0]: #verificação de qualidade
                    doces_descartados.append(volante[0])
                    volante=[]
                    qualidade_volante=[]
                    volante.append(separacao[0]) #adição do doce da roda
                    qualidade_volante.append(separacao[1]) #adição da qualidade do doce 
                else: #caso de doce mediano se a lista já tiver algo
                    doces_descartados.append(separacao[0])
            elif len(volante)==0: #condicional se a lista estiver vazia
                volante.append(separacao[0]) #adição do doce 
                qualidade_volante.append(separacao[1]) #adição da qualidade do doce 

#laço da montagem do carro

print("Vamos lá, Vanellope! Vou te ajudar a montar um carro CINistro!")
if rei_doce:
    print("Ah não!! Ele vai destruir seu carro, Vanellope! CUIDADO")
if len(roda)>0 and len(chassi)>0 and len(volante)>0 and "qualidade mediana" in qualidade_roda and "qualidade mediana" in qualidade_chassi and "qualidade mediana" in qualidade_volante:
    print("Pelo menos anda! Você consegue!")
elif len(roda)>0 and len(chassi)>0 and len(volante)>0 and ("alta qualidade" in qualidade_roda or "alta qualidade" in qualidade_chassi or "alta qualidade" in qualidade_volante):
    print("Conseguimos! Impossível você não ganhar essa corrida, Vanellope!") 
    print(f"Para fazer o carro você utilizou {chassi[0]} para ser a estrutura do carro, {volante[0]} para o volante, {roda[0]} para compor as rodas!")
elif len(roda)==0 or len(chassi)==0 or len(volante)==0:
    print("Sinto muito, Vanellope. Não consegui te ajudar dessa vez.")

#prints do resultado do carro

if len(doces_descartados)>0:
    print(f"Alguns doces foram descartados. São eles:")
    print(f"{', '.join(doces_descartados)}")

