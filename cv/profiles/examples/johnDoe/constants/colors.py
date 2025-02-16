from classes.settings.generationSettings import GenerationSettings # type: ignore
from classes.constants.colors import Colors # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={
        "tex":"",
        "scss":""
        },
    subtemplates={},
)

contentDict_full_en = {
    "example": Colors(
        colorPrimary= ("HTML", "000FF0"),
        colorSecondary= ("rgb", "0,1,1"),
        black= ("rgb", "0,0,0"),
        grayDark= ("rgb", "0.5,5,1"),
        grayMed= ("HTML", "FFFF00"),
        grayLight= ("HTML", "00FF00"),
        bgColor= ("rgb", "1,0.9,1"),
        textColor= ("rgb", "0,0,0"),
        sectionTitleColor=("rgb","0.1,9,0"),
        iconColor=("rgb","1,0.5,0.25"),
        colorTableBorders=("rgb","1,0.5,0.25"),
        colorTableFill=("rgb","1,0.5,0.25"),
        sectionTitleBgColor=("rgb","1,0.5,0.25")
    )
    }