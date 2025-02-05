from datetime import date
from typing import Union

class Education:
    def __init__(self,
                 EDU_level: dict[str, str] = {"LEVEL KEY: ": "LEVEL VALUE"},
                 EDU_institution: dict[str, str] = {"EMPLOYER KEY: ": "EMPLOYER VALUE"},
                 EDU_startDate:dict[str, date] = {"STARTDATE KEY: ":date(1,1,1)},
                 EDU_endDate:dict[str, date] = {"ENDDATE KEY: ":date.today()},
                 EDU_location: dict[str, str] = {"LOCATION KEY: ": "LOCATION VALUE"},
                 EDU_content:dict[str, Union[str, list[str]]] = {"CONTENT KEY: ":"CONTENT"},
                 EDU_include: dict[str, bool] = {"INCLUDE ENTRY" : "true"},
                 EDU_columnsDef: dict[str, str] = {"": ""}
                 ):
        self.EDU_level = EDU_level
        self.EDU_institution = EDU_institution
        self.EDU_startDate = EDU_startDate
        self.EDU_endDate = EDU_endDate
        self.EDU_location = EDU_location
        self.EDU_content = EDU_content
        self.EDU_include = EDU_include
        self.EDU_columnsDef = EDU_columnsDef