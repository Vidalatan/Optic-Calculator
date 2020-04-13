regs = {
    "single":"(?i)\A(si?n?g?l?e?v?)$",
    "multifo":"(?i)\A(mu?l?t?i?p?l?e? ?-?f?o?c?a?l?s?)$",
    "lined":"(?i)\A(li?n?e?d?)$",
    "noline":"(?i)(\A(no?))|(\A(pr?o?g?r?e?s?s?i?v?e?)$)",
    "linebi":"(?i)\A(bi? ?-?f?o?c?a?l?)$",
    "linetri":"(?i)\A(tr?i? ?-?f?o?c?a?l?)$",
    "standpro":"(?i)\A(st?a?n?d?a?r?d?)$",
    "prempro":"(?i)\A(pr?e?m?i?u?m?)$",
    "digipro":"(?i)\A(di?g?i?t?a?l?)$",
    "polar":"(?i)\A(po?l?a?r?i?z?e?d?)$",
    "tint":"((?i)\A(no?n? ?-?p?o?l?a?r?i?z?e?d?)$)|((?i)\A(ti?n?t?)$)",
    "trans":"((?i)\A(tr?a?n?s?i?t?i?o?n?s?)$)|((?i)\A(li?g?h?t? ?-?r?e?a?c?t?i?v?e?)$)",
    "cr39":"((?i)\A(cr? ?-?3?9?)$)|((?i)\A(pl?a?s?t?i?c?)$)",
    "poly":"(?i)\A(po?l?y?c?a?r?b?o?n?a?t?e?)$",
    "hi167":"(?i)\A(hi?g?h? ?-?i?n?d?e?x? ?1?.?6?7?)$"
}
"""
The primary goal of these expressions is to find at least one match for
the terms that apply to the applicable variable, and provide some exclusion
to other terms.

--------BELOW ARE THE LIST OF LENS REGEX---------

single = "(?i)\A(si?n?g?l?e?v?)$"
searches for single vision terms. This will return a match for any string
that contains the term "single" at the beginning with any shortening.

multifocal = "(?i)\A(mu?l?t?i?p?l?e? ?-?f?o?c?a?l?s?)$"
searches for multifocal terms
this will return a match for
["multi", "multifocal","multi focal","multi-focal", "mf", "m"]

lined = "(?i)\A(li?n?e?d?)$"
searches for lined multifocal terms
this will return a match for
["line", "lined","li", "l"] as long as it is at the front of the string

noline = "(?i)(\A(no?))|(\A(pr?o?g?r?e?s?s?i?v?e?)$)"
searches for no lined multifocal terms"
this will return a match as long as the user includes "n" or "no"
or if the term "progressive" is entered at the beginning with any shortening

linebi = "(?i)\A(bi? ?-?f?o?c?a?l?)$"
searches for bifocal terms
this will return a match for
["bifocal","bi focal","bi-focal","bi","b"]
*focal can be shortened as long as spelling retains original order

linetri = "(?i)\A(tr?i? ?-?f?o?c?a?l?)$"
searches for trifocal terms
this will return a match for
["trifocal","tri focal","tri-focal","tri","t"]
*focal can be shortened as long as spelling retains original order

standpro = "(?i)\A(st?a?n?d?a?r?d?)$"
searches for standard progresssive terms
this will return a match for
any string that contains "standard" or any shortening of the word
at the begining of the string.

prempro = "(?i)\A(pr?e?m?i?u?m?)$"
searches for premium progressive terms
this will return a match for
any string that contains "premium" or any shortening of the word
at the beginning of the string.

digipro = "(?i)\A(di?g?i?t?a?l?)$"
searches for digital progressive terms
this will return a match for
any string that contains "digital" or any shortening of the word
at the beginning of the string.

---------BELOW ARE A LIST OF SUN REGEX----------

polar = "(?i)\A(po?l?a?r?i?z?e?d?)$"
searches for polarlized terms
this will return a match for
any string that contains "polarized" or any shortening of the word
at the beginning of the string

tint = "((?i)\A(no?n? ?-?p?o?l?a?r?i?z?e?d?)$)|((?i)\A(ti?n?t?)$)"
searches for non-polarized terms
this will return a match for
any string that contains "non-polarized" or any shortening of the word
at the beginning of the string

trans = "((?i)\A(tr?a?n?s?i?t?i?o?n?s?)$)|((?i)\A(li?g?h?t? ?-?r?e?a?c?t?i?v?e?)$)"
searches for light-reactive terms
this will return a match for any string
that contains "light-reactive" or "transition", or any shortening of the words
at the beginning of the string

----------BELOW ARE A LIST OF MATERIAL REGEX------------

cr39 = "((?i)\A(cr? ?-?3?9?)$)|((?i)\A(pl?a?s?t?i?c?)$)"
searches for cr39/plastic terms
this will return a match for
any string that contains "cr-39" or plastic, or anyshortening of the words
at the beginning of the string

poly = "(?i)\A(po?l?y?c?a?r?b?o?n?a?t?e?)$"
searches for polycarbonate terms
this will return a match for
any string that contains "polycarbonate" or any shortening of the word
at the beginning of the string

hi167 = "(?i)\A(hi?g?h? ?-?i?n?d?e?x? ?1?.?6?7?)$"
searches for high-index 1.67 terms
this will return a match for
any string that contains "high-index 1.67" or any shortening of the word
at the beginning of the string
"""