class Colors:
    def __init__(
        self,
        #### Semantic colors
        colorPrimary: tuple[str, str],
        colorSecondary: tuple[str, str],
        black: tuple[str, int],
        grayDark: tuple[str, int],
        grayMed: tuple[str, int],
        grayLight: tuple[str, str],
        #### Component colors
        bgColor: tuple[str, str],
        textColor: tuple[str, str],
        sectionTitleColor: tuple[str, str],
        iconColor: tuple[str, str],
        colorTableBorders: tuple[str, str],
        colorTableFill: tuple[str, str],
        sectionTitleBgColor: tuple[str, str],

    ):
        # Semantic colors
        self.CONST_colorPrimary = colorPrimary
        self.CONST_colorSecondary = colorSecondary
        self.CONST_black = black
        self.CONST_grayDark = grayDark
        self.CONST_grayMed = grayMed
        self.CONST_grayLight = grayLight
        # Component colors
        self.CONST_bgColor = bgColor
        self.CONST_textColor = textColor
        self.CONST_sectionTitleColor = sectionTitleColor
        self.CONST_iconColor= iconColor
        self.CONST_colorTableBorders= colorTableBorders
        self.CONST_colorTableFill= colorTableFill
        self.CONST_sectionTitleBgColor= sectionTitleBgColor

        # Adjusting for SCSS
        def replaceCommaWithSpaceInValue(colorKV: tuple):
            if colorKV[0] == "rgb":
                return ("", f'color(srgb {colorKV[1].replace(","," ")} )')
            if colorKV[0] == "HTML":
                return ("", f"#{colorKV[1]}")
            return "INVALID COLOR KEY"
        self.CONST_colorPrimary_scss = replaceCommaWithSpaceInValue(colorPrimary)
        self.CONST_colorSecondary_scss = replaceCommaWithSpaceInValue(colorSecondary)
        self.CONST_black_scss = replaceCommaWithSpaceInValue(black)
        self.CONST_grayDark_scss = replaceCommaWithSpaceInValue(grayDark)
        self.CONST_grayMed_scss = replaceCommaWithSpaceInValue(grayMed)
        self.CONST_grayLight_scss = replaceCommaWithSpaceInValue(grayLight)
        self.CONST_bgColor_scss = replaceCommaWithSpaceInValue(bgColor)
        self.CONST_textColor_scss = replaceCommaWithSpaceInValue(textColor)
        self.CONST_sectionTitleColor_scss = replaceCommaWithSpaceInValue(sectionTitleColor)
        self.CONST_iconColor_scss = replaceCommaWithSpaceInValue(iconColor)
        self.CONST_colorTableBorders_scss = replaceCommaWithSpaceInValue(colorTableBorders)
        self.CONST_colorTableFill_scss = replaceCommaWithSpaceInValue(colorTableFill)
        self.CONST_sectionTitleBgColor_scss = replaceCommaWithSpaceInValue(sectionTitleBgColor)
