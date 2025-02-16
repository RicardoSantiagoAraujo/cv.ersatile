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
        name = ("" , "John Doe"),
        title = ("" , "MSc"),
        birthDay = ("" , 1),
        birthMonth = ("" , 1),
        birthYear = ("" , 1993),
        street = ("" , "1 Downing Street"),
        city = ("" , "London"),
        country = ("", "UK"),
        email = ("","john.doe@gmail.com"),
        linkedIn = ("","john-doe"),
        phone = ("","1234567890"),
        site = ("","johndoe.com"),
        picture = ("","images/johnDoe_portrait.png"),
        signature = ("","images/signatures/signature.png"),
        picCropTop = ("","10mm"),
        picCropRight = ("","10mm"),
        picCropBottom = ("","20mm"),
        picCropLeft = ("","10mm"),
        myPictureStyleExtras = ("", ""),
        )
    }