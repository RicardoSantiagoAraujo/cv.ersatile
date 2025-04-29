import enum


class OutputType(enum.Enum):
    """File types that the generator can output."""
    html = "html"
    tex = "tex"
    ts = "ts"
    scss = "scss"
