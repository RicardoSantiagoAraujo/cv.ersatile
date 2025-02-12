class Colors:
    def __init__(self,
                colorPrimary: tuple[str, str],
                colorSecondary: tuple[str, str],
                black:tuple[str, int],
                grayDark:tuple[str, int],
                grayMed: tuple[str, int],
                grayLight:tuple[str, str],
                bgColor: tuple[str, str],
                textColor: tuple[str, str]
                 ):
        self.CONST_colorPrimary = colorPrimary
        self.CONST_colorSecondary = colorSecondary
        self.CONST_black = black
        self.CONST_grayDark = grayDark
        self.CONST_grayMed = grayMed
        self.CONST_grayLight = grayLight
        self.CONST_bgColor = bgColor
        self.CONST_textColor = textColor

        def replaceCommaWithSpaceInValue(tuple):
            return ("" , tuple[0].replace(","," "))

        self.CONST_colorPrimary_scss = replaceCommaWithSpaceInValue(colorPrimary)
        self.CONST_colorSecondary_scss = replaceCommaWithSpaceInValue(colorSecondary)
        self.CONST_black_scss = replaceCommaWithSpaceInValue(black)
        self.CONST_grayDark_scss = replaceCommaWithSpaceInValue(grayDark)
        self.CONST_grayMed_scss = replaceCommaWithSpaceInValue(grayMed)
        self.CONST_grayLight_scss = replaceCommaWithSpaceInValue(grayLight)
        self.CONST_bgColor_scss = replaceCommaWithSpaceInValue(bgColor)
        self.CONST_textColor_scss = replaceCommaWithSpaceInValue(textColor)
