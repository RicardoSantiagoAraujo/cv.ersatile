from classes.sections.popScience import PopScience # type: ignore
from datetime import date

contentDict_full_en = {
    "example": PopScience(
        title=("", "Organisation of workshop"),
        initiative=("Initiative", "PopSci Project"),
        startDate=("Start",date(2022, 9, 15)),
        endDate=("End",""),
        location=("Location", "London, England"),
        columnsDef=("", "|p{1.5cm} | X | p{2.5cm}| p{3.5cm}|"),
        include=("","true"),
        content=("Content",
            "Major role in the organisation of a popular science workshop."
            ),
    ),
}
