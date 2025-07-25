from datetime import date
from typing import Union


# Support class of individual entries in informatics
class InformaticsSub:
    """Subdivide a informatics group into individual entries, like Python, R, etc."""

    def __init__(
        self,
        name: tuple[str, str],
        iconLatex: tuple[str, str],
        score: tuple[str, str],
        details: tuple[str, str],
        include: tuple[str, bool],
        comment: tuple[str, str],
    ):
        self.PROGENTRY_name = name
        self.PROGENTRY_iconLatex = iconLatex
        self.PROGENTRY_score = score
        self.PROGENTRY_details = details
        self.PROGENTRY_include = include
        self.PROGENTRY_comment = comment


# Class of informatics groups holding entries
class InformaticsGroup:
    """Category of informatics languages, tools or skills, like data science, web development, etc."""

    def __init__(
        self,
        groupName: tuple[str, str],
        nrow: tuple[str, int],
        contents: tuple[str, list[InformaticsSub]],
        include: tuple[str, bool],
        comment: tuple[str, str],
    ):
        self.PROG_groupName = groupName
        self.PROG_nrow = nrow
        self.PROG_contents = contents
        self.PROG_include = include
        self.PROG_comment = comment
