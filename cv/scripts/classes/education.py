from datetime import date
from typing import Union

class Education:
    def __init__(self,
                 EDU_level: dict[str, str],
                 EDU_institution: dict[str, str],
                 EDU_startDate:dict[str, date],
                 EDU_endDate:dict[str, date],
                 EDU_location: dict[str, str],
                 EDU_content:dict[str, Union[str, list[str]]],
                 EDU_include: dict[str, bool],
                 EDU_columnsDef: dict[str, str]
                 ):
        self.EDU_level = EDU_level
        self.EDU_institution = EDU_institution
        self.EDU_startDate = EDU_startDate
        self.EDU_endDate = EDU_endDate
        self.EDU_location = EDU_location
        self.EDU_content = EDU_content
        self.EDU_include = EDU_include
        self.EDU_columnsDef = EDU_columnsDef