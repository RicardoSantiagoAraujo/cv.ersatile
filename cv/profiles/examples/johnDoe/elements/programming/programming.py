from classes.settings.generationSettings import GenerationSettings # type: ignore
from classes.sections.programming import ProgrammingGroup, ProgrammingSub # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={
        "html":"",
        "tex":""
        },
    subtemplates={
        "html":"",
        "tex":""
        },
)

contentDict_full_en = {
    "example1": ProgrammingGroup(
        groupName=("","Programming and Scripting"),
        nrow=("",5),
        include=("","true"),
        comment=("", "COMMENT GOES HERE"),
        contents=("",
                  [
                      ProgrammingSub(
                      name=("", "Python"),
                      iconLatex=("", "\\faPython"),
                      score=("", 5),
                      details=("", "pandas, Matplotlib, Flask"),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                      ProgrammingSub(
                      name=("", "R"),
                      iconLatex=("", "\\faRProject"),
                      score=("", 5),
                      details=("", "DataViz, Tidyverse"),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                      ProgrammingSub(
                      name=("", "Type/Javascript"),
                      iconLatex=("", "\\faJs"),
                      score=("", 5),
                      details=("", "Angular 2/JS, D3.js, jQuery"),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                      ProgrammingSub(
                      name=("", "C\\#"),
                      iconLatex=("", "\\faFileCode"),
                      score=("", 4),
                      details=("", ".NET Framework"),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                      ProgrammingSub(
                      name=("", "Java"),
                      iconLatex=("", "\\faJava"),
                      score=("", 3),
                      details=("", "Spring"),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    )
                  ]
                  ),
        ),
    "example2": ProgrammingGroup(
        groupName=("","Markup"),
        nrow=("",3),
        include=("","true"),
        comment=("", "COMMENT GOES HERE"),
        contents=("",
                  [
                      ProgrammingSub(
                      name=("", "HTML/CSS"),
                      iconLatex=("", "\\faHtml5"),
                      score=("", 5),
                      details=("", "Sass, Tailwind, Bootstrap"),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                    ProgrammingSub(
                      name=("", "\\LaTeX"),
                      iconLatex=("","\\faFilePdf"),
                      score=("", 5),
                      details=("", ""),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                    ProgrammingSub(
                      name=("", "R Markdown"),
                      iconLatex=("","\\faFileDownload"),
                      score=("", 5),
                      details=("", ""),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                  ]
                  ),
        ),
    "example3": ProgrammingGroup(
        groupName=("","Databases"),
        nrow=("",1),
        include=("","true"),
        comment=("", "COMMENT GOES HERE"),
        contents=("",
                  [
                      ProgrammingSub(
                      name=("", "Relational"),
                      iconLatex=("", "\\faDatabase"),
                      score=("", 4),
                      details=("", "SQL Server, MySQL, SQLite"),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                  ]
                  ),
        ),
    "example4": ProgrammingGroup(
        groupName=("","Version control"),
        nrow=("",1),
        include=("","true"),
        comment=("", "COMMENT GOES HERE"),
        contents=("",
                  [
                      ProgrammingSub(
                      name=("", "git"),
                      iconLatex=("", "\\faGit"),
                      score=("", 5),
                      details=("", "Gitflow, GitHub, Gitlab"),
                      include=("", "true"),
                      comment=("", "COMMENT GOES HERE"),
                    ),
                  ]
                  ),
        ),
}
