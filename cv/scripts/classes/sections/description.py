from datetime import date
from typing import Union


class Description:
    def __init__(
            self,
            content: tuple[str, str],
            comment: tuple[str, str]
        ):
        self.DESC_content = content
        self.DESC_comment = comment
