class Colors:
    """Class to hold colors used in the CV generation to customize the look of the CV.
    This class contains base colors (primary, secondary, etc.) and component-specific colors (background, text, etc.)
    """
    def __init__(
        self,
        #### ======== Base colors
        colorPrimary: tuple[str, str],
        colorSecondary: tuple[str, str],
        colorBlack: tuple[str, int],
        colorWhite: tuple[str, int],
        colorGrayDark: tuple[str, int],
        colorGrayMed: tuple[str, int],
        colorGrayLight: tuple[str, str],
        #### ======== Semantic colors
        colorSuccess: tuple[str, str],
        colorWarning: tuple[str, str],
        colorDanger: tuple[str, str],
        #### ======== Component colors
        colorBg: tuple[str, str],
        colorText: tuple[str, str],
        # Sections
        colorSectionTitle: tuple[str, str],
        colorSectionTitleBg: tuple[str, str],
        colorSectionBg: tuple[str, str],
        # Header
        colorHeaderBg: tuple[str, str],
        colorIcon: tuple[str, str],
        colorIconBg: tuple[str, str],
        # Tables
        colorTableBorders: tuple[str, str],
        colorTableFill: tuple[str, str],
        #### ======== Meta about color palette
        comment: tuple[str, str],
    ):
        # Adjusting for TEX
        def colorForTEX(key, colorKV: tuple) -> str | tuple[str, str]:
            """ Create a LaTeX color definition for the given color.

            Args:
                key (_type_): _description_
                colorKV (tuple): tuple containing the color type and value

            Returns:
                str | tuple[str, str]: either an error warning or a tuple whose second element is the LaTeX color definition
            """
            if colorKV[0] in ["rgb", "HTML"]:
                return ("", f"\\definecolor{{{key}}}{{{colorKV[0]}}}{{{colorKV[1]}}}")
            if colorKV[0] == "":  # copy another color
                return ("", f"\\colorlet{{{key}}}{{{colorKV[1]}}}")
            return "INVALID COLOR KEY"

        # Adjusting for SCSS
        def colorForSCSS(colorKV: tuple) -> str | tuple[str, str]:
            """Create a SCSS color definition for the given color.

            Args:
                colorKV (tuple): either an error warning or a tuple whose second element is the SCSS color definition

            Returns:
            str | tuple[str, str]: either an error warning or a tuple whose second element is the SCSS color definition
            """
            if colorKV[0] == "rgb":
                return ("", f'color(srgb {colorKV[1].replace(","," ")} )')
            if colorKV[0] == "HTML":
                return ("", f"#{colorKV[1]}")
            if colorKV[0] == "":  # copy another color
                return ("", f"${colorKV[1]}")
            return "INVALID COLOR KEY"

        # Loop through local variables to generate new variables
        for key, value in locals().items():
            if key != "self" and key not in [
                "colorForTEX",
                "colorForSCSS",
                "comment",
            ]:  # Don't assign 'self' or functions
                # Dynamically assign the variable to the object
                setattr(self, f"CONST_{key}_tex", colorForTEX(key, value))
                setattr(self, f"CONST_{key}_scss", colorForSCSS(value))
            # attributes to include as is :
            if key in ["comment"]:
                setattr(self, f"CONST_{key}", value)
