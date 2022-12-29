from src.assignment_letter import MappingTable

class Dni:
    
    def __init__(self):
        self.tabla = MappingTable()

    @staticmethod
    def checkDni(num):
        if len(num) == 8 and num.isdigit():
            return True
        return False


    def completeDni(self, num):
        return num+(self.tabla.getLetter(num))
    