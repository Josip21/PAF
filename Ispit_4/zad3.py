import VertikalniHitac as VH
import matplotlib.pyplot as plt

vh1 = VH.VertikalniHitac(10, 10)
h_list, v_list, t_list = vh1.evolve(0.01)

plt.plot(t_list, h_list)
plt.title("h-t graf")
plt.xlabel("t [s]")
plt.ylabel("h [m]")
plt.show()

plt.plot(t_list, v_list)
plt.title("v-t graf")
plt.xlabel("t [s]")
plt.ylabel("v [m/s]")
plt.show()