F = float(input("Unesi silu u N:"))
m = float(input("Unesi masu u kilogramima:"))
a = F/m
vp = float(input("Unesi početnu brzinu:"))
xp = float(input("Unesi početni položaj:"))
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

import matplotlib.pyplot as plt

fig1 = plt.figure()
fig1.suptitle('Grafovi')

plt.subplot(2,2,1)
plt.plot(Y, XK, label = 'x-t graf')

plt.subplot(2,2,2)
plt.plot(Y, A, label = 'a-t graf')

plt.show()