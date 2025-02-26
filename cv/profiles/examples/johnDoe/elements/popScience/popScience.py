from classes.settings.generationSettings import GenerationSettings # type: ignore
from classes.sections.popScience import PopScience # type: ignore
from datetime import date

### SETTINGS
generation_settings = GenerationSettings(
    templates={
        "html":"2x2",
        "tex":"2x2"
        },
    subtemplates={
        "html":"2x2",
        "tex":"2x2"
        },
)


### CONTENTS

contentDict_full_en = {
    "example": PopScience(
        title=("", "Organisation of workshop"),
        initiative=("Initiative", "PopSci Project"),
        startDate=("Start",date(2022, 9, 15)),
        endDate=("End",""),
        location=("Location", "London, England"),
        columnsDef=("", "|p{1.5cm} | X | p{2.5cm}| p{3.5cm}|"),
        include=("","true"),
        comment=("", "COMMENT GOES HERE"),
        content=("Content",
            "Major role in the organisation of a popular science workshop."
            ),
    ),
}
