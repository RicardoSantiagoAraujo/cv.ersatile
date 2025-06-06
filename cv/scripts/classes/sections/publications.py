from datetime import date
from typing import Union


class Publication:
    """Publication entry in the CV. Each entry is a publication like a paper, a book, etc."""
    def __init__(
        self,
        key: tuple[str, str],
        fullText: tuple[str, str],
        include: tuple[str, bool],
        comment: tuple[str, str],
        hyperlink: tuple[str, str],
    ):
        self.PUB_key = key
        self.PUB_fullText = fullText
        # Generate atribute specifically for latex
        key_val = str(key[1])
        fullText_val = str(fullText[1])
        self.PUB_latexEntry = (
            "",
            ("\\fullcite{" + key_val + "}") if key_val != "" else fullText_val,
        )
        self.PUB_include = include
        self.PUB_comment = comment
        self.PUB_hyperlink = hyperlink
