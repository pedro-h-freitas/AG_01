from sympy import Derivative, Integral, Symbol, pi, cos

C = 971 % 10  # Constante
A = 0.15  # m - Amplitude
F = 20  # Hz - Frequencia
W = 2 * pi * F  # Frequência angular


def minha_funcao(t):
    return A * W * cos(W * t - C)


if __name__ == '__main__':
    t = Symbol('t')

    x = Integral(minha_funcao(t), t).doit()
    v = minha_funcao(t)
    a = Derivative(minha_funcao(t), t).doit()

    a10 = a.subs({t: 10})

    print('\n***  DESLOCAMENTO  ***')
    print(f'x(t) = {x}')

    print('\n***  VELOCIDADE  ***')
    print(f'v(t) = {v}')

    print('\n***  ACELERAÇÃO  ***')
    print(f'a(t) = {a}')

    print('\n***  a em t=10  ***')
    print(f'a(10) = {a10}')
    print(f'a(10) = {round(float(a10), 2)} m/s²')
