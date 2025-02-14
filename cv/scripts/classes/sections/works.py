from datetime import date
from typing import Union

class WorkItem:
    def __init__(self,
                 year: tuple[str, str],
                 title: tuple[str, str],
                 details:tuple[str, str],
                 comment:tuple[str, str],
                 include:tuple[str, str],
                 ):
        self.WORKITEM_year = year
        self.WORKITEM_title = title
        self.WORKITEM_details = details
        self.WORKITEM_comment = comment
        self.WORKITEM_include = include


class WorkGroup:
    def __init__(self,
                 groupTitle: tuple[str, str],
                 content: tuple[str, list[WorkItem]],
                 comment:tuple[str, str],
                 include:tuple[str, str],
                 ):
        self.WORK_groupTitle = groupTitle
        self.WORK_content = content
        self.WORK_comment = comment
        self.WORK_include = include