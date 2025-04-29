from datetime import date
from typing import Union


 
class AwardsSub:
    """Each object of AwardSub is a single awards, within the categories defined by AwardGroup
    """
    def __init__(
        self,
        year: tuple[str, str],
        title: tuple[str, str],
        details: tuple[str, str],
        hyperlink: tuple[str, str],
        comment: tuple[str, str],
        include: tuple[str, str],
    ):
        self.AWARDITEM_year = year
        self.AWARDITEM_title = title
        # add ":" after title only if necessary
        self.AWARDITEM_details = (details[0],(f": {details[1]}." if details[1] != "" else ""))
        self.AWARDITEM_hyperlink = hyperlink
        self.AWARDITEM_comment = comment
        self.AWARDITEM_include = include


class AwardGroup:
    """Group of awards for a single category of awards, like university, sports, etc.
    """
    def __init__(
        self,
        groupTitle: tuple[str, str],
        content: tuple[str, list[AwardsSub]],
        comment: tuple[str, str],
        include: tuple[str, str],
    ):
        self.AWARD_groupTitle = groupTitle
        self.AWARD_content = content
        self.AWARD_comment = comment
        self.AWARD_include = include
