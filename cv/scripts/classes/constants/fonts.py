class Fonts:
    """Class to define fonts used in the CV generation.
    This class contains things like the main fonts and backup fonts.
    """
    def __init__(
        self,
        # Fonts
        mainFont: tuple[str, str],
        titleFont: tuple[str, str],
        subtitleFont: tuple[str, int],
        # Backups if fonts are not available
        mainFontBackup: tuple[str, str],
        titleFontBackup: tuple[str, str],
        subtitleFontBackup: tuple[str, int],
        # Meta
        comment: tuple[str, int],
    ):
        self.CONST_mainFont = mainFont
        self.CONST_titleFont = titleFont
        self.CONST_subtitleFont = subtitleFont

        self.CONST_mainFontBackup = mainFontBackup
        self.CONST_titleFontBackup = titleFontBackup
        self.CONST_subtitleFontBackup = subtitleFontBackup

        self.CONST_comment = comment
