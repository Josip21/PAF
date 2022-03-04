while True:
    x1 = float(input("Unesi koordinatu:"))
    y1 = float(input("Unesi koordinatu"))
    x2 = float(input("Unesi koordinatu:"))
    y2 = float(input("Unesi koordinatu:"))
    print(x1,y1,x2,y2)

    k = (y2-y1) / (x2-x1)
    l = -k * (x1) + y1
    if x2 == x1:
        print("Ponovi unos")
    else:
        print("y={}*x+{}".format(k,l))
        break