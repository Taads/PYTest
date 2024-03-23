import re

def validar_telefone(numero_telefone):
    pattern = re.compile(r'^\(\d{2}\) (9?\d{4}-\d{4})$')
    
    if pattern.match(numero_telefone):
        return True
    else:
        return False
