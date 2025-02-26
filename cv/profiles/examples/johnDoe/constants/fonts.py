from classes.settings.generationSettings import GenerationSettings # type: ignore
from classes.constants.fonts import Fonts # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={
        "tex":"",
        "scss":""
        },
    subtemplates={},
)

contentDict_full_en = {
    "example": Fonts(
        mainFont= ("", "Arial"),
        titleFont= ("", "Times New Roman"),
        subtitleFont=("", "Times New Roman"),
        mainFontBackup= ("", "Times New Roman"),
        titleFontBackup= ("", "Times New Roman"),
        subtitleFontBackup=("", "Times New Roman"),
        comment=("", "Fonts for johnDoe"),
    )
    }