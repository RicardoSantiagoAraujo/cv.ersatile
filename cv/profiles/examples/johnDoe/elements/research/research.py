from classes.sections.research import Research # type: ignore
from datetime import date

contentDict_full_en = {
    "example": Research(
        title={"": ""},
        institute={"": "CS Institute"},
        startDate={"Start":date(2019, 1, 11)},
        endDate={"End":date(2019,6,1)},
        location={"Location": "Manchester, UK"},
        columnsDef={"": "|p{1.5cm} | X | p{2.5cm}| p{5cm}|"},
        include={"":"true"},
        content={"Content":
            "I did my master thesis in a computer science research laboratory."
            },
    ),
}
