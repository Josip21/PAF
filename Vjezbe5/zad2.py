import harmonic_oscillator as h_o 
import matplotlib.pyplot as plt
import numpy as np

h_1 = h_o.HarmonicOscillator()

def preciznost():
    dt_lista = list(np.linspace(0.01,0.11, 50))
    num_period = []
    a_period = []

    for dt in dt_lista:
        h_1.init(0.1,5,0,0.5,dt)    #(m,k,v0,A,dt)
        num_period.append(h_1.period())
        a_period.append(h_1.period_analitic())
        h_1.reset()

    plt.plot(dt_lista, a_period, label = "analiticki period")
    plt.scatter(dt_lista, num_period, s = 3, c = "orange", label = "numericki period")
    plt.xlabel("dt [s]")
    plt.ylabel("T [s]")
    plt.title("Preciznost numerickog racunanja perioda")
    plt.legend(loc = "lower right")
    plt.show()

def apsolutna_pogreska():
    dt_lista = list(np.linspace(0.01,0.11, 50))
    aps_pogreska = []

    for dt in dt_lista:
        h_1.init(0.1,5,0,0.5,dt)    #(m,k,v0,A,dt)
        greska = (abs(h_1.period() - h_1.period_analitic()) / h_1.period_analitic()) * 100
        aps_pogreska.append(greska)
        h_1.reset()

    plt.plot(dt_lista, aps_pogreska)
    plt.xlabel("dt [s]")
    plt.ylabel("absolute error [%]")
    plt.title("preciznost numerickog racunanja perioda")
    plt.show()

apsolutna_pogreska()
preciznost()