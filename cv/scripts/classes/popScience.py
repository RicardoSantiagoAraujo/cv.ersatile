from datetime import date
from typing import Union

class PopScience:
    def __init__(self,
                 POPSCI_title: dict[str, str],
                 POPSCI_initiative: dict[str, str],
                 POPSCI_startDate:dict[str, date],
                 POPSCI_endDate:dict[str, date],
                 POPSCI_location: dict[str, str],
                 POPSCI_content:dict[str, Union[str, list[str]]],
                 POPSCI_include: dict[str, bool],
                 POPSCI_columnsDef: dict[str, str]
                 ):
        self.POPSCI_title = POPSCI_title
        self.POPSCI_initiative = POPSCI_initiative
        self.POPSCI_startDate = POPSCI_startDate
        self.POPSCI_endDate = POPSCI_endDate
        self.POPSCI_location = POPSCI_location
        self.POPSCI_content = POPSCI_content
        self.POPSCI_include = POPSCI_include
        self.POPSCI_columnsDef = POPSCI_columnsDef