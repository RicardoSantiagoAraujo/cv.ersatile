from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.Awards import AwardGroup, AwardsSub  # type: ignore
from datetime import date


generation_settings = GenerationSettings(
    templates={"html": "", "tex": ""},
    subtemplates={"html": "", "tex": ""},
)

contentDict_full_en = {
    "example1": AwardGroup(
        groupTitle=("", "Academic"),
        comment=("", "ACADEMIC"),
        include=("", "true"),
        content=(
            "",
            [
                AwardsSub(
                    year=("", "2015"),
                    title=("", "Student Merit Award"),
                    details=("", "University of Bristol"),
                    comment=("", ""),
                    include=("", "true"),
                ),
                AwardsSub(
                    year=("", "2018"),
                    title=("", "Hackathon competition"),
                    details=("", "Second place"),
                    comment=("", ""),
                    include=("", "true"),
                ),
            ],
        ),
    ),
    "example2": AwardGroup(
        groupTitle=("", "Sports"),
        comment=("", "SPORTS"),
        include=("", "true"),
        content=(
            "",
            [
                AwardsSub(
                    year=("", "2011"),
                    title=("", "National table tenis junior champion"),
                    details=("", ""),
                    comment=("", ""),
                    include=("", "true"),
                ),
            ],
        ),
    ),
}
