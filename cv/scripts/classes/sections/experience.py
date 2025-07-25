from datetime import date
from typing import Union


class ExperienceSub:
    """Class to specify individual characteristics or achievements within a professional experience."""

    def __init__(
        self,
        content: tuple[str, str],
        include: tuple[str, bool],
        comment: tuple[str, str],
    ):
        self.EXPLINE_content = content
        self.EXPLINE_include = include
        self.EXPLINE_comment = comment


class Experience:
    """Individual experience item, like a job or an internship.
    This class is used to create a list of experiences, each with its own title, employer, dates, location, and content.
    """

    def __init__(
        self,
        postTitle: tuple[str, str],
        employer: tuple[str, str],
        startDate: tuple[str, date],
        endDate: tuple[str, date],
        location: tuple[str, str],
        content: tuple[str, Union[str, list[ExperienceSub]]],
        contentShort: tuple[str, Union[str, list[ExperienceSub]]],
        include: tuple[str, bool],
        columnsDef: tuple[str, str],
        comment: tuple[str, str],
    ):
        self.EXP_postTitle = postTitle
        self.EXP_employer = employer
        self.EXP_startDate = startDate
        self.EXP_endDate = endDate
        self.EXP_location = location
        self.EXP_content = content
        self.EXP_contentShort = contentShort
        # Elements to wrap around content if it is a list in tex
        self.EXP_contentPre_tex = (
            "",
            "\\begin{customlist}[topsep=0pt]%" if type(content[1]) == list else "",
        )
        self.EXP_contentPos_tex = (
            "",
            "\\end{customlist}%" if type(content[1]) == list else "",
        )
        self.EXP_contentShortPre_tex = (
            "",
            "\\begin{customlist}[topsep=0pt]%" if type(contentShort[1]) == list else "",
        )
        self.EXP_contentShortPos_tex = (
            "",
            "\\end{customlist}%" if type(contentShort[1]) == list else "",
        )
        self.EXP_include = include
        self.EXP_columnsDef = columnsDef
        self.EXP_comment = comment
