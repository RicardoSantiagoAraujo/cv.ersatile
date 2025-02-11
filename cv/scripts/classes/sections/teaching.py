from datetime import date
from typing import Union

class Teaching:
    def __init__(self,
                 TEACH_title: dict[str, str],
                 TEACH_institute: dict[str, str],
                 TEACH_startDate:dict[str, date],
                 TEACH_endDate:dict[str, date],
                 TEACH_location: dict[str, str],
                 TEACH_content:dict[str, Union[str, list[str]]],
                 TEACH_include: dict[str, bool],
                 TEACH_columnsDef: dict[str, str]
                 ):
        self.TEACH_title = TEACH_title
        self.TEACH_institute = TEACH_institute
        self.TEACH_startDate = TEACH_startDate
        self.TEACH_endDate = TEACH_endDate
        self.TEACH_location = TEACH_location
        self.TEACH_content = TEACH_content
        self.TEACH_include = TEACH_include
        self.TEACH_columnsDef = TEACH_columnsDef