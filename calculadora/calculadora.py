def soma(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("Não é possível dividir por zero.")

def verifica_valores(*args):
    for arg in args:
        if not isinstance(arg, (int, float)):
            raise ValueError("Todos os valores devem ser numéricos.")
    return True


