from datetime import date
from typing import Union


class Teaching:
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
        self.TEACH_title = title
        self.TEACH_institute = institute
        self.TEACH_startDate = startDate
        self.TEACH_endDate = endDate
        self.TEACH_location = location
        self.TEACH_content = content
        self.TEACH_include = include
        self.TEACH_comment = comment
        self.TEACH_columnsDef = columnsDef
