class Eyewear:
    '''This class is for providing a structure to a pair of Eyewear and is run through the EWConstructor class. The format of it should print: Material > Vision type > Clear/Sun > Included Options. For example: Polycarbonate, No-Line Multifocal, Clear, w/ AR, w/ BL'''
    def __init__(self, ewid, material, vision, is_sun, options):
        self.ewid = ewid #EWConstructor will assign this based of of the DB to give unique ids.(Int)
        self.material = material #Material of the lens.(String)
        self.vision = vision #Represents what type of single/multifocal vision.(String)
        self.is_sun = is_sun #Represents if the eyewear is Clear/Tint/Polar.(String)
        self.options = options #tuple representing all present options. (tuple)

    def print_options(self):
        #Help format options tuple into readable text for __str__ redefinition.
        string = []
        for item in self.options:
            string.append("w/" + item)
        return " ".join(string)

    def __str__(self):
        #Redefine how the eyewear is represented as a string
        return f'{self.material},{self.vision},{self.is_sun} {self.print_options()}'

class EWConstructor:
    def vision(self):
        