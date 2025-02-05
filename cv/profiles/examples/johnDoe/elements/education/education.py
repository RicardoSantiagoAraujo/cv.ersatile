from classes.education import Education # type: ignore
from datetime import date

contentDict = {
    "educationA": Education(
        EDU_level={"": "Master in Computer Science"},
        EDU_institution={"University": "University of Bristol"},
        EDU_startDate={"Start":date(2022, 1, 1)},
        EDU_endDate={"End":""},
        EDU_location={"Location": "London, England"},
        EDU_columnsDef={"": "|p{2cm} | X | p{2.5cm}| p{6cm}|"},
        EDU_include={"":"true"},
        EDU_content={"Content":
            [
                "Contributed to three projects using Node.js, React, SQL, and Git for version control.",
                "Development of critical features for the frontend and database management.",
                "Significant optimization of application performance.",
            ]
            },
    ),
    "educationB": Education(
        EDU_level={"": "Frontend Developer"},
        EDU_institution={"Company": "Large corporation"},
        EDU_startDate={"Start":date(2014, 1, 1)},
        EDU_endDate={"End":date(2022, 6, 1)},
        EDU_location={"Location": "Bristol, UK"},
        EDU_columnsDef={"": "|p{2cm} | X | p{2.5cm}| p{6cm}|"},
        EDU_include={"":"true"},
        EDU_content={"Content":
            [
                "Worked on UX and UI features for three different projects.",
                "Used Sass and Tailwind to build professional websites.",
                "Collaborated closely with an international team, alongside key stakeholders, within the Agile SCRUM framework.",
            ]
            },
    ),
}
