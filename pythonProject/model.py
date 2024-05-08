class Frame:
    def __init__(self):
        self.roll1 = None
        self.roll2 = None
        self.puntaje = 0

    def calcular_puntaje(self):
        if self.es_strike():
            self.puntaje = 10 + self.roll1 + self.roll2
        elif self.es_spare():
            self.puntaje = 10 + self.roll1
        else:
            self.puntaje = self.roll1 + self.roll2

    def es_strike(self):
        return self.roll1 == 10

    def es_spare(self):
        return self.roll2 == 10

class Juego:
    def __init__(self):
        self.frames = []
        self.puntaje_total = 0

    def agregar_tiro(self, roll1, roll2):
        frame = Frame()
        frame.roll1 = roll1
        frame.roll2 = roll2
        frame.calcular_puntaje()
        self.frames.append(frame)
        self.calcular_puntaje_total()

    def calcular_puntaje_total(self):
        puntaje_acumulado = 0
        for i in range(len(self.frames)):
            puntaje_cuadro = self.frames[i].puntaje
            if i == 9:
                puntaje_cuadro += self.calcular_puntaje_extra(i)
            puntaje_acumulado += puntaje_cuadro
        self.puntaje_total = puntaje_acumulado

    def calcular_puntaje_extra(self, indice_cuadro):
        puntaje_extra = 0
        siguiente_cuadro = self.frames[indice_cuadro + 1]
        if siguiente_cuadro.es_strike():
            puntaje_extra += 10 + siguiente_cuadro.roll1
            if siguiente_cuadro.es_strike():
                puntaje_extra += self.frames[indice_cuadro + 2].roll1
        elif siguiente_cuadro.es_spare():
            puntaje_extra += siguiente_cuadro.roll1
        return puntaje_extra
