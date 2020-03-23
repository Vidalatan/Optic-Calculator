from constants import ReConstants as rcon
import re

class Eyewear:
    def __init__(self):
        self.lens = self.select_lens()
        self.material = self.select_material()
        self.options = self.select_options()
    def __str__(self):
        return f"The eyewear is {self.lens} vision. It is made of {self.material}. Anti-reflective {self.options['antireflect']}. Sunglass is {self.options['sun']} It has {self.options['other']}."
    def select_lens(self):
        # instance method for determining the lens of an eyewear.
        lens = None
        while lens not in ["sin","lbi","ltr","spr","ppr","dpr"]:
            lens = input("Single Vision (SV) or Multifocal (MF)\n").lower()
            if re.search(rcon.sin, lens):
                #if the lens is single vision set lens to sin. End of probe.
                lens = "sin"
                print("Single Vision selected.")

            elif re.search(rcon.mul, lens):
                #if the lens is multifocal, continue probing for type of multifocal.
                lens = input("Multifocal\n\tIs this a lined(L) or no lined(NL) multifocal lens?\n").lower()
                if re.search(rcon.line, lens):
                    #if lens is lined multifocal, probe for bi or tri focal type.
                    lens = input("Lined\n\tIs it bifocal(B) or trifocal(T)?\n").lower()
                    if re.search(rcon.lbi, lens):
                        #if lens is lined bifocal, set lens to lbi
                        lens = "lbi"
                        print("Lined-Bifocal Vision selected.")

                    elif re.search(rcon.ltr, lens):
                        #if lens is lined trifocal, set lens to ltr
                        lens = "ltr"
                        print("Lined-Trifocal Vision selected.")

                    else:
                        print("Invalid response. Please try again.")
                        continue
                elif re.search(rcon.noli, lens):
                    #if the lens is a no-line multifocal, probe for standard, premium, or digital.
                    lens = input("No-Line\n\tIs this a Standard(S), Premium(P), or Digital(D) progressive?\n").lower()
                    if re.search(rcon.spr, lens):
                        lens = "spr"
                        print("Standard Progressive selected.")

                    elif re.search(rcon.ppr, lens):
                        lens = "ppr"
                        print("Premium Progressive selected.")

                    elif re.search(rcon.dpr, lens):
                        lens = "dpr"
                        print("Digital Progressive selected.")

                    else:
                        print("Invalid response. Please try again")
                        continue
                else:
                    print("Invalid response. Please try again")
        return lens

    # def is_single(self, lens)
    # def is_multi(self, lens)
    # def is_line(self, lens)
    # def is_prog(self, lens)
    # def is_stand(self, lens)
    # def is_digit(self, lens)

    def select_material(self):
        material = input("What material is the lens made of?\n-CR-39(AKA Plastic)\n-Polycarobonate\nHigh-Index(AKA HI 1.67)\n").lower()
        return material

    def select_options(self):
        # instance method for determining what options were included in the eyewear.
        anti_reflect = input("Does the eyewear have an anti-reflective/anti-glare coating? Y/N\n").lower()
        while True:
            # while loop to determine what to set anti_reflect as.
            if anti_reflect.lower() in ["yes","ye","y"]:
                anti_reflect = True
                break
            elif anti_reflect.lower() in ["no","n"]:
                anti_reflect = False
                break
            else:
                print("Invalid response. Please try again.")
        sun = input("Does the eyewear have sun protection? Y/N \n **Sun protection is: \n-Polarized Lens\n-Non-polarized Tinted Lens\n-Light-reactive or Transition Lens\n").lower()
        while True:
            # while loop to determine what to set sun as.
            if sun in ["yes","y","ye"]:
                sun = self.select_sun()
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
    def select_sun(self):
        sun = input("Is it Polarized(P), non-polarized tint(N), or light-reactive(L)\n").lower()
        while True:
            if sun in ["polarized","polarize","polar","pol","p"]:
                return "pol"
            elif sun in ["non","non-polar","nonpolar","no polar","nopolar",
                               "nonpolarized","non-polarized","tint","non-polarized tint",
                              "nonpolarized tint","nonpolarizedtint","n","t"]:
                return "tin"
            elif sun in ["light","reactive","light-reactive","lightreactive","light reactive","l"
                                "transition","trans","t"]:
                return "tra"
            else:
                print("Invalid response. Please try again.")
