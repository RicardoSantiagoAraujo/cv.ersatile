from datetime import date
from typing import Union


class CertificateSub:
    """Each object of CertificateSub is a single awards, within the categories defined by CertificateGroup
    """
    def __init__(
        self,
        year: tuple[str, str],
        title: tuple[str, str],
        details: tuple[str, str],
        comment: tuple[str, str],
        include: tuple[str, str],
    ):
        self.CERTITEM_year = year
        self.CERTITEM_title = title
        # add ":" after title only if necessary
        self.CERTITEM_details = (details[0],(f": {details[1]}." if details[1] != "" else ""))
        self.CERTITEM_comment = comment
        self.CERTITEM_include = include


class CertificateGroup:
    """Group of certificates for a single category of certificate, like languages, courses, etc.
    """
    def __init__(
        self,
        groupTitle: tuple[str, str],
        content: tuple[str, list[CertificateSub]],
        comment: tuple[str, str],
        include: tuple[str, str],
    ):
        self.CERT_groupTitle = groupTitle
        self.CERT_content = content
        self.CERT_comment = comment
        self.CERT_include = include
