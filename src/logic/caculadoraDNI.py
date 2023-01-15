
class CalculadoraDNI:

    def __init__(self, numero):
        self.numero = numero
        self.table = ["T","R","W","A","G","M","Y","F","P","D","X","B",
                        "N","J","Z","S","Q","V","H","L","C","K","E"]
    

    def calcularResto(self):
        resto = int(self.numero) % len(self.table)
        return resto

    def obtenerPosicionLetra(self):
        posicion = self.calcularResto()
        return posicion 

    def obtenerLetraTabla(self):
        letra = self.table[self.obtenerPosicionLetra()]
        return letra
