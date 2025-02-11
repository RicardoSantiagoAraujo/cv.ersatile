from datetime import date
from typing import Union

class Publication:
    def __init__(self,
                 key: dict[str, str],
                 fullText: dict[str, str],
                 include: dict[str, bool],
                 ):
        self.PUB_key = key
        self.PUB_fullText = fullText
        # Generate atribute specifically for latex
        key_val = str(list(key.values())[0])
        fullText_val = str(list(fullText.values())[0])
        self.PUB_latexEntry = {
            "":("\\fullcite{" + key_val + "}")
            if key_val != "" else fullText_val
        }
        self.PUB_include = include
