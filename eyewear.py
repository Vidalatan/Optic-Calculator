class Eyewear:
    def __init__(self,name,pin,lens,material,options):
        self.name = name # The name of the user the eyewear belongs to. (string)
        self.pin = pin # ^^Probably need to add encryption later if to retain a pin attr (int)
        self.lens = lens # Lens category that the eyewear falls into (string)
        self.material = material # Material of the lens (string)
        self.options = options # Will contain a dict for options if they are present or not. (dict{option:boolean,...})
    # def __str__(self):
    #     return f"The eyewear is {self.lens} vision. It is made of {self.material}. Anti-reflective {self.options['antireflect']}. Sunglass is {self.options['sun']} It has {self.options['other']}."
    # Need to modify the string representation of the Eyewear class

    def what_is(self):
        term = input("Please enter a specific or general term:\n(Example: Polycarbonate or materials")
        


    def _select_lens(self):
        # instance method for determining the lens in the eyewear. This is the primary
        # function for determining the lense.
        lens = None
        while lens not in ["sin","lbi","ltr","spr","ppr","dpr"]:
          lens = input("Single Vision (SV) or Multi-focal (MF)\n").lower()
          if re.search(select["single"], lens):
            # if the input is for single vision, set lens to "sin". End of probe.
            lens = "sin"
            print("Single Vision selected")
          elif re.search(select["multifo"], lens):
            # if the input is for multi-focal vision, move to multifocal method to continue probing.
            lens = self._is_multifocal()
          else:
            print(self.errmsg)
            continue
        return lens
    def _is_multifocal(self):
        # This function contains two inner functions for determining which type of
        # multi-focal lens the eyewear has.
        def is_linedmulti():
            # this is the nested function for determining if the lens is lined multifocal
            lens = input("Lined\n\tIs it bifocal(B) or trifocal(T)?\n").lower()
            if re.search(select["linebi"], lens):
                #if lens is lined bifocal, set lens to lbi
                lens = "lbi"
                print("Lined-Bifocal Vision selected.")
                return lens
            elif re.search(select["linetri"], lens):
                #if lens is lined trifocal, set lens to ltr
                lens = "ltr"
                print("Lined-Trifocal Vision selected.")
                return lens
            else:
                print(self.errmsg)
        def is_nolinemulti():
            # this is the nested function for determining if the lens is no-line multifocal
            lens = input("No-Line\n\tIs this a Standard(S), Premium(P), or Digital(D) progressive?\n").lower()
            if re.search(select["standpro"], lens):
                lens = "spr"
                print("Standard Progressive selected.")
                return lens
            elif re.search(select["prempro"], lens):
                lens = "ppr"
                print("Premium Progressive selected.")
                return lens
            elif re.search(select["digipro"], lens):
                lens = "dpr"
                print("Digital Progressive selected.")
                return lens
            else:
                print(self.errmsg)

        lens = input("Multi-focal\n\tIs this a line (L) or no-line/progressive (NL/P) multifocal lens?\n").lower()
        if re.search(select["lined"], lens):
            # if the input is for lined multi-focal vision, move to linedmulti method to continue probing.
            return is_linedmulti()
        elif re.search(select["noline"], lens):
            # if the input is for no-line/progressive multi-focal vision, move to nolinemulti method to continue probing
            return is_nolinemulti()
        else:
            print(self.errmsg)


    def _select_material(self):
        while True:
            material = input("What material is the lens made of?\n-CR-39(AKA Plastic)\n-Polycarobonate\nHigh-Index(AKA HI 1.67)\n").lower()
            if re.search(select["cr39"], material):
                material = "cr39"
                break
            elif re.search(select["poly"], material):
                material = "poly"
                break
            elif re.search(select["hi167"], material):
                material = "h167"
                break
            else:
                print(self.errmsg)
        return material

    def _select_options(self):
        # instance method for determining what options were included in the eyewear.
        while True:
            # while loop to determine what to set anti_reflect as.
            anti_reflect = input("Does the eyewear have an anti-reflective/anti-glare coating? Y/N\n").lower()
            if anti_reflect.lower() in ["yes","ye","y"]:
                anti_reflect = True
                break
            elif anti_reflect.lower() in ["no","n"]:
                anti_reflect = False
                break
            else:
                print("Invalid response. Please try again.")
        
        while True:
            # while loop to determine what to set sun as.
            sun = input("Does the eyewear have sun protection? Y/N \n **Sun protection is: \n-Polarized Lens\n-Non-polarized Tinted Lens\n-Light-reactive or Transition Lens\n").lower()
            if sun in ["yes","y","ye"]:
                sun = self._select_sun()
                break
            elif sun in ["no","n"]:
                sun = None
                break
            else:
                print("Invalid response. Please try again.")
        other = input("Does the eyewear have bluelight blocker or smartscreen?\n").lower()
        while True:
            if other in ["yes","y","ye"]:
                other = "blu"
                break
            elif other in ["no","n"]:
                other = None
                break
            else:
                print("Invalid response. Please try again.")
        return {"antireflect":anti_reflect,"sun":sun,"other":other}
    def _select_sun(self):
        while True:
            sun = input("Is it Polarized(P), non-polarized tint(N), or light-reactive(L)\n").lower()
            if re.search(select["polar"], sun):
                return "pol"
            elif re.search(select["polar"], sun):
                return "tin"
            elif re.search(select["trans"], sun):
                return "tra"
            else:
                print("Invalid response. Please try again.")
