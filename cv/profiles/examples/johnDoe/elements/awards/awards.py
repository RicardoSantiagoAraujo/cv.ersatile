from classes.sections.awards import AwardGroup, AwardItem # type: ignore
from datetime import date


contentDict_full_en = {
    "example1": AwardGroup(
        groupTitle=("","Academic"),
        comment=("","ACADEMIC"),
         include=("","true"),
        content=("",
                  [
                      AwardItem(
                      year=("", "2015"),
                      title=("", "Student Merit Award"),
                      details=("", "University of Bristol"),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                      AwardItem(
                      year=("", "2018"),
                      title=("", "Hackathon competition"),
                      details=("", "Second place"),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                  ]
                  ),
        ),
    "example2": AwardGroup(
        groupTitle=("","Sports"),
        comment=("","SPORTS"),
         include=("","true"),
        content=("",
                  [
                      AwardItem(
                      year=("", "2011"),
                      title=("", "National table tenis junior champion"),
                      details=("", ""),
                      comment=("", ""),
                      include=("", "true"),
                    ),
                  ]
                  ),
        ),
}
