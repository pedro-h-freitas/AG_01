from sympy import Integral, Symbol

C = 224 % 10


def minha_func(x):
    return x**3 - 4*x**2 + 5*x - C


if __name__ == '__main__':
    x = Symbol('x')

    result = Integral(minha_func(x), (x, 0, 5)).doit()

    print(result)
