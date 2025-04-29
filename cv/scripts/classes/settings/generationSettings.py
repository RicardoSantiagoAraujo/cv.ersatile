from datetime import date
from typing import Union


class GenerationSettings:
    """Helper class to generate the CV. It  specifies the templates and subtemplates you wish to use in generating a CV section.
    """
    def __init__(
        self,
        templates: dict[str, str],
        subtemplates: dict[str, str],
    ):
        self.templates = templates
        self.subtemplates = subtemplates
