from scripts.classes.settings.GenerationSettings import GenerationSettings  # type: ignore
from scripts.classes.constants.General import General  # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={"tex": "", "ts": ""},
    subtemplates={},
)

contentDict_full_en = {
    "example": General(
        name=("", "Jane"),
        surname=("", "Doe"),
        title=("", "MSc"),
        gender=("", ""),
        nationality=("", ""),
        birthDay=("", 1),
        birthMonth=("", 1),
        birthYear=("", 1995),
        street=("", "1 Wall Street"),
        city=("", "New York"),
        postcode=("", "000000"),
        country=("", "USA"),
        email=("", "jane.doe@gmail.com"),
        linkedIn=("", "jane-doe"),
        github=("", "jane-doe"),
        phone=("", "1234567890"),
        site=("", "janedoe.com"),
        picture=("", "images/janeDoe_portrait.png"),
        picCropTop=("", "10mm"),
        picCropRight=("", "10mm"),
        picCropBottom=("", "20mm"),
        picCropLeft=("", "10mm"),
        myPictureStyleExtras=("", ""),
        drivingLicense=("", "B"),
        signature=("", "images/signatures/signature.png"),
        comment=("", "General constants for janeDoe"),
    )
}
