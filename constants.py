class ReConstants:
    # the primary goal of these expressions is to find at least one match for
    # the terms that apply to the applicable variable, and provide some exclusion
    # to other terms.

    sin = "(?i)\A(si?n?g?l?e?v?)$"
    # searches for single vision terms
    # this will return a match for
    # any string that contains the term "single" at the beginning with any shortening

    mul = "(?i)\A(mu?l?t?i?p?l?e? ?-?f?o?c?a?l?)$"
    # searches for multifocal terms
    # this will return a match for
    # ["multi", "multifocal","multi focal","multi-focal", "mf", "m"]

    line = "(?i)\A(li?n?e?d?)$"
    # searches for lined multifocal terms
    # this will return a match for
    # ["line", "lined","li", "l"] as long as it is at the front of the string

    noli = "(?i)(\A(no?))|(\A(pr?o?g?r?e?s?s?i?v?e?)$)"
    # searches for no lined multifocal terms"
    # this will return a match as long as the user includes "n" or "no"
    # or if the term "progressive" is entered at the beginning with any shortening

    lbi = "(?i)\A(bi? ?-?f?o?c?a?l?)$"
    # searches for bifocal terms
    # this will return a match for
    # ["bifocal","bi focal","bi-focal","bi","b"]
    # *focal can be shortened as long as spelling retains original order

    ltr = "(?i)\A(tr?i? ?-?f?o?c?a?l?)$"
    # searches for trifocal terms
    # this will return a match for
    # ["trifocal","tri focal","tri-focal","tri","t"]
    # *focal can be shortened as long as spelling retains original order

    spr = "(?i)\A(st?a?n?d?a?r?d?)$"
    # searches for standard progresssive terms
    # this will return a match for
    # any string that contains "standard" or any shortening of the word
    # at the begining of the string.

    ppr = "(?i)\A(pr?e?m?i?u?m?)$"
    # searches for premium progressive terms
    # this will return a match for
    # any string that contains "premium" or any shortening of the word
    #at the beginning of the string.

    dpr = "(?i)\A(di?g?i?t?a?l?)$"
    # searches for digital progressive terms
    # this will return a match for
    # any string that contains "digital" or any shortening of the word
    # at the beginning of the string.
