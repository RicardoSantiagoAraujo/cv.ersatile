from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.Experience import Experience, ExperienceSub  # type: ignore

from datetime import date

generation_settings = GenerationSettings(
    templates={"html": "2x2", "tex": "2x2"},
    subtemplates={"html": "2x2", "tex": "2x2"},
)

contentDict_full_en = {
    "experienceA": Experience(
        postTitle=("", "Software Engineer"),
        employer=("Company", "Dynamic Startup"),
        startDate=("Start", date(2022, 1, 1)),
        endDate=("End", ""),
        location=("Location", "London, England"),
        columnsDef=("", "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"),
        include=("", "true"),
        comment=("", ""),
        content=(
            "Content",
            [
                ExperienceSub(
                    content=(
                        "",
                        "Contributed to three projects using Node.js, React, SQL, and Git for version control.",
                    ),
                    include=("", "true"),
                    comment=("", ""),
                ),
                ExperienceSub(
                    content=("", "Development of critical features for the frontend and database management."),
                    include=("", "true"),
                    comment=("", ""),
                ),
                ExperienceSub(
                    content=("", "Significant optimization of application performance."),
                    include=("", "true"),
                    comment=("", ""),
                ),
            ],
        ),
        contentShort=("Content", "short content test"),
    ),
    "experienceB": Experience(
        postTitle=("", "Frontend Developer"),
        employer=("Company", "Large corporation"),
        startDate=("Start", date(2014, 1, 1)),
        endDate=("End", date(2022, 6, 1)),
        location=("Location", "Bristol, UK"),
        columnsDef=("", "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"),
        include=("", "true"),
        comment=("", ""),
        content=(
            "Content",
            [
                ExperienceSub(
                    content=("", "Worked on UX and UI features for three different projects."),
                    include=("", "true"),
                    comment=("", ""),
                ),
                ExperienceSub(
                    content=("", "Used Sass and Tailwind to build professional websites."),
                    include=("", "true"),
                    comment=("", ""),
                ),
                ExperienceSub(
                    content=(
                        "",
                        "Collaborated closely with an international team, alongside key stakeholders, within the Agile SCRUM framework.",
                    ),
                    include=("", "true"),
                    comment=("", ""),
                ),
            ],
        ),
        contentShort=("Content", "short content test"),
    ),
    "experienceC": Experience(
        postTitle=("", "Frontend Developer"),
        employer=("Internship", "Data intern"),
        startDate=("Start", date(2013, 1, 1)),
        endDate=("End", date(2013, 6, 1)),
        location=("Location", "Bristol, UK"),
        columnsDef=("", "|p{0.25cm} | X | p{2.5cm}| p{4cm}|"),
        include=("", "true"),
        comment=("", ""),
        content=("Content", """ Helped input data into database"""),
        contentShort=("Content", "short content test"),
    ),
}
