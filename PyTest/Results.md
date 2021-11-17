Результаты тестирования:

 pytest testrunner.py
============================= test session starts ==============================
platform linux -- Python 3.8.12, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: /home/runner/Pytest
collected 12 items                                                             

testrunner.py .F.F.F.F.F.F                                               [100%]

=================================== FAILURES ===================================
____________________________ test_umnozhenie_false _____________________________

    def test_umnozhenie_false():
>     assert umnozhenie(5, 5) == 125
E     assert 25 == 125
E      +  where 25 = umnozhenie(5, 5)

testrunner.py:35: AssertionError
______________________________ test_delenie_false ______________________________

    def test_delenie_false():
>     assert delenie(9, 0) == 1
E     AssertionError: assert 'Делитель должен быть больше нуля' == 1
E      +  where 'Делитель должен быть больше нуля' = delenie(9, 0)

testrunner.py:42: AssertionError
_____________________________ test_slozhenie_false _____________________________

    def test_slozhenie_false():
>     assert slozhenie(34, 2) == 90
E     assert 36 == 90
E      +  where 36 = slozhenie(34, 2)

testrunner.py:49: AssertionError
____________________________ test_vichitanie_false _____________________________

    def test_vichitanie_false():
>     assert vichitanie(20, 6) == 15
E     assert 14 == 15
E      +  where 14 = vichitanie(20, 6)

testrunner.py:56: AssertionError
______________________________ test_stepen_false _______________________________

    def test_stepen_false():
>     assert stepen(2, 3) == 20
E     assert 8 == 20
E      +  where 8 = stepen(2, 3)

testrunner.py:64: AssertionError
_______________________________ test_koren_false _______________________________

    def test_koren_false():
>     assert koren(9) == 2
E     assert 3.0 == 2
E      +  where 3.0 = koren(9)

testrunner.py:71: AssertionError
=========================== short test summary info ============================
FAILED testrunner.py::test_umnozhenie_false - assert 25 == 125
FAILED testrunner.py::test_delenie_false - AssertionError: assert 'Делитель д...
FAILED testrunner.py::test_slozhenie_false - assert 36 == 90
FAILED testrunner.py::test_vichitanie_false - assert 14 == 15
FAILED testrunner.py::test_stepen_false - assert 8 == 20
FAILED testrunner.py::test_koren_false - assert 3.0 == 2
========================= 6 failed, 6 passed in 0.28s ==========================
exit status 1
