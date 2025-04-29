from datetime import date
from typing import Union


class Other:
    """Mischelaneous items.  Each one is a category with a list of items, like a languages categories with a list of languages, or a hobbies category with a corresponding list of hobbies (dancing, reading, etc). 
    """
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
