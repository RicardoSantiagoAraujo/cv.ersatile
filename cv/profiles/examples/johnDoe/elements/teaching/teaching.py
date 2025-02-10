from classes.teaching import Teaching # type: ignore
from datetime import date

contentDict_full_en = {
    "example": Teaching(
        TEACH_title={"Position": "UX design course teaching assistant"},
        TEACH_institute={"": ""},
        TEACH_startDate={"Start":date(2018, 1, 1)},
        TEACH_endDate={"End":date(2019,1,1)},
        TEACH_location={"Location": "Bristol, UK"},
        TEACH_columnsDef={"": "|p{1.5cm} | X | p{2.5cm}| p{9cm}|"},
        TEACH_include={"":"true"},
        TEACH_content={"Content":
            "Assisted first year students in practical courses."
            },
    ),
}
