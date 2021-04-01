from math import sin
from math import cos
from math import pi 
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, vp, xp):

    a = F/m
    VK = []
    XK = []
    Y = []
    A = []

    for t in range(1,11):
        vk = vp + a*t
        VK.append(vk)

        xk = xp + vk*t
        XK.append(xk)
        Y.append(t)
        A.append(a)

    fig1 = plt.figure()
    fig1.suptitle('Grafovi')

    plt.subplot(2,2,1)
    plt.plot(Y, XK, label = 'x-t graf')

    plt.subplot(2,2,2)
    plt.plot(Y, A, label = 'a-t graf')

    plt.show()



def kosi_hitac(theta, v0, t):
    thetarad = theta*pi/180
    a = 9.81
    t = 10
    v0x = v0 * cos(thetarad)
    v0y = v0 * sin(thetarad)
    vy = v0y

    n = 100
    delta_t = t/n

    sx = 0
    sy = 0
    t_brojac = 0

    X = []
    Y = []
    T = []

    X.append(sx)
    Y.append(sy)
    T.append(t_brojac)

    for i in range(n):

        t_brojac = t_brojac + delta_t
        T.append(t_brojac)

        sx = sx + v0x*delta_t
        X.append(sx)

        vy = vy - a*delta_t
        sy = sy + vy*delta_t
        Y.append(sy)
    fig, axes = plt.subplots(2,2)

    axes[0, 0].plot(X,Y)
    axes[0, 0].set_title('x-y graf')

    axes[0, 1].plot(T, X)
    axes[0, 1].set_title('x-t graf')

    axes[1, 0].plot(T, Y)
    axes[1, 0].set_title('y-t graf')

    plt.show()