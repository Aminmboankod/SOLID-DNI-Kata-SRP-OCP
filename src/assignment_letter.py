

class MappingTable:

    def __init__(self):
        self.table_of_letters = ["T","R","W","A","G","M","Y","F","P","D","X","B",
                                "N","J","Z","S","Q","V","H","L","C","K","E"]
    

    def assignmentLetter(self, number):
        resto = int(number) % len(self.table_of_letters)
        return resto

    def getLetter(self, number):
        return self.table_of_letters[self.assignmentLetter(number)]
