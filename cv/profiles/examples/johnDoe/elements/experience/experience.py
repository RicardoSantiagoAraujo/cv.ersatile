from classes.sections.experience import Experience # type: ignore
from datetime import date

contentDict_full_en = {
    "experienceA": Experience(
        postTitle={"": "Software Engineer"},
        employer={"Company": "Dynamic Startup"},
        startDate={"Start":date(2022, 1, 1)},
        endDate={"End":""},
        location={"Location": "London, England"},
        columnsDef={"": "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"},
        include={"":"true"},
        content={"Content":
            [
                "Contributed to three projects using Node.js, React, SQL, and Git for version control.",
                "Development of critical features for the frontend and database management.",
                "Significant optimization of application performance.",
            ]
            },
    ),
    "experienceB": Experience(
        postTitle={"": "Frontend Developer"},
        employer={"Company": "Large corporation"},
        startDate={"Start":date(2014, 1, 1)},
        endDate={"End":date(2022, 6, 1)},
        location={"Location": "Bristol, UK"},
        columnsDef={"": "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"},
        include={"":"true"},
        content={"Content":
            [
                "Worked on UX and UI features for three different projects.",
                "Used Sass and Tailwind to build professional websites.",
                "Collaborated closely with an international team, alongside key stakeholders, within the Agile SCRUM framework.",
            ]
            },
    ),
}
