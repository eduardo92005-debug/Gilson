##### Exercício 06 #####
''' Neste exercício é criado um módulo chamado MinhasCurvas.py
    Todas as funções estão no outro arquivo e não neste.
    Este aquivo principal só testa as funções e no final plota algumas retas.
    A parte do plot está comentada porque não funciona no moodle
    Exemplo de execução deste programa:
    
    exemplo 1:
    
    Testa área (S/N)? S
    Qual reta? 1
    a: 15
    b: 30
    Área: 198.75
    Testa pontos2D (S/N)? N
    
    exemplo 2:
    
    Testa área (S/N)? N
    Testa pontos2D (S/N)? S
    reta: 2
    a: 1
    b: 5
    dist: 0.5
    [1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
    [10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0]

'''
import matplotlib.pyplot as plt
import MeuModulo as MeMo
import MinhasCurvas as mc

option=input('Testa área (S/N)? ')
if option=='S':
    reta = int(input('Qual reta? '))
    a=float(input('a: '))
    b=float(input('b: '))
    print('Área: ',end='')
    if reta ==1:
        print(mc.trapezio_area(mc.reta1,a,b))
    if reta ==2:
        print(mc.trapezio_area(mc.reta2,a,b))
    if reta ==3:
        print(mc.trapezio_area(mc.reta3,a,b))
    if reta ==4:
        print(mc.trapezio_area(mc.reta4,a,b))
        
option=input('Testa pontos2D (S/N)? ')
if option=='S':
    reta=int(input('reta: '))
    a=float(input('a: '))
    b=float(input('b: '))
    dist=float(input('dist: '))
    if reta ==1:
      X,Y = mc.pontos2D(mc.reta1,a,b,dist)
    elif reta ==2:
      X,Y = mc.pontos2D(mc.reta2,a,b,dist)
    elif reta ==3:
      X,Y = mc.pontos2D(mc.reta3,a,b,dist)
    elif reta==4 :
      X,Y = mc.pontos2D(mc.reta4,a,b,dist)
    MeMo.ImprimeListaFloat(X)
    MeMo.ImprimeListaFloat(Y)
    # Plot da reta
    #plt.plot(X,Y,c='red')
    #plt.legend(['reta %d'%reta])
    #plt.grid()
    #plt.show()
    
# Plot de várias retas:
#X1,Y1 = pontos2D(reta1,0,50,5)
#X2,Y2= pontos2D(reta2,0,50,5)
#X3,Y3= pontos2D(reta3,0,50,5)
#X4,Y4= pontos2D(reta4,0,50,5)
#plt.plot(X1,Y1)
#plt.plot(X2,Y2)
#plt.plot(X3,Y3)
#plt.plot(X4,Y4)
#plt.legend(['reta 1','reta 2','reta 3','reta 4'])
#plt.grid()
#plt.show()