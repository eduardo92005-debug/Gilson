import random
'''
Indice de reprodutibilidade do virus = 1.2
4% dos pacientes irão precisar de UTI
Função infectados i(x) = I0 * r**(x-1)
I0 = número de infectados inicial
r = indice de reprodutibilidade
i(x) = total de infectados
'''


#solution x = -log((3y)/2)/(-log(2) - log(3) + log(5)) for y>0
#x = -log((3*1)/2)/(-log(2) - log(3) + log(5)) for y>0
# eq1: 0.04*20*1.2^(x-1)- y = 0
def integral_carlo(a,b):
    TOTAL_PONTOS = 1000000
    area = 0
    integral = 0
    for i in range(TOTAL_PONTOS):
        x = random.uniform(a,b)
        y = random.uniform(a,b)
        func = y - f(x)
        if( func <= 0):
                integral += f(x)
    area = ((b-a)/TOTAL_PONTOS)*integral
    return area


def test_propagation():
    i0 = int(input("Insira o número inicial de infectados: \t"))
    r = float(input("Insira o indice de reprodutibilidade do virus no momento: \t"))
    x = int(input("Insira a quantidade de dias: \t"))
    i_x = i0 * r**(x-1)
    def testing(initial, reproductible, x, i_x):
        print(' === Teste da função de propagação ===')
        print('infectados inicial: %d'% i0)
        print('índice de reprodutibilidade: %.0f'% r)
        print('dia: %d'% x)
        print('resultado: %.1f'% i_x)
    testing(i0,r,x,i_x)
def f(x):
    #percentagem de infectados que podem precisar de uti
    p = 0.04
    i0 = 20
    r = 1.2
    if(x <= 15):
        func_x =  p * i0 * r**(x-1)
        return func_x
    else:
        func_x =  p * i0 * r**(x-1) - f(x-15)
        return func_x

def test_utiusers():
    dia = int(input("Insira a quantidade de dias: \t"))
    test_f_x = f(dia)
    def testing():
        print(" === Calculo de pacientes para UTI ===")
        print("dia: %d" % dia)
        print("resultado: %.1f" % test_f_x)
    testing()

def test_curva():
    a = int(input("Insira o intervalo inicial: \t"))
    b =  int(input("Insira o intervalo final: \t"))
    area = integral_carlo(a,b)
    def testing():
        print(' === Cálculo da área sob a curva ===')
        print('inicio do intervalo: %d' % a)
        print('final do intervalo: %d'% b)
        print('resultado: %.1f' % area)
    testing()

def test_leitos():
    leitos_inicial = int(input("Insira a quantidade inicial de leitos: \t"))
    leitos_providenciar =  integral_carlo(1,30) - leitos_inicial
    def testing():
        print('=== Cálculo de leitos necessários ===')
        print('resultado: %.0f' %leitos_providenciar)
    testing()


    



    
if __name__ == '__main__':
    #test_utiusers()
    #test_propagation()
    #test_curva()
    test_leitos()
