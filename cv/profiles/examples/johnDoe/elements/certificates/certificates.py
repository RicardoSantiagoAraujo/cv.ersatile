from classes.settings.generationSettings import GenerationSettings # type: ignore
from classes.sections.certificates import CertificateGroup, CertificateSub # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={
        "html":"",
        "tex":""
        },
    subtemplates={
        "html":"",
        "tex":""
        },
)

contentDict_full_en = {
    "example1": CertificateGroup(
        groupTitle=("","English"),
        comment=("","ENGLISH"),
         include=("","true"),
        content=("",
                  [
                      CertificateSub(
                      year=("", "2011"),
                      title=("", "Cambridge English : First Certificate in English (FCE)"),
                      details=("", "Score: A"),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                      CertificateSub(
                      year=("", "2012"),
                      title=("", "Cambridge English : Certificate in Advanced English (CAE)"),
                      details=("", "Score: B"),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                      CertificateSub(
                      year=("", "2016"),
                      title=("", "IELTS Academic"),
                      details=("", "Overall Band Score: 8.0"),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                      CertificateSub(
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
