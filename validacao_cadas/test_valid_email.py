import pytest
from valid_email import validar_email

@pytest.mark.parametrize("email", [
    "email@gmail.com",
    "nome.sobrenome@dominio.com.br",
    "primeiro_nome.ultimo_nome@dominio.com",
    "email+tag@exemplo.com",
    "silva@dominio.com",
    "email@sub.dominio.com"
])
def test_email_valido(email):
    assert validar_email(email), f"O e-mail {email} deveria ser válido."

@pytest.mark.parametrize("email", [
    "email.invalido",
    "hotmail@.com",
    "email@dominio-sem-ponto",
    "email@.com.br",
    "@seminicio.com",
    "email@dominio_com_underscore.com",
    "email@domínio-acento.com",
    "espaço@dominio.com",
    "email@dominio..com"
])
def test_email_invalido(email):
    assert not validar_email(email), f"O e-mail {email} deveria ser inválido."
