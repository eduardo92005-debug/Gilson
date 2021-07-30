'''
Módulo MinhasCurvas
Este módulo contém funções para funções do exercício 07 da lista
Além das funções do enunciado você pode colcar outras funções auxiliares se achar necessário
'''
import numpy as np

def parabola_generica(x,a=0,b=0,c=0):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  parabola =  a*(x**2) + b*x + c
  f_x = parabola
  return f_x

def parabola1(x):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  parabola = parabola_generica(x,a = 2, b = 0, c = -18)
  f_x = parabola
  return f_x

def parabola2(x):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  parabola = parabola_generica(x,a = 1, b = 4, c = 10)
  f_x = parabola
  return f_x

def parabola3(x):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  parabola = parabola_generica(x,a = -2, b = 20, c = -50)
  f_x = parabola
  return f_x
  
def mt_area(f,a,b,dx):
  '''Escreva aqui a descrição'''
  #escreva aqui a função
  N = 1000
  x = np.linspace(a,b,N+1) # N+1 points make N subintervals
  y = f(x)
  trapz = np.trapz(y,x,dx)*10
  return trapz


  
