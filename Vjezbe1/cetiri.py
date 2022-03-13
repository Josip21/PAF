def funkcija(x1,y1,x2,y2):
    k = (y2-y1) / (x2-x1)
    l = -k * (x1) + y1
    return print("y={}*x+{}".format(k,l)) 


funkcija(2,2,4,4)