import pytest
from voo_ import Voo, SistemaReservas

@pytest.fixture
def sistema_voos_preparado():
    sistema = SistemaReservas()
    voo1 = Voo("V001", "Bauru", "São Paulo", 2)
    voo2 = Voo("V002", "Rio de Janeiro", "Salvador", 1)
    sistema.adicionar_voo(voo1)
    sistema.adicionar_voo(voo2)
    return sistema

def test_adicionar_voo(sistema_voos_preparado):
    sistema = sistema_voos_preparado
    voo3 = Voo("V003", "São Paulo", "NY", 3)
    sistema.adicionar_voo(voo3)
    assert len(sistema.voos) == 3

def test_pesquisar_voos_disponiveis(sistema_voos_preparado):
    sistema = sistema_voos_preparado
    voos_disponiveis = sistema.pesquisar_voos("Rio de Janeiro", "Salvador")
    assert len(voos_disponiveis) == 1
    assert voos_disponiveis[0].id_voo == "V002"

def test_realizar_reserva_com_sucesso(sistema_voos_preparado):
    sistema = sistema_voos_preparado
    sucesso = sistema.realizar_reserva("V001")
    assert sucesso
    assert sistema.voos[0].assentos == 1
    assert sistema.visualizar_reservas()["V001"] == 1

def test_tentar_reserva_sem_assentos(sistema_voos_preparado):
    sistema = sistema_voos_preparado
    sistema.realizar_reserva("V002")  
    sucesso = sistema.realizar_reserva("V002") 
    assert not sucesso

def test_visualizar_reservas(sistema_voos_preparado):
    sistema = sistema_voos_preparado
    sistema.realizar_reserva("V001")
    reservas = sistema.visualizar_reservas()
    assert "V001" in reservas
    assert reservas["V001"] == 1

def test_cancelar_reserva(sistema_voos_preparado):
    sistema = sistema_voos_preparado
    sistema.realizar_reserva("V001")
    cancelado = sistema.cancelar_reserva("V001")
    assert cancelado
    assert sistema.voos[0].assentos == 2
    assert sistema.visualizar_reservas()["V001"] == 0
