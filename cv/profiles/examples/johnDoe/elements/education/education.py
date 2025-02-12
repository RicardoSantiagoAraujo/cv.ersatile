from classes.sections.education import Education # type: ignore
from datetime import date

contentDict_full_en = {
    "educationA": Education(
        level=("", "Master in Computer Science"),
        institution=("University", "University of Bristol"),
        startDate=("Start",date(2016, 2, 1)),
        endDate=("End", date(2016, 7, 1)),
        location=("Location", "Briston, UK"),
        columnsDef=("", "|p{0.2cm} | X | p{2.5cm}| p{2.0cm}|"),
        include=("","true"),
        content=("Content",""
            ),
    ),
    "educationB": Education(
        level=("", "Bachelor in Computer Science"),
        institution=("University", "UCL"),
        startDate=("Start",date(2013, 9, 1)),
        endDate=("End",date(2026, 7, 1)),
        location=("Location", "London, UK"),
        columnsDef=("", "|p{0.2cm} | X | p{2.5cm}| p{2.0cm}|"),
        include=("","true"),
        content=("Content","First rank honors in class."
            ),
    ),
}
