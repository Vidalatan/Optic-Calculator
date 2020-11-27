#--------BELOW ARE THE LIST OF LENS DEFINITIONS AND REGEX---------#

single = "Single vision. The term used to indicate that a prescription or form of eyewear has only one form of correction. This correction can be seen in the sphere^ and cylinder^ of the prescription form. A single vision lens is also considered a spherical lens."
"""
Regular expression | (?i)\A(si?n?g?l?e?)$"
searches for single vision terms. This will return a match for any string
that contains the term "single" or any shortening of the word
at the beginning of the string
"""

multifocal = "Multi-Focal vision. The term used to indicate that a prescription or form of eyewear has two or more forms of correction. The primary correction, which is usually for distance, is found in the sphere^ and cylinder^ of the prescription. The secondary correction, which is usually for some form of reading assistance, is found in the add-power^ section of the prescription. This secondary correction is almost always the same for both eyes. There is in some cases a third or tertiary correction that is in some cases reffered to as the intermediate, which is the corrective power in between the primary and secondary."
"""
Regular expression | "(?i)\A(mu?l?t?i?p?l?e? ?-?f?o?c?a?l?s?)$"
searches for multifocal terms. This will return a match for any string
that contains the term "multi-focal" or any shortening of the word(s)
at the beginning of the string.
"""


lined = "Lined multi-focal lens. The term used to indicate that a certain eyewear contains a multi-focal lens where the segregation of the primary and secondary (and sometimes third) corrections is created by a difined line roughly 5-12mm below the pupil. This is the way multi-focal lenses were traditionally created."
"""
Regular expression | "(?i)\A(li?n?e?d?)$"
searches for lined multifocal terms. This will return a match for any string
that contains the term "lined" or any shortening of the word
at the beginning of the string.
"""

noline = 'No-line multi-focal lens; AKA Progressive. The term used to indicate that a certain eyewear contains a multi-focal lens where there is no clear segregation of the primary and secondary corrections. This is often referred to as a "Progressive" lens due to the fact that it progressively increases into the secondary correction.'
"""
Regular expression | "(?i)(\A(no?))|(\A(pr?o?g?r?e?s?s?i?v?e?)$)"
searches for no-line multifocal terms. This will return a match for any string
that contains the term "no-line" or "progressive" or any shortening of the word(s)
at the beginning of the string.
"""

linebi = "Lined Bi-focal. The term used to indicate that a certain eyewear contains a multi-focal lens where there are only two corrections separated by a line."
"""
Regular expression | "(?i)\A(bi? ?-?f?o?c?a?l?)$"
searches for bifocal terms. This will return a match for any string
that contains the term "bi-focal" or any shortening of the word
at the beginning of the string.
"""

linetri = "Lined Tri-focal. The term used to indicate that a certain eyewear contains a multi-focal lens where there is three corrections separated by a line."
"""
Regular expression | "(?i)\A(tr?i? ?-?f?o?c?a?l?)$"
searches for trifocal terms. This will return a match for any string
that contains the term "tri-focal" or any shortening of the word
at the beginning of the string.
"""

standpro = "Standard Progressive. The term used to indicate that a certain eyewear contains a multi-focal lens where there are three corrections with no distinct separation. A standard progressive has the narrowest corridor."
"""
Regular expression | "(?i)\A(st?a?n?d?a?r?d?)$"
searches for standard progresssive terms. This will return a match for
any string that contains "standard" or any shortening of the word
at the begining of the string.
"""

prempro = "Premium Progressive. The term used to indicate that a certain eyewear contains a multi-focal lens where there are three corrections with no disctinct separation. A premium progressive has an average corridor size."
"""
Regular expression | "(?i)\A(pr?e?m?i?u?m?)$"
searches for premium progressive terms. This will return a match for
any string that contains "premium" or any shortening of the word
at the beginning of the string.
"""

digipro = "Dital Progressive. The term used to indicate that a certain eyewear contains a multi-focal lens where there are three corrections with no disctinct separation. A digital progressive has the widest corridor size, and has a compensated prescription."
"""
Regular expression | "(?i)\A(di?g?i?t?a?l?)$"
searches for digital progressive terms. This will return a match for
any string that contains "digital" or any shortening of the word
at the beginning of the string.
"""

#---------BELOW ARE A LIST OF SUN REGEX AND DEFINITIONS----------#

polar = "Polarization. The term used to indicate that a certain eyewear contains a lens that is polarized. Polarization works to eliminate percieved glare by filtering out light that is reflected by most objects. Polarization is specific to sunglass eyewear, this is not the same as anti-glare, or anti-reflective, coatings."
"""
Regular expression | "(?i)\A(po?l?a?r?i?z?e?d?)$"
searches for polarlized terms. This will return a match for
any string that contains "polarized" or any shortening of the word
at the beginning of the string
"""

tint = "Tint. The term used to indicate that a certain eyewear contains a lens that has been tinted. Tints are just dyes applied to the surface of the lens to add shade or color to the lens. It is most common to see tint applied to a lens to create non-polarized sunglasses, as long as the lens still contains a UV filtering coating."
"""
Regular expression | "((?i)\A(no?n? ?-?p?o?l?a?r?i?z?e?d?)$)|((?i)\A(ti?n?t?)$)"
searches for non-polarized terms. This will return a match for
any string that contains "non-polarized" or any shortening of the word
at the beginning of the string
"""

trans = "Transition/Light-Reactive. The term used to indicate that a certain eyewear contains a lens that darkens in direct sunlight. Light-reactive lenses come in a few color options, as well as shades of maximum darkness. The optimal use of a Transition lens is for patients who will use their eyewear both indoors and outdoors, and would prefer not to swap between two different glasses."
"""
Regular expression | "((?i)\A(tr?a?n?s?i?t?i?o?n?s?)$)|((?i)\A(li?g?h?t? ?-?r?e?a?c?t?i?v?e?)$)"
searches for light-reactive terms. This will return a match for any string
that contains "light-reactive" or "transition", or any shortening of the word(s)
at the beginning of the string
"""

#----------BELOW ARE A LIST OF MATERIAL REGEX AND DEFINITIONS------------#

cr39 = "CR39/Plastic. The term used to indicate that a certain eyewear contains a lens made out of CR39 plastic. This material has the highest ABBE value of the three offered, meaning it is the clearest lens we have. The main drawback to a CR39 lens is that it is not very durable, and is much easier to scratch or damage."
"""
Regular expression | "((?i)\A(cr? ?-?3?9?)$)|((?i)\A(pl?a?s?t?i?c?)$)"
searches for cr39/plastic terms. This will return a match for
any string that contains "cr-39" or plastic, or anyshortening of the word(s)
at the beginning of the string
"""

poly = "Polycarbonate. The term used to indicate that a certain eyewear contains a lens made of a polycarbonate material. This material is the most durable and damage resistant by far. It is impossible to chip, crack, or break a polycarbonate lens by normal means."
"""
Regular expression | "(?i)\A(po?l?y?c?a?r?b?o?n?a?t?e?)$"
searches for polycarbonate terms. This will return a match for
any string that contains "polycarbonate" or any shortening of the word
at the beginning of the string
"""

hi167 = "High Index 1.67. The term used to indicate a certain eyewear contains a lens made of a high-index material with a 1.67 rating. This material has the highest refractive index rate, which means that it bends light more efficiently and effectively; This ultimately means that you need less lens for a higher correction, which makes higher prescriptions less dramatic in thickness."
"""
Regular expression | "(?i)\A(hi?g?h? ?-?i?n?d?e?x? ?1?.?6?7?)$"
searches for high-index 1.67 terms. This will return a match for
any string that contains "high-index 1.67" or any shortening of the word
at the beginning of the string.
"""

terms = {
    "single":["(?i)\A(si?n?g?l?e?v?)$",single],
    "multifocal":["(?i)\A(mu?l?t?i?p?l?e? ?-?f?o?c?a?l?s?)$",multifocal],
    "lined":["(?i)\A(li?n?e?d?)$",lined],
    "noline":["(?i)(\A(no?))|(\A(pr?o?g?r?e?s?s?i?v?e?)$)",noline],
    "linebi":["(?i)\A(bi? ?-?f?o?c?a?l?)$",linebi],
    "linetri":["(?i)\A(tr?i? ?-?f?o?c?a?l?)$",linetri],
    "standpro":["(?i)\A(st?a?n?d?a?r?d?)$",standpro],
    "prempro":["(?i)\A(pr?e?m?i?u?m?)$",prempro],
    "digipro":["(?i)\A(di?g?i?t?a?l?)$",digipro],
    "polar":["(?i)\A(po?l?a?r?i?z?e?d?)$",polar],
    "tint":["((?i)\A(no?n? ?-?p?o?l?a?r?i?z?e?d?)$)|((?i)\A(ti?n?t?)$)",tint],
    "trans":["((?i)\A(tr?a?n?s?i?t?i?o?n?s?)$)|((?i)\A(li?g?h?t? ?-?r?e?a?c?t?i?v?e?)$)",trans],
    "cr39":["((?i)\A(cr? ?-?3?9?)$)|((?i)\A(pl?a?s?t?i?c?)$)",cr39],
    "poly":["(?i)\A(po?l?y?c?a?r?b?o?n?a?t?e?)$",poly],
    "hi167":["(?i)\A(hi?g?h? ?-?i?n?d?e?x? ?1?.?6?7?)$",hi167]
}
"""
The primary goal of these expressions is to find at least one match for
the terms that apply to the applicable variable, and provide some exclusion
to other terms.
"""