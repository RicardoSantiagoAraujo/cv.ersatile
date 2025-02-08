from datetime import date
from typing import Union

class Research:
    def __init__(self,
                 RES_title: dict[str, str],
                 RES_institute: dict[str, str],
                 RES_startDate:dict[str, date],
                 RES_endDate:dict[str, date],
                 RES_location: dict[str, str],
                 RES_content:dict[str, Union[str, list[str]]],
                 RES_include: dict[str, bool],
                 RES_columnsDef: dict[str, str]
                 ):
        self.RES_title = RES_title
        self.RES_institute = RES_institute
        self.RES_startDate = RES_startDate
        self.RES_endDate = RES_endDate
        self.RES_location = RES_location
        self.RES_content = RES_content
        self.RES_include = RES_include
        self.RES_columnsDef = RES_columnsDef