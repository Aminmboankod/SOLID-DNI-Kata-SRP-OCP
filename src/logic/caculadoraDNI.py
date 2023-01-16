
class CalculadoraDNI:

    def __init__(self, numero):
        self.numero = numero
        self.table = ["T","R","W","A","G","M","Y","F","P","D","X","B",
                        "N","J","Z","S","Q","V","H","L","C","K","E"]
    

    def calcularResto(self):
        resto = int(self.numero) % len(self.table)
        return resto

    def posicionDigito(self):
        posicion = self.calcularResto()
        return posicion 

    def obtenerDigito(self):
        letra = self.table[self.posicionDigito()]
        return letra

    def nifCompleto(self):
        self.numero+str(self.obtenerDigito())