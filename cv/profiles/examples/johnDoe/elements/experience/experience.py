from classes.experience import Experience # type: ignore
from datetime import date

contentDict = {
    "experienceA": Experience(
        EXP_postTitle={"": "Software Engineer"},
        EXP_employer={"Company": "Dynamic Startup"},
        EXP_startDate={"Start":date(2025, 2, 24)},
        EXP_endDate={"End":date.today()},
        EXP_location={"Location": "London, England"},
        EXP_columnsDef={"": "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"},
        EXP_include={"":"true"},
        EXP_content={"Content":
            '''
            \\begin{customlist}
                \item Contributed to three projects using Node.js, React, SQL, and Git for version control.
                \item Development of critical features for the frontend and database management.
                \item Significant optimization of application performance.
            \end{customlist}
            '''
            },
    ),
    "experienceB": Experience(
        EXP_postTitle={"": "Frontend Developer"},
        EXP_employer={"Company": "Large corporation"},
        EXP_startDate={"Start":date(2025, 2, 24)},
        EXP_endDate={"End":date.today()},
        EXP_location={"Location": "Bristol, UK"},
        EXP_columnsDef={"": "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"},
        EXP_include={"":"true"},
        EXP_content={"Content":
            '''
           \\begin{customlist}
                \item Worked on UX and UI features for three different projects.
                \item Used Sass and Tailwind to build professional websites.
                \item Collaborated closely with an international team, alongside key stakeholders, within the Agile SCRUM framework.
            \end{customlist}
            '''
            },
    ),
}
