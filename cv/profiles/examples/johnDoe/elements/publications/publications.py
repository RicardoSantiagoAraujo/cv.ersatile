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
        comment=("", "Example of publication from profile's own publication list (<profile>/assets/bibliography_files/my_publications.bib)"),
        hyperlink=("", ""),
    ),
    "example2": Publication(
        key=("", "publicationToReference"),
        fullText=("", ""),
        include=("", "true"),
        comment=("", "Example of publication from profile's referenced publication list (<profile>/assets/bibliography_files/bibliography.bib)"),
        hyperlink=("", ""),
    ),
    "example3": Publication(
        key=("", ""),
        fullText=("", "John Doe (Feb. 2023). The Joy of Fullstack Developing"),
        include=("", "true"),
        comment=("", "Example of publication created here directly"),
        hyperlink=("", ""),
    ),
    "example4": Publication(
        key=("", "laland_how_2010"),
        fullText=("", ""),
        include=("", "true"),
        comment=("", "Example of publication from bibliography shared between profiles (cv/assets/bibliography_files/shared_bibliography)"),
        hyperlink=("", ""),
    ),

}
