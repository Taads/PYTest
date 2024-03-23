import pytest
from valid_tel import validar_telefone

@pytest.mark.parametrize("numero_telefone, esperado", [
    ("(14) 99288-7047", True),
    ("(11) 9971-2796", True),
    ("(16) 9918-3736", False),  
    ("(44) 9190-9278", False),   
    ("(21)9 4065-4111", False),
    ("(16) 92395-6499", True),
    ("(11) 92397-9092", True), 
    ("(1) 9889-2499", False),  
    ("(123) 9809-1197", False),
    ("(99) 9999-9999", False),  
    ("(00) 000000000", False),               
    ("(99) 9889-889", False),  
    ("(99) 99999-99999", False)
])
def test_validacao_telefone(numero_telefone, esperado):
    assert validar_telefone(numero_telefone) == esperado, f"Erro ao validar {numero_telefone}"
