from sympy import Limit, Symbol, S

C = 224 % 10


def minha_funcao(x):
    return (1 + (C + 4) / (x**3)) ** (x**3)


if __name__ == '__main__':
    x = Symbol('x')

    result = Limit(minha_funcao(x), x, 0).doit()
    print(f'\nX -> 0: {result}')

    result = Limit(minha_funcao(x), x, S.Infinity).doit()
    print(f'\nX -> infinito: {result}')

    result = Limit(minha_funcao(x), x, -S.Infinity).doit()
    print(f'\nX -> -infinito: {result}')
