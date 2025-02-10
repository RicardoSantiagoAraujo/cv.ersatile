from classes.popScience import PopScience # type: ignore
from datetime import date

contentDict_full_en = {
    "example": PopScience(
        POPSCI_title={"": "Organisation of workshop"},
        POPSCI_initiative={"Initiative": "PopSci Project"},
        POPSCI_startDate={"Start":date(2022, 9, 15)},
        POPSCI_endDate={"End":""},
        POPSCI_location={"Location": "London, England"},
        POPSCI_columnsDef={"": "|p{1.5cm} | X | p{2.5cm}| p{3.5cm}|"},
        POPSCI_include={"":"true"},
        POPSCI_content={"Content":
            "Major role in the organisation of a popular science workshop."
            },
    ),
}
