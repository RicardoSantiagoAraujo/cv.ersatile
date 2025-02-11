from datetime import date
from typing import Union

class Experience:
    def __init__(self,
                 EXP_postTitle: dict[str, str],
                 EXP_employer: dict[str, str],
                 EXP_startDate:dict[str, date],
                 EXP_endDate:dict[str, date],
                 EXP_location: dict[str, str],
                 EXP_content:dict[str, Union[str, list[str]]],
                 EXP_include: dict[str, bool],
                 EXP_columnsDef: dict[str, str]
                 ):
        self.EXP_postTitle = EXP_postTitle
        self.EXP_employer = EXP_employer
        self.EXP_startDate = EXP_startDate
        self.EXP_endDate = EXP_endDate
        self.EXP_location = EXP_location
        self.EXP_content = EXP_content
        self.EXP_include = EXP_include
        self.EXP_columnsDef = EXP_columnsDef