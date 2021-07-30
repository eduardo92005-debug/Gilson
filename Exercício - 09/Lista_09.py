import math
##### Exercício 09 #####
'''
    Neste exercício criaremos uma classe de nome Reta.
    A classe Ponto dada em aula também será utilizada, portanto copie no corpo do programa
    O programa principal possui opções e deve ser completado.

    ===== Opções: =====
    0: sair
    1: criar reta
    2: calcula f(x) dado x
    3: calcula área dado intervalo
    4: calcula perpendicular passando por ponto
    5: calcula interseção com outra reta
    6: calcula distância ao ponto

    Exemplo de execução:

    opção: 1
    a: -2
    b: -2
    Reta -2.0x-2.0
    opção: 2
    x: 4
    resultado: -10.0
    opção: 3
    início do intervalo: -5
    final do intervalo: -3
    resultado: 12.0
    opção: 4
    x: 5
    y: -2
    Reta 0.5x-4.5
    opção: 5
    a: 0.5
    b: -4.5
    Ponto em (1.0,-4.0)
    opção: 6
    x: 5
    y: -2
    resultado: 4.5
    opção: 0
'''
##### Classes ######


class Ponto:
    '''
    Atributos:
    x : coordenada no eixo x
    y : coordenada no eixo y

    Métodos:
    dist() : calcula a distância para outro ponto
    '''
    # copie o que foi dado em aula aqui

    def __init__(self, x, y):
    	self.__x = x
    	self.__y = y
     
    def get_x(self):
      return self.__x
    def get_y(self):
      return self.__y
    def textua(self):
      x = self.__x
      y = self.__y
      return "Ponto em (%.1f,%.1f)"%(x,y)

class Reta:
    ''' Coloque a descrição aqui
    '''
    # escreva aqui o construtor:

    def __init__(self, a, b):
      self.__a = a
      self.__b = b
    # getters

    def get_linear(self):
      return self.__b

    def get_angular(self):
      return self.__a

    def validar_sinal(self, b):
      linear = b
      sinal = '+' if linear >= 0 else '-'
      return sinal

    def reta_generica(self):
      angular = self.__a
      linear = self.__b
      sinal = self.validar_sinal(linear)
      abs_linear = abs(linear)
      reta = "Reta %.1fx " % (angular) + sinal + " %.1f" % (abs_linear)
      return reta

    def calc(self):
      x = float(input('x:\t'))
      angular = self.__a
      linear = self.__b
      y = angular*x + linear
      resposta = 'resultado: %.1f' % y
      return resposta

    def area(self):
      x0 = float(input('início do intervalo:\t'))
      x1 = float(input('final do intervalo:\t'))
      angular = self.__a
      linear = self.__b
      y0 = angular*x0 + linear
      y1 = angular*x1 + linear
      A = 0.5*(y1+y0)*(x1 - x0)
      return A

    def perpendicular(self, P):
      angular = self.__a
      angular_p = - (1/angular)
      x_p = P.get_x()
      y_p = P.get_y()
      linear_p = y_p - angular_p*x_p
      gera_reta = Reta(angular_p, linear_p)
      reta = gera_reta.reta_generica()
      return reta
      
    def intersec(self, r):
      linear_s = self.__b
      angular_s = self.__a
      angular_r = r.get_angular()
      linear_r = r.get_linear()
      x_i = (linear_s - linear_r)/(angular_r - angular_s)
      y_i = angular_s*x_i + linear_s
      ponto = Ponto(x_i,y_i)
      return ponto.textua()
    def dist(self,P):
      linear = self.__b
      angular = self.__a
      xb = P.get_x()
      yb = P.get_y()
      xa = 1
      ya = abs(angular*xa + linear)
      dist = math.sqrt((xb - xa)**2 + (yb - ya)**2)
      resposta = "resultado: %.1f"%dist
      return resposta
      	
      	
     	

    
    # escreva aqui a representação para o print
    
    # escreva aqui os demais métodos

##### principal: #####

while True:
  global r
  global p
  opcao=input('opção: ')
  try:
    opcao=int(opcao)
    if opcao==1:
      # criar reta
      a=float(input('a:\t'))
      b=float(input('b:\t'))
      r = Reta(a,b)
      generica = r.reta_generica()
      print(generica)
    elif opcao==2:
      calc = r.calc()
      print(calc)
    elif opcao==3:
      # calcula área dado intervalo
      area = r.area()
      print(area)
    elif opcao==4:
      # calcula perpendicular passando por ponto
      x = float(input('x:\t'))
      y = float(input('y:\t'))
      ponto = Ponto(x,y)
      reta_p = r.perpendicular(ponto)
      print(reta_p)
    elif opcao==5:
      # calcula interseção com outra reta
      #cria reta de interseccao
      a=float(input('a:\t'))
      b=float(input('b:\t'))
      reta_intersectadora = Reta(a,b)
      intersecta = r.intersec(reta_intersectadora)
      print(intersecta)
    elif opcao==6:
      # calcula distância ao ponto
      x = float(input('x:\t'))
      y = float(input('y:\t'))
      p = Ponto(x,y)
      distancia = r.dist(p)
      print(distancia)
    elif opcao==0:
      break
    else:
      print('A opção não é válida.')
      
  except:
    print('===== Opções: =====')
    print('0: sair')
    print('1: criar reta')
    print('2: calcula f(x) dado x')
    print('3: calcula área dado intervalo')
    print('4: calcula perpendicular passando por ponto')
    print('5: calcula interseção com outra reta')
    print('6: calcula distância ao ponto')
