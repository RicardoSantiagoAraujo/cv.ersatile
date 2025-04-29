from scripts.classes.settings.generationSettings import GenerationSettings  # type: ignore
from scripts.classes.sections.other import Other  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"html": "", "tex": ""},
    subtemplates={"html": "", "tex": ""},
)

contentDict_full_en = {
    "example1": Other(
        category=("", "Languages"),
        content=("", "English (Native), Spanish (C1)"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
    ),
    "example2": Other(
        category=("", "Other Digital Tools"),
        content=("", "Adobe Photoshop \\& Adobe Illustrator and Photoshop, MS Office suite"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
    ),
    "example3": Other(
        category=("", "Miscellaneous experience"),
        content=("", "Waiter at italian restaurant"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
    ),
    "example4": Other(
        category=("", "Volunteer work"),
        content=("", "Active volunteer at food bank"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
    ),
    "example5": Other(
        category=("", "Hobbies and interests"),
        content=("", "Table tenis, cycling, guitar, tabletop games"),
        include=("", "true"),
        comment=("", "COMMENT GOES HERE"),
    ),
}
