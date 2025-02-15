from classes.sections.works import WorkGroup, WorkSub # type: ignore
from datetime import date


contentDict_full_en = {
    "example1": WorkGroup(
        groupTitle=("","Web development"),
        comment=("","COMMENT"),
         include=("","true"),
        content=("",
                  [
                      WorkSub(
                      year=("", ""),
                      title=("", "Weather app:"),
                      details=("", "\href{https://weather.com}{weather.com}"),
                      comment=("", "COMMENT"),
                      include=("", "true"),
                    ),
                      WorkSub(
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
