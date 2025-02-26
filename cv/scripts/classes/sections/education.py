from datetime import date
from typing import Union


class Education:
    def __init__(
        self,
        level: tuple[str, str],
        institution: tuple[str, str],
        startDate: tuple[str, date],
        endDate: tuple[str, date],
        location: tuple[str, str],
        content: tuple[str, Union[str, list[str]]],
        include: tuple[str, bool],
        comment: tuple[str, str],
        columnsDef: tuple[str, str],
    ):
        self.EDU_level = level
        self.EDU_institution = institution
        self.EDU_startDate = startDate
        self.EDU_endDate = endDate
        self.EDU_location = location
        self.EDU_content = content
        self.EDU_include = include
        self.EDU_comment = comment
        self.EDU_columnsDef = columnsDef
