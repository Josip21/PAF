import VertikalniHitac as VH
import matplotlib.pyplot as plt

vh1 = VH.VertikalniHitac(10, 10)

dt_list = []
re_list = []

for i in range(100):
    dt_list.append(0.001 * (i + 1))

for dt in dt_list:
    vh1.reset()
    numeric = vh1.timedurationNum(dt)
    vh1.reset()
    analitic = vh1.timedurationNum_ar(1)
    re = abs(100 * (numeric - analitic) / analitic)
    re_list.append(re)

plt.plot(dt_list, re_list)
plt.show()