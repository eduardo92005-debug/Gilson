import random
from EP1 import f
TOTAL_PONTOS = 10000
#solution x = -log((3y)/2)/(-log(2) - log(3) + log(5)) for y>0
#x = -log((3*1)/2)/(-log(2) - log(3) + log(5)) for y>0
# eq1: 0.04*20*1.2^(x-1)- y = 0
a = int(input("Insira o intervalo inicial: \t"))
b =  int(input("Insira o intervalo final: \t"))
area = 0
integral = 0
for i in range(TOTAL_PONTOS):
    x = random.uniform(a,b)
    y = random.uniform(a,b)
    func = y - f(x)
    if( func <= 0):
            integral += f(x)
area = ((b-a)/TOTAL_PONTOS)*integral
print("%.1f" % area)

