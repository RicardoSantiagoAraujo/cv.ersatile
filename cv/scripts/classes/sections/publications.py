from datetime import date
from typing import Union


class Publication:
    def __init__(
        self,
        key: tuple[str, str],
        fullText: tuple[str, str],
        include: tuple[str, bool],
        hyperlink: tuple[str, bool],
    ):
        self.PUB_key = key
        self.PUB_fullText = fullText
        # Generate atribute specifically for latex
        key_val = str(key[0])
        fullText_val = str(fullText[1])
        self.PUB_latexEntry = (
            "",
            ("\\fullcite{" + key_val + "}") if key_val != "" else fullText_val,
        )
        self.PUB_include = include
        self.PUB_hyperlink = hyperlink
