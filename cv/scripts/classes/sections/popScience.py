from datetime import date
from typing import Union

class PopScience:
    def __init__(self,
                 title: dict[str, str],
                 initiative: dict[str, str],
                 startDate:dict[str, date],
                 endDate:dict[str, date],
                 location: dict[str, str],
                 content:dict[str, Union[str, list[str]]],
                 include: dict[str, bool],
                 columnsDef: dict[str, str]
                 ):
        self.POPSCI_title = title
        self.POPSCI_initiative = initiative
        self.POPSCI_startDate = startDate
        self.POPSCI_endDate = endDate
        self.POPSCI_location = location
        self.POPSCI_content = content
        self.POPSCI_include = include
        self.POPSCI_columnsDef = columnsDef