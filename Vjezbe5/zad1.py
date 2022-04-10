import harmonic_oscillator as h_o 
import matplotlib.pyplot as plt

h_1 = h_o.HarmonicOscillator()

h_1.init(0.1,5,0,0.3,0.01)   
h_1.oscillate(2)
h_1.plot_trajectory()
plt.scatter(h_1.t,h_1.x, s = 2, c = "green", label = "dt = 0.01")
h_1.reset()

h_1.init(0.1,5,0,0.3,0.025)    
h_1.oscillate(2)
plt.scatter(h_1.t,h_1.x, s = 4, c = "orange", label = "dt = 0.025")
h_1.reset()

h_1.init(0.1,5,0,0.3,0.05)    
h_1.oscillate(2)
plt.scatter(h_1.t,h_1.x, s = 6, label = "dt = 0.05")
h_1.reset()

h_1.init(0.1,5,0,0.3,0.01)    
h_1.analitic_x(2)
plt.plot(h_1.t, h_1.x, c = "red", label = "analitic")
h_1.reset()

plt.xlabel("t [s]")
plt.ylabel("x [m]")
plt.title("Precicnost numeričkog riješenja")
plt.legend(loc = "lower right")
plt.show()