import pytest
from cont_palavras import contador_palavras

def test_texto_vazio():
    assert contador_palavras("") == 0, "O texto vazio deve retornar uma contagem de 0 palavras"

def test_uma_palavra():
    assert contador_palavras("Python") == 1, "O texto com uma única palavra deve retornar uma contagem de 1 palavra"

def test_varias_palavras():
    assert contador_palavras("Olá, mundo Python!") == 3, "O texto com várias palavras deve retornar a contagem correta"

def test_espacos_extras():
    assert contador_palavras("  Python  é  incrível  ") == 3, "O texto com espaços extras deve retornar a contagem correta ignorando os espaços extras"

def test_linha_nova():
    assert contador_palavras("Python\né\nincrível") == 3, "O texto com quebras de linha deve considerar cada palavra separadamente"

def test_com_pontuacao():
    assert contador_palavras("Python, é incrível!") == 3, "O texto com pontuação deve contar as palavras corretamente, ignorando a pontuação"
