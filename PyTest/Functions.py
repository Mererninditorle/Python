import pytest
import math

# Обозначение функций:
def umnozhenie(a, b):
  return a * b

def delenie(a, b):
  if b == 0:
    return ("Делитель должен быть больше нуля")
    print("Делитель должен быть больше нуля")
  else:
    return a / b

def slozhenie(a, b):
    return a + b

def vichitanie(a, b):
    return a - b

def stepen(a, b):
  if (b == 0):
    return 1
  else:
    return a ** b

def koren(a):
  return math.sqrt(a)
