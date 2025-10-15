from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.Works import WorkGroup, WorkSub  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"html": "", "tex": ""},
    subtemplates={"html": "", "tex": ""},
)

contentDict_full_en = {
    "example1": WorkGroup(
        groupTitle=("", "Web development"),
        description=("", "Software development projects for the web"),
        comment=("", "COMMENT"),
        include=("", "true"),
        content=(
            "",
            [
                WorkSub(
                    year=("", ""),
                    title=("", "Weather app"),
                    subtitle=("", "subtitle"),
                    authors=("", "Author list"),
                    content=("", "App to check weather"),
                    contentShort=("", "App to check weather"),
                    externalLink=("", "\\href{https://weather.com}{weather.com}"),
                    repository=("", "\\href{https://github.com}{Github}"),
                    comment=("", "COMMENT"),
                    include=("", "true"),
                ),
                WorkSub(
                    year=("", ""),
                    title=("", "e-commerce website"),
                    subtitle=("", "subtitle"),
                    authors=("", "Author list"),
                    content=("", "App to sell stuff"),
                    contentShort=("", "App to sell stuff"),
                    externalLink=("", "\\href{https://commerce.com}{buyandsell.com}"),
                    repository=("", "\\href{https://github.com}{Github}"),
                    comment=("", "COMMENT"),
                    include=("", "true"),
                ),
            ],
        ),
    ),
}
