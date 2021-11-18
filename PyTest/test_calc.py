from Functions import umnozhenie, delenie, slozhenie, vichitanie, stepen, koren
# ----------------------------------------------------------------
# Проверка на умножение
def test_umnozhenie_true():
  assert umnozhenie(4, 6) == 24

def test_umnozhenie_false():
  assert umnozhenie(5, 5) == 125
# ----------------------------------------------------------------
# Проверка на деление
def test_delenie_true():
  assert delenie(90, 9) == 10

def test_delenie_false():
  assert delenie(9, 0) == 1
# ----------------------------------------------------------------
# Проверка на сложение
def test_slozhenie_true():
  assert slozhenie(80, 9) == 89

def test_slozhenie_false():
  assert slozhenie(34, 2) == 90
# ----------------------------------------------------------------
# Проверка на вычитание
def test_vichitanie_true():
  assert vichitanie(5, 3) == 2

def test_vichitanie_false():
  assert vichitanie(20, 6) == 15

# -----------------------------------------  
# Проверка степени
def test_stepen_true():
  assert stepen(2, 2) == 4

def test_stepen_false():
  assert stepen(2, 3) == 20
# -----------------------------------------  
# Проверка корня
def test_koren_true():
  assert koren(16) == 4

def test_koren_false():
  assert koren(9) == 2
# -----------------------------------------  
