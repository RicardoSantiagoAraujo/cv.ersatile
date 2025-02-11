from classes.sections.education import Education # type: ignore
from datetime import date

contentDict_full_en = {
    "educationA": Education(
        EDU_level={"": "Master in Computer Science"},
        EDU_institution={"University": "University of Bristol"},
        EDU_startDate={"Start":date(2016, 2, 1)},
        EDU_endDate={"End": date(2016, 7, 1)},
        EDU_location={"Location": "Briston, UK"},
        EDU_columnsDef={"": "|p{0.2cm} | X | p{2.5cm}| p{2.0cm}|"},
        EDU_include={"":"true"},
        EDU_content={"Content":""
            },
    ),
    "educationB": Education(
        EDU_level={"": "Bachelor in Computer Science"},
        EDU_institution={"University": "UCL"},
        EDU_startDate={"Start":date(2013, 9, 1)},
        EDU_endDate={"End":date(2026, 7, 1)},
        EDU_location={"Location": "London, UK"},
        EDU_columnsDef={"": "|p{0.2cm} | X | p{2.5cm}| p{2.0cm}|"},
        EDU_include={"":"true"},
        EDU_content={"Content":"First rank honors in class."
            },
    ),
}
