from datetime import date
from typing import Union

class CertificateItem:
    def __init__(self,
                 year: tuple[str, str],
                 title: tuple[str, str],
                 details:tuple[str, str],
                 comment:tuple[str, str],
                 include:tuple[str, str],
                 ):
        self.CERTITEM_year = year
        self.CERTITEM_title = title
        self.CERTITEM_details = details
        self.CERTITEM_comment = comment
        self.CERTITEM_include = include


class CertificateGroup:
    def __init__(self,
                 groupTitle: tuple[str, str],
                 content: tuple[str, list[CertificateItem]],
                 comment:tuple[str, str],
                 include:tuple[str, str],
                 ):
        self.CERT_groupTitle = groupTitle
        self.CERT_content = content
        self.CERT_comment = comment
        self.CERT_include = include