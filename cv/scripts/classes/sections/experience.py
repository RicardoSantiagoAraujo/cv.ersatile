from datetime import date
from typing import Union


# Each ExperienceSub represents one item in a list in Experience.content
class ExperienceSub:
    def __init__(self, content: tuple[str, str]):
        self.EXPLINE_content = content


class Experience:
    def __init__(
        self,
        postTitle: tuple[str, str],
        employer: tuple[str, str],
        startDate: tuple[str, date],
        endDate: tuple[str, date],
        location: tuple[str, str],
        content: tuple[str, Union[str, list[ExperienceSub]]],
        include: tuple[str, bool],
        columnsDef: tuple[str, str],
    ):
        self.EXP_postTitle = postTitle
        self.EXP_employer = employer
        self.EXP_startDate = startDate
        self.EXP_endDate = endDate
        self.EXP_location = location
        self.EXP_content = content
        self.EXP_include = include
        self.EXP_columnsDef = columnsDef
