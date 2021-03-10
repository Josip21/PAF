import matplotlib.pyplot as plt
def Pravac(x1,y1,x2,y2,znak):
    x = [x1,x2]
    y = [y1,y2]
    plt.plot(x,y)
    if znak == 0:
        plt.show()
    elif znak == 1:
        ime = input("Ime:")
        plt.savefig(f'{ime}.pdf')


PravacO(1,1,2,2)
