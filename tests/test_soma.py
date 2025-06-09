def soma(a, b):
    return a + b

def test_soma_com_valores_positivos():
    resultado = soma(2, 3)
    assert resultado == 5

def test_soma_com_valores_positivos_e_negativos():
    resultado = soma(-1, 1)
    assert resultado == 0