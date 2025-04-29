from scripts.classes.settings.generationSettings import GenerationSettings  # type: ignore
from scripts.classes.constants.colors import Colors  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"tex": "", "scss": ""},
    subtemplates={},
)

contentDict_full_en = {
    "example": Colors(
        colorPrimary=("HTML", "000FF0"),
        colorSecondary=("rgb", "0,1,1"),
        colorBlack=("rgb", "0,0,0"),
        colorWhite=("rgb", "1,1,1"),
        colorGrayDark=("rgb", "0.5,5,1"),
        colorGrayMed=("HTML", "FFFF00"),
        colorGrayLight=("HTML", "00FF00"),
        colorBg=("rgb", "1,0.9,1"),
        colorText=("rgb", "0,0,0"),
        colorSectionTitle=("rgb", "0.1,9,0"),
        colorIcon=("rgb", "1,0.5,0.25"),
        colorIconBg=("", "colorBg"),
        colorTableBorders=("rgb", "1,0.5,0.25"),
        colorTableFill=("rgb", "1,0.5,0.25"),
        colorSectionTitleBg=("rgb", "1,0.5,0.25"),
        colorSectionBg=("", "colorBg"),
        colorHeaderBg=("", "colorBg"),
        comment=("", "Color palette for JohnDoe"),
    )
}
