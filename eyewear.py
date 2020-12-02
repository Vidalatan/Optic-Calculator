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

class EyewearConstructor:
    '''This class specifically designed to instantiate Eyewear class objects off of the Eyewear class. It has several
    functions that loop through and generate the information needed to instantiate the object.'''
    def select_material():
        #Function used to determine the material of the lens
        while True:    #Hold until something is selected
            materials = ["CR39","Polycarbonate","High_Index 1.67","Other"]
            input_int = int(input("What is the lens made from?\n1: CR39 or Plastic\n2: Polycarbonate\n3: High-Index 1.67\n4: Other\n"))
            if input_int in range(1,6): #Check if valid response
                return materials[input_int-1]
            elif input_int.lower() == "cancel": #Check if exiting program
                return None
            else:
                print("Invalid Response")

    def select_vision():
        #Function used to determine the type of vision.
        #Has nested function to determine type of Multi-Focal vision
        while True:    #Hold until vision selected
            def select_multifocal():
                #Nested function to determine what type of multifocal lens
                while True:  #Hold until multifocal selected
                    input_int = int(input("What type of Multi-Focal lens?\n1: Line\n2: No-Line or Progressive\n"))
                    if input_int in range(1,3): #Check if valid response
                        if input_int == 1:
                            return "Line Multi-Focal Vision"
                        elif input_int == 2:
                            return "Progressive Multi-Focal Vision"
                    elif input_int.lower() == "cancel": #Check if exiting program
                        return None
                    else:
                        print("Invalid Response")
            input_int = int(input("What type of vision?\n1: Single Vision\n2: Multi-Focal Vision(Lined or No-line)\n"))
            if input_int in range(1,3): #Check if valid response
                if input_int == 1:
                    return "Single Vision"
                if input_int == 2:
                    return select_multifocal()
            elif input_int.lower() == "cancel": #Check if exiting program
                return None
            else:
                print("Invalid Response")

    def is_sun():
        #Function to determine if the lens is sunwear
        #If for sun, then nested function will determine if it is tint or polar
        while True:   #Hold until sun or clear is determined.
            def select_sun():
                #Nested function to determine what type of sunwear
                while True:    #Hold until Tint or Polar is selected
                    input_int = int(input("What kind of sunwear is this?\n1: Tint or Non-Polar\n2: Polar\n"))
                    if input_int in range(1,3):  #Check if valid response
                        if input_int == 1:
                            return "Tint"
                        elif input_int == 2:
                            return "Polar"
                    elif input_int.lower() == "cancel":  #Check if exiting program
                        return None
                    else:
                        print("Invalid Response")
            input_str = input("Is this sunwear?(Transition is considered clear)\n(Y)es/(N)o\n")
            fchar = input_str[0].lower()  #Simplify character check for yes or no
            if fchar in ["y","n"]:  #Check if valid response
                if fchar == "y":
                    return select_sun()
                elif fchar == "n":
                    return "Clear"
            elif input_str.lower() == "cancel":  #Check if exiting program
                return None
            else:
                print("Invalid Response")

    def select_options(is_sun):
        #Function to determine what other options are on the lense
        def has_antiglare():
            #Nested function to determine if Anti-Glare is part of the eyewear.
            input_str = input("Is there an Anti-Glare or Anti-Reflective coating?\n(Y)es/(N)o\n")
            fchar = input_str[0].lower() #Simplify character check for yes or no
            while True:  #Hold until something is selected
                if fchar in ["y","n"]: #Check if valid response
                    if fchar == "y":
                        return "Anti-Glare Coating"
                    elif fchar == "n":
                        return "Nothing"
                    elif input_str == "cancel":  #Check if exiting program
                        return None
                    else:
                        print("Invalid Response")
        def has_other(is_sun):
            #This function is unique to the others in that it can return the string "Nothing" rather than the None value that is being used to exit the program at any point.
            if is_sun == "Clear":
                pass
            else:
                return "Nothing"
            input_int = int(input("Is there a Blue-Light filter or Photochromatic coating?\n1: Blue-Light filter\n2: Photochromatic coating\n3: Neither\n"))
            while True:
                others = ["Blue-Light filter","Photochromatic coating"]
                if input_int == 3:
                    return "Nothing"
                elif input_int in range(1,3):
                    return others[input_int-1]
                elif input_int == "cancel":
                    return None
                else:
                    print("Invalid Reponse")
        ar = has_antiglare()
        ot = has_other(is_sun)
        feedback = []
        for item in [ar,ot]:
            print(f"Testing {item}")
            if item != "Nothing":
                feedback.append(item)
        return feedback

    def build(identity):
        #This is the main function for the EyeWearConstructor. Will use all previous functions to instantiate Eyewear object from the Eyewear class
        def will_exit(variable):
            #Check if user exited during function
            if variable == None:
                return True
            else:
                return False
        material = EyewearConstructor.select_material()
        if will_exit(material):
            return 1
        vision = EyewearConstructor.select_vision()
        if will_exit(vision):
            return 2
        sun = EyewearConstructor.is_sun()
        if will_exit(sun):
            return 3
        options = EyewearConstructor.select_options(sun)
        if will_exit(options):
            return 4
        return Eyewear(identity,material,vision,sun,options)

    class EyewearHelper:
        '''This class is meant to give the program tools to help with trouble-shooting and calculations that would otherwise be
        difficult or repetative'''
        def trouble_shoot(self): #Will help with specific issues that may be present within eyewear object.
            pass
        def term_search(self): #Will help with looking up terms from a list of terms that will be in the constants.py file.
            pass
        def find_best_price(self):  #Will help with determining all of the best options for pricing. Does not calculate based off of eyewear object.
            pass
        def calculate_decentration(self):  #Will help with calculating decentration of prescription based on the box measurements of the eyewear. Will check if eyewear is fully defined.
            pass