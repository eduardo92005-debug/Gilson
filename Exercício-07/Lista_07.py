##### Exercício 07 #####
'''
    Neste exercício é utilizado um módulo chamado MinhasCurvas.py
    Todas as funções estão no outro arquivo e não neste.
    Este aquivo principal só testa as funções.
    Não tem plot, mas se quiser visualizar pode usar os mesmos passos do exercício passado
    Exemplo de execução deste programa:
    
    exemplo 1:
    
    Testa parábola (S/N)? S
    Qual parábola? 1
    x: 0
    -18.00
    Testa área (S/N)? N
    
    exemplo 2:
    
    Testa parábola (S/N)? N
    Testa área (S/N)? S
    Qual parabola? 1
    a: 0
    b: 5
    dx: 0.1
    Área: 65.33
'''
import MinhasCurvas as mc

option=input('Testa parábola (S/N)? ')
if option=='S':
    p = int(input('Qual parábola? '))
    if p ==1:
        x=float(input('x: '))
        print('%.2f'%mc.parabola1(x))
    elif p ==2:
        x=float(input('x: '))
        print('%.2f'%mc.parabola2(x))
    elif p ==3:
        x=float(input('x: '))
        print('%.2f'%mc.parabola3(x))
        
option=input('Testa área (S/N)? ')
if option=='S':
    p = int(input('Qual parabola? '))
    a=float(input('a: '))
    b=float(input('b: '))
    dx=float(input('dx: '))
    print('Área: ',end='')
    if p ==1:
        print('%.2f'%mc.mt_area(mc.parabola1,a,b,dx))
    elif p ==2:
        print('%.2f'%mc.mt_area(mc.parabola2,a,b,dx))
    elif p ==3:
        print('%.2f'%mc.mt_area(mc.parabola3,a,b,dx))