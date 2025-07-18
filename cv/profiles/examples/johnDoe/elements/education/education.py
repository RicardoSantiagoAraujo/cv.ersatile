from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.Education import Education  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"html": "2x2", "tex": "2x2"},
    subtemplates={"html": "2x2", "tex": "2x2"},
)

contentDict_full_en = {
    "educationA": Education(
        level=("", "Master in Computer Science"),
        institution=("University", "University of Bristol"),
        startDate=("Start", date(2016, 2, 1)),
        endDate=("End", date(2016, 7, 1)),
        location=("Location", "Briston, UK"),
        columnsDef=("", "|p{0.2cm} | X | p{2.5cm}| p{2.0cm}|"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        content=("Content", "Long description of the education with additional details."),
        contentShort=("Content", "Short description of the education"),
    ),
    "educationB": Education(
        level=("", "Bachelor in Computer Science"),
        institution=("University", "UCL"),
        startDate=("Start", date(2013, 9, 1)),
        endDate=("End", date(2026, 7, 1)),
        location=("Location", "London, UK"),
        columnsDef=("", "|p{0.2cm} | X | p{2.5cm}| p{2.0cm}|"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        content=("Content", "Long description of the education with additional details."),
        contentShort=("Content", "Short description of the education"),
    ),
}
