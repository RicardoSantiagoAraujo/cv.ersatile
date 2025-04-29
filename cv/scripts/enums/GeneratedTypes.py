import enum


class GeneratedTypes(enum.Enum):
    """Type of generated files from the generator module: either individual sections that make up the CV or constants used by it.
    """
    sections = "sections"
    constants = "constants"
