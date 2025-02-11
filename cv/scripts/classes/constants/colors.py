class Color:
    def __init__(self,
                colorPrimary: dict[str, str],
                colorSecondary: dict[str, str],
                black:dict[str, int],
                grayDark:dict[str, int],
                grayMed: dict[str, int],
                grayLight:dict[str, str],
                bgColor: dict[str, str],
                textColor: dict[str, str]
                 ):
        self.CONST_colorPrimary = colorPrimary
        self.CONST_colorSecondary = colorSecondary
        self.CONST_black = black
        self.CONST_grayDark = grayDark
        self.CONST_grayMed = grayMed
        self.CONST_grayLight = grayLight
        self.CONST_bgColor = bgColor
        self.CONST_textColor = textColor
