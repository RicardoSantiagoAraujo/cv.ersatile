from datetime import date
from typing import Union

class Description:
    def __init__(self,
                 content: tuple[str, str]
                 ):
        self.DESC_content = content