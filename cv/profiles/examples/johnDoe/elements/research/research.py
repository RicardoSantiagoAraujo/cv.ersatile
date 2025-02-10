from classes.research import Research # type: ignore
from datetime import date

contentDict_full_en = {
    "example": Research(
        RES_title={"": ""},
        RES_institute={"": "CS Institute"},
        RES_startDate={"Start":date(2019, 1, 11)},
        RES_endDate={"End":date(2019,6,1)},
        RES_location={"Location": "Manchester, UK"},
        RES_columnsDef={"": "|p{1.5cm} | X | p{2.5cm}| p{5cm}|"},
        RES_include={"":"true"},
        RES_content={"Content":
            "I did my master thesis in a computer science research laboratory."
            },
    ),
}
