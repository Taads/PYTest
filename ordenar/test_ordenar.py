import pytest
from ordenacao import ordem_crescente, ordem_decrescente

def test_ordem_crescente():
    assert ordem_crescente([]) == [], "A lista vazia deve retornar uma lista vazia"
    assert ordem_crescente([1]) == [1], "Uma lista com um único elemento deve retornar ela mesma"
    assert ordem_crescente([1, 1, 1]) == [1, 1, 1], "Uma lista com elementos iguais deve retornar ela mesma"
    assert ordem_crescente([-1, -2, -3]) == [-3, -2, -1], "A lista com números negativos deve ser ordenada corretamente"

def test_ordem_decrescente():
    assert ordem_decrescente([5, 2, 3, 1, 4]) == [5, 4, 3, 2, 1], "A lista deve estar ordenada em ordem decrescente"
    assert ordem_decrescente([]) == [], "A lista vazia deve retornar uma lista vazia"
    assert ordem_decrescente([1]) == [1], "Uma lista com um único elemento deve retornar ela mesma"
    assert ordem_decrescente([1, 1, 1]) == [1, 1, 1], "Uma lista com elementos iguais deve retornar ela mesma"
    assert ordem_decrescente([-1, -2, -3]) == [-1, -2, -3], "A lista com números negativos deve ser ordenada corretamente em ordem decrescente"
