def nacrtaj_kruznicu_i_tocku(xi, yi, r, xt, yt):
    x = []
    y = []

    for fi in range(1, 360):
        rad = fi*pi/180
        xs = xi + r*cos(rad)
        x.append(xs)
        ys = yi + r*sin(rad)
        y.append(ys)
        plt.plot(x,y)
        plt.plot(xt, yt, 'bo')
        p = input('Odma ili PDF')
        if p=='odma':
            plt.show()
        elif p == 'PDF':
            ime = input("Unesite ime PDF")
            plt.savefig(f'{ime}.pdf')

import matplotlib
import matplotlib.pyplot as plt
from math import sqrt
from math import pi
from math import cos
from math import sin
import numpy as np


while True:
    xi = float(input('Unesi x'))
    yi = float(input('Unesi y'))

    if xi == str or yi == str:
        print('Broj ne string')
    else:
        break

while True:
    r = int(input('Unesi radijus kruznice:'))

    if r == 0 or r == str:
        print('Radijus mora biti veci od 0 i ne smije biti string')
    else:
        break
d = sqrt((xi-xt)**2+(yi-yt)**2)

if d > r:
    print('Tocka se nalazi izvan kruznice i udaljena je {} od kruznice!'.format(d-r))
elif d == r:
    print('Tocka se nalazi na kruznici u udaljena je {} od kruznice'.format(d=r))
else:
    print('Tocka se nalazi unutar kruznice i udaljena je {} od kruznice!'.format(r-d))

plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

nacrtaj_kruznicu_i_tocku(xi, yi, r, xt, yt)