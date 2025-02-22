from datetime import date
from typing import Union


# Each object of AwardSub is a single awards, within the categories defined by AwardGroup
class GenerationSettings:
    def __init__(
        self,
        templates: dict[str,str],
        subtemplates: dict[str,str],
    ):
        self.templates=templates
        self.subtemplates=subtemplates