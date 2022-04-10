import harmonic_oscillator as h_o 

h_1 = h_o.HarmonicOscillator()

h_1.init(0.1,5,0,0.5,0.001)   
print("Period titranja iznosi: {:.2f}".format(h_1.period()))
print("Analiticki period titranja iznosi: {:.2f}".format(h_1.period_analitic()))