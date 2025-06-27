import enum


class SectionType(enum.Enum):
    """Names of sections that the CV supports."""

    description = "description"
    education = "education"
    experience = "experience"
    popScience = "popScience"
    teaching = "teaching"
    research = "research"
    informatics = "informatics"
    other = "other"
    certificates = "certificates"
    works = "works"
    awards = "awards"
    publications = "publications"
