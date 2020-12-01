import constants #constants contain all regex information for all terms

class Eyewear:
    '''This class is for providing a structure to a pair of Eyewear and is run through the EyeWearConstructor class. The format of it should print: Material > Vision type > Clear/Sun > Included Options. For example: Polycarbonate, No-Line Multifocal, Clear, w/ AR, w/ BL'''
    def __init__(self, ewid, material, vision, is_sun, options):
        self.ewid = ewid #EyeWearConstructor will assign this based of of the DB to give unique ids.(Int)
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

class EyeWearConstructor:
    def select_material(self):
        #Function used to determine the material of the lens
        while True:    #Hold until something is selected
            materials = ["CR39","Polycarbonate","High_Index 1.67","Other"]
            input_int = input("What is the lens made from?\n1: CR39 or Plastic\n2: Polycarbonate\n3: High-Index 1.67\n4: Other")
            if input_int in range(1,6): #Check if valid response
                return materials[input_int-1]
            elif input_int.lower() == "cancel": #Check if exiting program
                return None
            else:
                print("Invalid Response")

    def select_vision(self):
        #Function used to determine the type of vision.
        #Has nested function to determine type of Multi-Focal vision
        while True:    #Hold until vision selected
            def select_multifocal():
                #Nested function to determine what type of multifocal lens
                while True    #Hold until multifocal selected
                    input_int = input("What type of Multi-Focal lens?\n1: Line\n2: No-Line or Progressive")
                    if input_int in range(1,3): #Check if valid response
                        if input_int == 1:
                            return "Line Multi-Focal Vision"
                        elif input_int == 2:
                            return "Progressive Multi-Focal Vision"
                    elif input_int.lower() == "cancel": #Check if exiting program
                        return None
                    else:
                        print("Invalid Response")
            input_int = input("What type of vision?\n1: Single Vision\n2: Multi-Focal Vision(Lined or No-line)")
            if input_int in range(1,3): #Check if valid response
                if input_int == 1:
                    return "Single Vision"
                if input_int == 2:
                    return select_multifocal()
            elif input_int.lower() == "cancel": #Check if exiting program
                return None
            else:
                print("Invalid Response")

    def is_sun(self):
        #Function to determine if the lens is sunwear
        #If for sun, then nested function will determine if it is tint or polar
        while True:   #Hold until sun or clear is determined.
            def select_sun():
                #Nested function to determine what type of sunwear
                while True:    #Hold until Tint or Polar is selected
                    input_int = input("What kind of sunwear is this?\n1: Tint or Non-Polar\n2: Polar")
                    if input_int in range(1,3):  #Check if valid response
                        if input_int == 1:
                            return "Tint"
                        elif input_int == 2:
                            return "Polar"
                    elif input_int.lower() == "cancel":  #Check if exiting program
                        return None
                    else:
                        print("Invalid Response")
            input_str = input("Is this sunwear?(Transition is considered clear)\n(Y)es/(N)o")
            fchar = input_str[0].lower()
            if fchar in ["y","n"]:  #Check if valid response
                if fchar == "y":
                    return select_sun()
                elif fchar == "n":
                    return "Clear"
            elif input_str.lower() == "cancel":  #Check if exiting program
                return None
            else:
                print("Invalid Response")

    def select_options(self):
        def has_antiglare():
            input_str = input("Is there an Anti-Glare or Anti-Reflective coating?\n(Y)es/(N)o")
            fchar = input_str[0].lower()
            if fchar in ["y","n"]:
                if fchar == "y":
                    return True
                elif fchar == "n":
                    return False
                else
        def has_other():
            pass

       # input_str = input("Is there an Anti-Glare or Anti-Reflective coating?\n(Y)es/(N)o")
        # if fchar in ["y","n"]:
        #     if fchar == "y":
        #         options.append("Anti-Glare")