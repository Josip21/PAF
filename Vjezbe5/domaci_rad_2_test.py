import matplotlib.pyplot as plt
import domaci_rad_2 as m

def f1(v,x,t):
    return 10

p1 = m.Particle()
p1.init(f1,1.5,0,0,1,0.01)    
p1.plot_trajectory()

def f2(v,x,t):
    k = 10
    return -k*x

p2 = m.Particle()
p2.init(f2,1.5,2,0,5,0.01)    
p2.plot_trajectory()
