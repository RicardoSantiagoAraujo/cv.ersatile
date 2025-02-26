from datetime import date
from typing import Union


class PopScience:
    def __init__(
        self,
        title: tuple[str, str],
        initiative: tuple[str, str],
        startDate: tuple[str, date],
        endDate: tuple[str, date],
        location: tuple[str, str],
        content: tuple[str, Union[str, list[str]]],
        include: tuple[str, bool],
        comment: tuple[str, str],
        columnsDef: tuple[str, str],
    ):
        self.POPSCI_title = title
        self.POPSCI_initiative = initiative
        self.POPSCI_startDate = startDate
        self.POPSCI_endDate = endDate
        self.POPSCI_location = location
        self.POPSCI_content = content
        self.POPSCI_include = include
        self.POPSCI_comment = comment
        self.POPSCI_columnsDef = columnsDef
