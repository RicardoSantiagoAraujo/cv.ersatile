from datetime import date
from typing import Union


# Each object of AwardSub is a single awards, within the categories defined by AwardGroup
class GenerationSettings:
    def __init__(
        self,
        templates: dict[str,str]={
            "html":"2x2",
            "tex":"2x2",
            "ts":"",
            "scss":"",
            },
        subtemplates: dict[str,str]={
            "html":"2x2",
            "tex":"2x2",
            "ts":"",
            "scss":"",
            },
    ):
        self.templates=templates
        self.subtemplates=subtemplates