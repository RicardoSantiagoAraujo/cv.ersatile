from classes.settings.generationSettings import GenerationSettings # type: ignore
from classes.constants.general import General # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={
        "tex":"",
        "ts":""
        },
    subtemplates={},
)

contentDict_full_en = {
    "example": General(
        name = ("" , "John"),
        surname = ("" , "Doe"),
        title = ("" , "MSc"),
        gender = ("", ""),
        nationality = ("", ""),
        birthDay = ("" , 1),
        birthMonth = ("" , 1),
        birthYear = ("" , 1993),
        street = ("" , "1 Downing Street"),
        city = ("" , "London"),
        postcode = ("" , "000000"),
        country = ("", "UK"),
        email = ("","john.doe@gmail.com"),
        linkedIn = ("","john-doe"),
        github = ("","john-doe"),
        phone = ("","1234567890"),
        site = ("","johndoe.com"),
        picture = ("","images/johnDoe_portrait.png"),
        picCropTop = ("","10mm"),
        picCropRight = ("","10mm"),
        picCropBottom = ("","20mm"),
        picCropLeft = ("","10mm"),
        myPictureStyleExtras = ("", ""),
        drivingLicense = ("", "B"),
        signature = ("","images/signatures/signature.png"),
        comment = ("", "General constants for johnDoe"),
        )
    }