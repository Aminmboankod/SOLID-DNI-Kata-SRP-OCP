
class TablaAsignacion:

    def __init__(self):
        self.tablaDigitos = ["T","R","W","A","G","M","Y","F","P","D","X","B",
                        "N","J","Z","S","Q","V","H","L","C","K","E"]

    def calcularResto(self, nif):
        return int(nif) % len(self.tablaDigitos)


    def obtenerDigito(self, nif):
        return self.tablaDigitos[self.calcularResto(nif)]
        
