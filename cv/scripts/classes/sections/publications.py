from datetime import date
from typing import Union

class Publication:
    def __init__(self,
                 PUB_key: dict[str, str],
                 PUB_fullText: dict[str, str],
                 PUB_include: dict[str, bool],
                 ):
        self.PUB_key = PUB_key
        self.PUB_fullText = PUB_fullText
        # Generate atribute specifically for latex
        key = str(list(PUB_key.values())[0])
        fullText = str(list(PUB_fullText.values())[0])
        self.PUB_latexEntry = {
            "":("\\fullcite{" + key + "}")
            if key != "" else fullText
        }
        self.PUB_include = PUB_include
