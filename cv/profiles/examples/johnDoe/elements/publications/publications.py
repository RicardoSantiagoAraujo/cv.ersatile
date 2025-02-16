from classes.settings.generationSettings import GenerationSettings # type: ignore
from classes.sections.publications import Publication # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={
        "html":"",
        "tex":""
        },
    subtemplates={
        "html":"",
        "tex":""
        },
)

contentDict_full_en = {
    "example1": Publication(
        key=("", "mypublications:johnDoe"),
        fullText=("", "Entry contents"),
        include=("","true"),
        hyperlink=("",""),
    ),
    "example2": Publication(
        key=("", ""),
        fullText=("", "John Doe (Feb. 2023). “The Joy of Fullstack Developing”"),
        include=("","true"),
        hyperlink=("",""),
    ),
}
