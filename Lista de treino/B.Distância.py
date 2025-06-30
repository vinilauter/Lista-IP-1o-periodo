x_hogs=34
z_hogs=220
#coord Hogsmeade
x_kakariko=0
z_kakariko=0
#coord Kakariko
x_solitude=140
z_solitude=456
#coord Solitude
x_atual=int(input())
z_atual=int(input())
#coord atual
dist_hogs=((x_hogs-x_atual)**2 + (z_hogs-z_atual)**2)**0.5
dist_kakariko=((x_kakariko-x_atual)**2 + (z_kakariko-z_atual)**2)**0.5
dist_solitude=((x_solitude-x_atual)**2 + (z_solitude-z_atual)**2)**0.5
print ("Distância para Hogsmeade:{:.2f}".format(dist_hogs))
print ("Distância para Hogsmeade:{:.2f}".format(dist_kakariko))
print ("Distância para Hogsmeade:{:.2f}".format(dist_solitude))
