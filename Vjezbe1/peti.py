def graf(x1,y1,x2,y2):
    x = [x1,x2]
    y = [y1,y2]
    plt.plot(x,y)
    plt.plot(x1,y1, "ro")
    plt.plot(x2,y2, "ro")
    p = input("Graf ispisati odmah ili PDF")
    if p == "odma":
        plt.show()
    elif p == "PDF":
        ime = input("Ime PDF")
        plt.savefog(f"{ime}.pdf")

import matplotlib.pyplot as plt

x1 = float(input("Unesi koordinatu:"))
y1 = float(input("Unesi koordinatu:"))

x2 = float(input("Unesi koordinatu:"))
y2 = float(input("Unesi koordinatu:"))
plt.xlabel("x")
plt.ylabel("y")
plt.title("Pravac kroz dvije tocke")
graf(x1,y1,x2,y2)    
