from datetime import date
from typing import Union

class AwardItem:
    def __init__(self,
                 year: tuple[str, str],
                 title: tuple[str, str],
                 details:tuple[str, str],
                 comment:tuple[str, str],
                 include:tuple[str, str],
                 ):
        self.AWARDITEM_year = year
        self.AWARDITEM_title = title
        self.AWARDITEM_details = details
        self.AWARDITEM_comment = comment
        self.AWARDITEM_include = include


class AwardGroup:
    def __init__(self,
                 groupTitle: tuple[str, str],
                 content: tuple[str, list[AwardItem]],
                 comment:tuple[str, str],
                 include:tuple[str, str],
                 ):
        self.AWARD_groupTitle = groupTitle
        self.AWARD_content = content
        self.AWARD_comment = comment
        self.AWARD_include = include