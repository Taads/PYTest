import calculadora
import pytest

def test_soma():
    assert calculadora.soma(1, 2) == 3

def test_sub():
    assert calculadora.sub(2, 1) == 1

def test_mult():
    assert calculadora.mult(3, 4) == 12

def test_div():
    assert calculadora.div(10, 2) == 5

