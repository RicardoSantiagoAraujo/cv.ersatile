from datetime import date
from typing import Union

class Education:
    def __init__(self,
                 level: dict[str, str],
                 institution: dict[str, str],
                 startDate:dict[str, date],
                 endDate:dict[str, date],
                 location: dict[str, str],
                 content:dict[str, Union[str, list[str]]],
                 include: dict[str, bool],
                 columnsDef: dict[str, str]
                 ):
        self.EDU_level = level
        self.EDU_institution = institution
        self.EDU_startDate = startDate
        self.EDU_endDate = endDate
        self.EDU_location = location
        self.EDU_content = content
        self.EDU_include = include
        self.EDU_columnsDef = columnsDef