from datetime import date
from typing import Union

class Teaching:
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
        self.TEACH_title = title
        self.TEACH_institute = institute
        self.TEACH_startDate = startDate
        self.TEACH_endDate = endDate
        self.TEACH_location = location
        self.TEACH_content = content
        self.TEACH_include = include
        self.TEACH_columnsDef = columnsDef