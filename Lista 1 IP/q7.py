lugar=input()
#input do local
x_cin=500
y_cin=100
x_concha=400
y_concha=500
x_lago=300
y_lago=1000
x_hospital=1000
y_hospital=1000
x_ginasio=800
y_ginasio=100
#coordenadas
dist_concha=(((x_cin-x_concha)**2+(y_cin-y_concha)**2)**0.5)*2
dist_lago=(((x_cin-x_lago)**2+(y_cin-y_lago)**2)**0.5)*2
dist_hospital=(((x_cin-x_hospital)**2+(y_cin-y_hospital)**2)**0.5)*2
dist_ginasio=(((x_cin-x_ginasio)**2+(y_cin-y_ginasio)**2)**0.5)*2
#distancias
tempo_concha=(dist_concha/2)/60+15
tempo_lago=(dist_lago/2)/60+15
tempo_hospital=(dist_hospital/2)/60+15
tempo_ginasio=(dist_ginasio/2)/60+15
#tempos
if lugar=="Concha Acústica da UFPE":
    print(f"Byte visitou {lugar}, caminhou {dist_concha:.0f} metros e gastou {tempo_concha:.0f} minutos passeando!")
    print("Aqui é muito grande mesmo! Muitos eventos ocorrem por aqui!") 
elif lugar=="Laguinho da UFPE":
    print(f"Byte visitou {lugar}, caminhou {dist_lago:.0f} metros e gastou {tempo_lago:.0f} minutos passeando!")
    print("Nossa, mas esse lago é longe hein?!") 
elif lugar=="Hospital das Clínicas":
    print(f"Byte visitou {lugar}, caminhou {dist_hospital:.0f} metros e gastou {tempo_hospital:.0f} minutos passeando!")
    print("Um dos hospitais mais importantes do estado também fica na área do Campus da UFPE!") 
elif lugar=="Ginásio e Pista de Atletismo da UFPE":
    print(f"Byte visitou {lugar}, caminhou {dist_ginasio:.0f} metros e gastou {tempo_ginasio:.0f} minutos passeando!")
    print("Que legal! O Ginásio é bem perto do CIn!") 
