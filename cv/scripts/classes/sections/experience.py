from datetime import date
from typing import Union

class Experience:
    def __init__(self,
                 postTitle: dict[str, str],
                 employer: dict[str, str],
                 startDate:dict[str, date],
                 endDate:dict[str, date],
                 location: dict[str, str],
                 content:dict[str, Union[str, list[str]]],
                 include: dict[str, bool],
                 columnsDef: dict[str, str]
                 ):
        self.EXP_postTitle = postTitle
        self.EXP_employer = employer
        self.EXP_startDate = startDate
        self.EXP_endDate = endDate
        self.EXP_location = location
        self.EXP_content = content
        self.EXP_include = include
        self.EXP_columnsDef = columnsDef