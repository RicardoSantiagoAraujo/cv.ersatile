from classes.sections.teaching import Teaching # type: ignore
from datetime import date

contentDict_full_en = {
    "example": Teaching(
        title={"Position": "UX design course teaching assistant"},
        institute={"": ""},
        startDate={"Start":date(2018, 1, 1)},
        endDate={"End":date(2019,1,1)},
        location={"Location": "Bristol, UK"},
        columnsDef={"": "|p{1.5cm} | X | p{2.5cm}| p{9cm}|"},
        include={"":"true"},
        content={"Content":
            "Assisted first year students in practical courses."
            },
    ),
}
