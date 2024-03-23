import pytest
import datetime
from dif_datas import diferenca_entre_datas

def test_diferenca_em_dias():
    data_inicial = datetime(2020, 1, 1)
    data_final = datetime(2020, 1, 31)
    assert diferenca_entre_datas(data_inicial, data_final, "dias") == 30

def test_diferenca_em_horas():
    data_inicial = datetime(2020, 1, 1, 0, 0)
    data_final = datetime(2020, 1, 2, 0, 0)
    assert diferenca_entre_datas(data_inicial, data_final, "horas") == 24

def test_diferenca_em_minutos():
    data_inicial = datetime(2020, 1, 1, 0, 0)
    data_final = datetime(2020, 1, 1, 1, 0)
    assert diferenca_entre_datas(data_inicial, data_final, "minutos") == 60

def test_diferenca_em_meses():
    data_inicial = datetime(2020, 1, 1)
    data_final = datetime(2020, 4, 1)
    assert diferenca_entre_datas(data_inicial, data_final, "meses") == 3

def test_diferenca_em_anos():
    data_inicial = datetime(2019, 1, 1)
    data_final = datetime(2020, 1, 1)
    assert diferenca_entre_datas(data_inicial, data_final, "anos") == 1

def test_unidade_nao_reconhecida():
    data_inicial = datetime(2020, 1, 1)
    data_final = datetime(2020, 1, 2)
    with pytest.raises(ValueError):
        diferenca_entre_datas(data_inicial, data_final, "indefinido")
