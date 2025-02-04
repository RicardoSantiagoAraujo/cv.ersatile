from datetime import date

class Experience:
    def __init__(self,
                 EXP_postTitle: dict[str, str] = {"POSTTITLE KEY: ": "POSTTITLE VALUE"},
                 EXP_employer: dict[str, str] = {"EMPLOYER KEY: ": "EMPLOYER VALUE"},
                 EXP_startDate:dict[str, date] = {"STARTDATE KEY: ":date(1,1,1)},
                 EXP_endDate:dict[str, date] = {"ENDDATE KEY: ":date.today()},
                 EXP_location: dict[str, str] = {"LOCATION KEY: ": "LOCATION VALUE"},
                 EXP_content:dict[str, date] = {"CONTENT KEY: ":"CONTENT"}
                 ):
        self.EXP_postTitle = EXP_postTitle
        self.EXP_employer = EXP_employer
        self.EXP_startDate = EXP_startDate
        self.EXP_endDate = EXP_endDate
        self.EXP_location = EXP_location
        self.EXP_content = EXP_content
