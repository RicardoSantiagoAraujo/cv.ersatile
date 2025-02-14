from classes.sections.certificates import CertificateGroup, CertificateItem # type: ignore
from datetime import date


contentDict_full_en = {
    "example1": CertificateGroup(
        groupTitle=("","English"),
        comment=("","ENGLISH"),
         include=("","true"),
        content=("",
                  [
                      CertificateItem(
                      year=("", "2011"),
                      title=("", "Cambridge English : First Certificate in English (FCE)"),
                      details=("", "Score: A"),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                      CertificateItem(
                      year=("", "2012"),
                      title=("", "Cambridge English : Certificate in Advanced English (CAE)"),
                      details=("", "Score: B"),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                      CertificateItem(
                      year=("", "2016"),
                      title=("", "IELTS Academic"),
                      details=("", "Overall Band Score: 8.0"),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                      CertificateItem(
                      year=("", "2022"),
                      title=("", "TOEIC"),
                      details=("", ""),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                  ]
                  ),
        ),
}
