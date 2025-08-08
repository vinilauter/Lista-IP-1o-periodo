num_1=int(input())
num_2=int(input())
num_3=int(input())
num_4=int(input())
num_5=int(input())
resultado=(num_1+num_2+num_3+num_4+num_5)%5
if resultado==0:
    monitor="Arthur"
elif resultado==1:
    monitor="Bruna"
elif resultado==2:
    monitor="César"
elif resultado==3:
    monitor="Daniel"
elif resultado==4:
    monitor="Eduarda"
print(f"{monitor} vai ter a honra de passear com Byte hoje!")