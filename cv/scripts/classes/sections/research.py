from datetime import date
from typing import Union


class Research:
    def __init__(
        self,
        title: tuple[str, str],
        institute: tuple[str, str],
        startDate: tuple[str, date],
        endDate: tuple[str, date],
        location: tuple[str, str],
        content: tuple[str, Union[str, list[str]]],
        include: tuple[str, bool],
        comment: tuple[str, str],
        columnsDef: tuple[str, str],
    ):
        self.RES_title = title
        self.RES_institute = institute
        self.RES_startDate = startDate
        self.RES_endDate = endDate
        self.RES_location = location
        self.RES_content = content
        self.RES_include = include
        self.RES_comment = comment
        self.RES_columnsDef = columnsDef
