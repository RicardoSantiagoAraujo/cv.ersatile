from datetime import date
from typing import Union


class Other:
    def __init__(
        self,
        category: tuple[str, str],
        content: tuple[str, str],
        include: tuple[str, bool],
        comment: tuple[str, str],
    ):
        self.OTHER_category = category
        self.OTHER_content = content
        self.OTHER_include = include
        self.OTHER_comment = comment
