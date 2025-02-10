from classes.experience import Experience # type: ignore
from datetime import date

contentDict_en = {
    "experienceA": Experience(
        EXP_postTitle={"": "Software Engineer"},
        EXP_employer={"Company": "Dynamic Startup"},
        EXP_startDate={"Start":date(2022, 1, 1)},
        EXP_endDate={"End":""},
        EXP_location={"Location": "London, England"},
        EXP_columnsDef={"": "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"},
        EXP_include={"":"true"},
        EXP_content={"Content":
            [
                "Contributed to three projects using Node.js, React, SQL, and Git for version control.",
                "Development of critical features for the frontend and database management.",
                "Significant optimization of application performance.",
            ]
            },
    ),
    "experienceB": Experience(
        EXP_postTitle={"": "Frontend Developer"},
        EXP_employer={"Company": "Large corporation"},
        EXP_startDate={"Start":date(2014, 1, 1)},
        EXP_endDate={"End":date(2022, 6, 1)},
        EXP_location={"Location": "Bristol, UK"},
        EXP_columnsDef={"": "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"},
        EXP_include={"":"true"},
        EXP_content={"Content":
            [
                "Worked on UX and UI features for three different projects.",
                "Used Sass and Tailwind to build professional websites.",
                "Collaborated closely with an international team, alongside key stakeholders, within the Agile SCRUM framework.",
            ]
            },
    ),
}
