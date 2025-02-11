from datetime import date
from typing import Union

class Research:
    def __init__(self,
                 title: dict[str, str],
                 institute: dict[str, str],
                 startDate:dict[str, date],
                 endDate:dict[str, date],
                 location: dict[str, str],
                 content:dict[str, Union[str, list[str]]],
                 include: dict[str, bool],
                 columnsDef: dict[str, str]
                 ):
        self.RES_title = title
        self.RES_institute = institute
        self.RES_startDate = startDate
        self.RES_endDate = endDate
        self.RES_location = location
        self.RES_content = content
        self.RES_include = include
        self.RES_columnsDef = columnsDef