from classes.experience import Experience
from datetime import date
contentDict = {
    "livingpackets": Experience(
        EXP_postTitle={"Title": "Data analyst"},
        EXP_employer={"Employer": "Living Packets"},
        EXP_startDate={"Start":date(2025, 2, 24)},
        EXP_endDate={"End":date.today()},
        EXP_location={"Location": "Nantes"},
        EXP_content={"Content":"Content goes here"},
    ),
    "soprasteria": Experience(
        EXP_postTitle={"Title": "Software Enginner"},
        EXP_employer={"Employer": "Sopra Steria"},
        EXP_startDate={"Start":date(2023, 1, 14)},
        EXP_endDate={"End":date(2025, 1, 14)},
        EXP_location={"Location": "Toulouse"},
        EXP_content={"Content":"Content goes here"},
    ),
    "phd": Experience(
        EXP_postTitle={"Title": "PhD Student"},
        EXP_employer={"Funding": "CNRS"},
        EXP_startDate={"Start":date(2019, 10, 1)},
        EXP_endDate={"End":date(2023, 4, 1)},
        EXP_location={"Location": "Toulouse"},
        EXP_content={"Content":"Content goes here"},
    ),
}
