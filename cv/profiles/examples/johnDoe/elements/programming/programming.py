from classes.sections.programming import ProgrammingGroup, ProgrammingItem # type: ignore
from datetime import date

contentDict_full_en = {
    "example1": ProgrammingGroup(
        groupName=("","Programming and Scripting"),
        nrow=("",5),
        include=("","true"),
        contents=("",
                  [
                      ProgrammingItem(
                      name=("", "Python"),
                      iconLatex=("", "\\faPython"),
                      score=("", 5),
                      details=("", "pandas, Matplotlib, Flask"),
                      include=("", "true"),
                    ),
                      ProgrammingItem(
                      name=("", "R"),
                      iconLatex=("", "\\faRProject"),
                      score=("", 5),
                      details=("", "DataViz, Tidyverse"),
                      include=("", "true"),
                    ),
                      ProgrammingItem(
                      name=("", "Type/Javascript"),
                      iconLatex=("", "\\faJs"),
                      score=("", 5),
                      details=("", "Angular 2/JS, D3.js, jQuery"),
                      include=("", "true"),
                    ),
                      ProgrammingItem(
                      name=("", "C\#"),
                      iconLatex=("", "\\faFileCode"),
                      score=("", 4),
                      details=("", ".NET Framework"),
                      include=("", "true"),
                    ),
                      ProgrammingItem(
                      name=("", "Java"),
                      iconLatex=("", "\\faJava"),
                      score=("", 3),
                      details=("", "Spring"),
                      include=("", "true"),
                    )
                  ]
                  ),
        ),
    "example2": ProgrammingGroup(
        groupName=("","Markup"),
        nrow=("",3),
        include=("","true"),
        contents=("",
                  [
                      ProgrammingItem(
                      name=("", "HTML/CSS"),
                      iconLatex=("", "\\faHtml5"),
                      score=("", 5),
                      details=("", "Sass, Tailwind, Bootstrap"),
                      include=("", "true"),
                    ),
                    ProgrammingItem(
                      name=("", "\LaTeX"),
                      iconLatex=("","\\faFilePdf"),
                      score=("", 5),
                      details=("", ""),
                      include=("", "true"),
                    ),
                    ProgrammingItem(
                      name=("", "R Markdown"),
                      iconLatex=("","\\faFileDownload"),
                      score=("", 5),
                      details=("", ""),
                      include=("", "true"),
                    ),
                  ]
                  ),
        ),
    "example3": ProgrammingGroup(
        groupName=("","Databases"),
        nrow=("",1),
        include=("","true"),
        contents=("",
                  [
                      ProgrammingItem(
                      name=("", "Relational"),
                      iconLatex=("", "\\faDatabase"),
                      score=("", 4),
                      details=("", "SQL Server, MySQL, SQLite"),
                      include=("", "true"),
                    ),
                  ]
                  ),
        ),
    "example4": ProgrammingGroup(
        groupName=("","Version control"),
        nrow=("",1),
        include=("","true"),
        contents=("",
                  [
                      ProgrammingItem(
                      name=("", "git"),
                      iconLatex=("", "\\faGit"),
                      score=("", 5),
                      details=("", "Gitflow, GitHub, Gitlab"),
                      include=("", "true"),
                    ),
                  ]
                  ),
        ),
}
