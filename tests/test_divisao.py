def divisao(a, b):
    return a / b

def test_divisao_com_valores_positivos():
    resultado = divisao(10, 2)
    assert resultado == 5

def test_divisao_com_valores_zero():
    resultado = divisao(5, 0)
    assert resultado == ZeroDivisionError