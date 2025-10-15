from datetime import date
from typing import Union

 
# Each object of WorkSub is a single awards, within the categories defined by WorkGroup
class WorkSub:
    """Within each category of work (group), each object of WorkSub is a single work.
    """
    def __init__(
        self,
        year: tuple[str, str],
        title: tuple[str, str],
        subtitle: tuple[str, str],
        details: tuple[str, str],
        detailsShort: tuple[str, str],
        authors: tuple[str, str],
        repository: tuple[str, str],
        externalLink: tuple[str, str],
        comment: tuple[str, str],
        include: tuple[str, str],
    ):
        self.WORKITEM_year = year
        self.WORKITEM_title = title
        self.WORKITEM_subtitle = subtitle
        self.WORKITEM_authors = authors
        self.WORKITEM_details = details
        self.WORKITEM_detailsShort = detailsShort
        self.WORKITEM_repository = repository
        self.WORKITEM_externalLink = externalLink
        self.WORKITEM_comment = comment
        self.WORKITEM_include = include


class WorkGroup:
    """Works are projects that you wish to highlight, and are grouped in categories like IT, exhibitions, etc.
    """
    def __init__(
        self,
        groupTitle: tuple[str, str],
        description: tuple[str, str],
        content: tuple[str, list[WorkSub]],
        comment: tuple[str, str],
        include: tuple[str, str],
    ):
        self.WORK_groupTitle = groupTitle
        self.WORK_description = description
        self.WORK_content = content
        self.WORK_comment = comment
        self.WORK_include = include
