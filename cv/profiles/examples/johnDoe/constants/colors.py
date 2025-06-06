from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.constants.Colors import Colors  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"tex": "", "scss": ""},
    subtemplates={},
)

contentDict_full_en = {
    "example": Colors(
        # base colors
        colorPrimary=("HTML", "000000"),
        colorSecondary=("rgb", "0,0,0"),
        colorBlack=("rgb", "0,0,0"),
        colorWhite=("rgb", "1,1,1"),
        colorGrayDark=("rgb", "0.1,0.1,0.1"),
        colorGrayMed=("rgb", "0.5,0.5,0.5"),
        colorGrayLight=("rgb", "0.8,0.8,0.8"),
        # semantic colors
        colorSuccess=("HTML", "00FF00"),
        colorWarning=("HTML", "990000"),
        colorDanger=("HTML", "FF0000"),
        # component colors
        colorBg=("rgb", "1,0.99,1"),
        colorText=("rgb", "0,0,0"),
        colorSectionTitle=("rgb", "0,0,0"),
        colorIcon=("rgb", "0.3,0.2,0.2"),
        colorIconBg=("", "colorBg"),
        colorTableFill=("rgb", "0.8, 0.9, 0.9"),
        colorTableBorders=("", "colorTableFill"),
        colorSectionTitleBg=("rgb", "0.85, 0.95, 0.95"),
        colorSectionBg=("", "colorBg"),
        colorHeaderBg=("", "colorBg"),
        comment=("", "Color palette for JohnDoe"),
    )
}
