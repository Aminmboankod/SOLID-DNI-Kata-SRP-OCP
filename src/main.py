from assignment_letter import MappingTable
from Dni import Dni



if __name__=="__main__":




    dni = Dni()
    nif = input("Introduzca su DNI sin letra: ")
    
    def respuesta(nif):
        if Dni.checkDni(nif) == True:
                print("Su DIN con letra es: "+ (dni.completeDni(nif)))
        else:
            print("Introduce un número de 8 dígitos!")
