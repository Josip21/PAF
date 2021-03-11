def funkcija(x1,y1,x2,y2):
    k = (y2-y1) / (x2-x1)
    l = -k * (x1) + y1
    return print("Jednadzba pravca je:{}x+{}".format(k,l)) 


funkcija(1,1,2,2)