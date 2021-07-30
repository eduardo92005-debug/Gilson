import numpy as np
'''
Módulo MinhasCurvas
Este módulo contém funções para funções lineares (retas) do exercício 06 da lista
Além das funções do enunciado você pode colocar outras funções auxiliares se achar necessário
'''
def reta_generica(x,a=0,b=0):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  reta =  a*x + b
  f_x = reta
  return f_x

def reta1(x):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  reta = reta_generica(x, a = 0.5, b = 2)
  f_x = reta
  return f_x

def reta2(x):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  reta = reta_generica(10,a = 1,b = 0)
  f_x = reta
  return f_x

def reta3(x):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  reta = reta_generica(x, a=-1.5, b=50)
  f_x = reta
  return f_x

def reta4(x):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  reta = reta_generica(x, a=1.5, b=-50)
  f_x = reta
  return f_x
  
def trapezio_area(f,a,b):
  '''Escreva aqui a descrição'''
  #escreva aqui a função - cuidado com valores negativos
  cortes = 50 #iteracoes
  x = np.linspace(a, b, cortes + 1)
  y = f(x)
  y_dir = y[1:]
  y_esq = y[:-1]
  infinitesimal = (b - a) / cortes
  area = (infinitesimal / 2) * np.sum(y_dir + y_esq)
  return area
  
def pontos2D(f,a,b,dist):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  a = int(a)
  b = int(b)
  v = a
  x = [v]
  y = []
  for i in range(a,2*b - 1):
    v = v + dist
    x.append(v)
  for num in x:
    yi = f(num)
    y.append(yi)
  return x,y
