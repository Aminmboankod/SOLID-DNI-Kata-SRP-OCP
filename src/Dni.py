

class Dni:
    

    @staticmethod
    def checkDni(num):
        if len(num) == 8 and num.isdigit():
            return True
        return False


    