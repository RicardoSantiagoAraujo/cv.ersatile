from scripts.classes.settings.generationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.research import Research  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"html": "2x2", "tex": "2x2"},
    subtemplates={"html": "2x2", "tex": "2x2"},
)

contentDict_full_en = {
    "example": Research(
        title=("", "Computer science project"),
        institute=("", "CS Institute"),
        startDate=("Start", date(2019, 1, 11)),
        endDate=("End", date(2019, 6, 1)),
        location=("Location", "Manchester, UK"),
        columnsDef=("", "|p{1.5cm} | X | p{2.5cm}| p{5cm}|"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        content=("Content", "I did my master thesis in a computer science research laboratory."),
    ),
}
