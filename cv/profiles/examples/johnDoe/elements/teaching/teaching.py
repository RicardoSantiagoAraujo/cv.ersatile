from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.Teaching import Teaching  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"html": "2x2", "tex": "2x2"},
    subtemplates={"html": "2x2", "tex": "2x2"},
)

contentDict_full_en = {
    "example": Teaching(
        title=("Position", "UX design course teaching assistant"),
        institute=("", ""),
        startDate=("Start", date(2018, 1, 1)),
        endDate=("End", date(2019, 1, 1)),
        location=("Location", "Bristol, UK"),
        columnsDef=("", "|p{1.5cm} | X | p{2.5cm}| p{9cm}|"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        content=("Content", "Assisted first year students in practical courses."),
    ),
}
