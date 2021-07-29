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
    def __init__(self,x,y):
    	self.__x = x
    	self.__y = y
    def dist(self):
    	xb = float(input('x:\t'))
    	yb = float(input('y:\t'))
    	xa = self.__x
    	ya = self.__y
    	dist = sqrt((xb - xa)**2 + (yb - ya)**2)
    	resposta = "resultado: %.1f"%dist
    	return resposta
    
class Reta:
    ''' Coloque a descrição aqui
    '''
    # escreva aqui o construtor:
    def __init__(self, a, b):
      self.__a = a
      self.__b = b
    #getters
    def get_linear(self):
      return self.__b
    def get_angular(self):
      return self.__a
    def validar_sinal(self,b):
      linear = b
      sinal = '+' if linear >= 0 else '-'
      return sinal
    def reta_generica(self):
      angular = self.__a
      linear = self.__b
      sinal = self.validar_sinal(linear)
      reta = "Reta %.1fx "%(angular) + sinal + " %.1f"%(linear)
      return reta
      
    def calc(self,x):
      x = float(input('x:\t'))
      angular = self.__a
      linear = self.__b
      y = angular*x + linear
      resposta = 'resultado: %.1f'%y
      return resposta
      
    def area(self):
      x0 = float(input('início do intervalo:\t'))
      x1 = float(input('final do intervalo:\t'))
      angular = self.__a
      linear = self.__b
      b = x1 - x0
      h = angular * b
      y0 = angular*x0 + linear
      y1 = angular*x1 + linear
      A = 0.5*(y1+y0)*(x1 - x0)
      return A
      
     def perpendicular(self):
       angular = self.__a
       linear  = self.__b
       mr = -angular/linear
       mp = -1/(mr)
       x = float(input('x:\t')))
       y = float(input('y:\t'))
       b = 1
       c = -(mp*x + b*y)
       linearp= c/b
       sinal = self.validar_sinal(linear)
       reta = "Reta %.1fx "%(mp) + sinal + " %.1f"%(linearp)
       return reta
      
      def intersec(self):
      	a_r = float(input('a:\t'))
      	b_r = float(input('b:\t'))
      	angular_s = self.__a
      	linear_s = self.__b
      	x = (linear_s - b_r)/(angular_s - a_r)
      	y = angular_s*x + linear_s
      	ponto = "Ponto em (%.1f,%.1f)"%(x,y)
      	return ponto
      	
      	
     	

    
    # escreva aqui a representação para o print
    
    # escreva aqui os demais métodos

##### principal: #####

while True:
  r = 0
  opcao=input('opção: ')
  try:
    opcao=int(opcao)
    if opcao==1:
      # criar reta
      a=float(input('a:\t'))
      b=float(input('b:\t'))
      r=Reta(a,b)
      print(r.reta_generica())
    elif opcao==2:
      print(r.calc())
    elif opcao==3:
      # calcula área dado intervalo
      a=float(input('a:\t'))
      b=float(input('b:\t'))
      r=Reta(a,b)
      print(r.area())
      pass
    elif opcao==4:
      # calcula perpendicular passando por ponto
      pass 
    elif opcao==5:
      # calcula interseção com outra reta
      pass
    elif opcao==6:
      # calcula distância ao ponto
      pass
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
