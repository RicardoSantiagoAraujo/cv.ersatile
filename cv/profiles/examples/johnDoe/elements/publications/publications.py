from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.Publications import Publication  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"html": "", "tex": ""},
    subtemplates={"html": "", "tex": ""},
)

contentDict_full_en = {
    "example1": Publication(
        key=("", "mypublications:johnDoe"),
        fullText=("", "Entry contents"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        hyperlink=("", ""),
    ),
    "example2": Publication(
        key=("", ""),
        fullText=("", "John Doe (Feb. 2023). The Joy of Fullstack Developing"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        hyperlink=("", ""),
    ),
}
