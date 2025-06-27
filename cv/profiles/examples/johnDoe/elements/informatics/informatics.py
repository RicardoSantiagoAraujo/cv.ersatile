from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.Informatics import InformaticsGroup, InformaticsSub  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"html": "", "tex": ""},
    subtemplates={"html": "", "tex": ""},
)

contentDict_full_en = {
    "example1": InformaticsGroup(
        groupName=("", "Informatics and Scripting"),
        nrow=("", 5),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        contents=(
            "",
            [
                InformaticsSub(
                    name=("", "Python"),
                    iconLatex=("", "\\faPython"),
                    score=("", 5),
                    details=("", "pandas, Matplotlib, Flask"),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
                InformaticsSub(
                    name=("", "R"),
                    iconLatex=("", "\\faRProject"),
                    score=("", 5),
                    details=("", "DataViz, Tidyverse"),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
                InformaticsSub(
                    name=("", "Type/Javascript"),
                    iconLatex=("", "\\faJs"),
                    score=("", 5),
                    details=("", "Angular 2/JS, D3.js, jQuery"),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
                InformaticsSub(
                    name=("", "C\\#"),
                    iconLatex=("", "\\faFileCode"),
                    score=("", 4),
                    details=("", ".NET Framework"),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
                InformaticsSub(
                    name=("", "Java"),
                    iconLatex=("", "\\faJava"),
                    score=("", 3),
                    details=("", "Spring"),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
            ],
        ),
    ),
    "example2": InformaticsGroup(
        groupName=("", "Markup"),
        nrow=("", 3),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        contents=(
            "",
            [
                InformaticsSub(
                    name=("", "HTML/CSS"),
                    iconLatex=("", "\\faHtml5"),
                    score=("", 5),
                    details=("", "Sass, Tailwind, Bootstrap"),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
                InformaticsSub(
                    name=("", "\\LaTeX"),
                    iconLatex=("", "\\faFilePdf"),
                    score=("", 5),
                    details=("", ""),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
                InformaticsSub(
                    name=("", "R Markdown"),
                    iconLatex=("", "\\faFileDownload"),
                    score=("", 5),
                    details=("", ""),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
            ],
        ),
    ),
    "example3": InformaticsGroup(
        groupName=("", "Databases"),
        nrow=("", 1),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        contents=(
            "",
            [
                InformaticsSub(
                    name=("", "Relational"),
                    iconLatex=("", "\\faDatabase"),
                    score=("", 4),
                    details=("", "SQL Server, MySQL, SQLite"),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
            ],
        ),
    ),
    "example4": InformaticsGroup(
        groupName=("", "Version control"),
        nrow=("", 1),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
        contents=(
            "",
            [
                InformaticsSub(
                    name=("", "git"),
                    iconLatex=("", "\\faGit"),
                    score=("", 5),
                    details=("", "Gitflow, GitHub, Gitlab"),
                    include=("", "true"),
                    comment=("", "COMMENT GOES HERE"),
                ),
            ],
        ),
    ),
}
