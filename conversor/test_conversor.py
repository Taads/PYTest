import pytest
import conversor

def test_dolar_em_euro():
    assert conversor.dolar_em_euro(100) == pytest.approx(93)

def test_euro_em_dolar():
    assert conversor.euro_em_dolar(100) == pytest.approx(108)

def test_real_em_dolar():
    assert conversor.real_em_dolar(100) == pytest.approx(20)

def test_dolar_em_real():
    assert conversor.dolar_em_real(100) == pytest.approx(500)

def test_euro_em_real():
    assert conversor.euro_em_real(100) == pytest.approx(538)

def test_real_em_euro():
    assert conversor.real_em_euro(100) == pytest.approx(19)
