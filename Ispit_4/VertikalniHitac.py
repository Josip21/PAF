
class VertikalniHitac:
    def __init__(self, h0, v0):
        self.h = h0
        self.v = v0
        self.t = 0
        self.h_lista = []
        self.v_lista = []
        self.t_lista = []
        self.h_lista.append(self.h)
        self.v_lista.append(self.v)
        self.t_lista.append(self.t)
        print("Pocetna visina je: {}".format(self.h_lista))
        print("Pocetna brzina je: {}".format(self.v_lista))

    def promijeni_visinu(self, h):
        self.h = h
        print("Nova visina: {}".format(self.h))

    def promijeni_brzinu(self, v):
        self.v = v
        print("Nova brzina: {}".format(self.v))
    
    def move(self,dt):
        self.t = self.t + dt
        self.v = self.v - 10 * dt
        self.h = self.h + self.v * dt
        self.t_lista.append(self.t)
        self.v_lista.append(self.v)
        self.h_lista.append(self.h)

    def move_ar(self, k, dt):
        self.t = self.t + dt
        self.v = self.v - 10 * dt - k * self.v * dt
        self.h = self.h + self.v * dt
        self.t_lista.append(self.t)
        self.v_lista.append(self.v)
        self.h_lista.append(self.h)

    def evolve(self, dt):
        while self.h > 0:
            self.move(dt)
        return self.h_lista, self.v_lista, self.t_lista
    
    def evolve_ar(self, k, dt):
        while self.h > 0:
            self.move(k, dt)
        return self.h_lista, self.v_lista, self.t_lista
    
    def max_heightNum(self, dt):
        while self.v > 0:
            self.move(dt)
        return self.h

    def max_heightAr(self, k, dt):
        while self.v > 0:
            self.move(k, dt)
        return self.h

    def timedurationNum(self, dt):
        while self.h > 0:
            self.move(dt)
        return self.t

    def timedurationNum_ar(self, k, dt):
        while self.h > 0:
            self.move(k, dt)
        return self.t

    def reset(self):
        self.h = self.h_lista[0]
        self.v = self.v_lista[0]
        self.t = 0
        self.h_lista = []
        self.v_lista = []
        self.t_lista = []
        self.t_lista.append(self.t)
        self.v_lista.append(self.v)
        self.h_lista.append(self.h)



        