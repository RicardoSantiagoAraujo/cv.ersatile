from datetime import date

class Experience:
    def __init__(self,
                 postTitle: dict[str, str] = {"POSTTITLE KEY: ": "POSTTITLE VALUE"},
                 employer: dict[str, str] = {"EMPLOYER KEY: ": "EMPLOYER VALUE"},
                 startDate:date = date(1,1,1),
                 endDate:date = date.today(),
                 location: dict[str, str] = {"LOCATION KEY: ": "LOCATION VALUE"},
                 content: str = "CONTENT"
                 ):
        self.postTitle = postTitle
        self.employer = employer
        self.startDate = startDate
        self.endDate = endDate
        self.location = location
        self.content = content
