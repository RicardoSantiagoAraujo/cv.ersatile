from classes.sections.works import WorkGroup, WorkItem # type: ignore
from datetime import date


contentDict_full_en = {
    "example1": WorkGroup(
        groupTitle=("","Web development"),
        comment=("","COMMENT"),
         include=("","true"),
        content=("",
                  [
                      WorkItem(
                      year=("", ""),
                      title=("", "Weather app:"),
                      details=("", "\href{https://weather.com}{weather.com}"),
                      comment=("", "COMMENT"),
                      include=("", "true"),
                    ),
                      WorkItem(
                      year=("", ""),
                      title=("", "e-commerce website"),
                      details=("", "\href{https://commerce.com}{buyandsell.com}"),
                      comment=("", "COMMENT"),
                      include=("", "true"),
                    ),
                  ]
                  ),
        ),
}
