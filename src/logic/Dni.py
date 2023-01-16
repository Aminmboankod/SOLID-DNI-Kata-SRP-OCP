from src.accesoDatos.caculadoraDNI import *

class DNI:
    
    def __init__(self, dni="", nif="", digitoControl=""):
        self.tablaDigitos = TablaAsignacion()
        self.nif = nif
        self.dni = dni
        self.digitoControl = digitoControl

    def dividirDigito(self):
        if self.verificarDNI() == True:
            self.digitoControl += self.dniCompleto[-1]

    def verificaDigito(self):
        return self.tablaDigitos.obtenerDigito(self.nif) == self.dividirDigito()
    
    def dividirNIF(self):
        if self.verificarDNI() == True:
            self.nif += self.dniCompleto[:-1]
    
    def verificaLongitudNIF(self):
        return len(self.nif) == 8
            
    def verificaContenidoNIF(self):
        return (self.nif).isdigit()

    def verificarNIF(self):
        return self.verificaLongitudNIF() and self.verificaContenidoNIF()
        
    def obtenerNIF(self):
        return self.nif

    def dniCompleto(self):
        self.digitoControl += self.tablaDigitos.obtenerDigito(self.nif)
        self.dni += str(self.nif)+str(self.digitoControl)
        return self.dni
    
    def obtenerDNI(self):
        return self.dni

    def verificarDNI(self):
        return len(self.dniCompleto()) == 9
        
        