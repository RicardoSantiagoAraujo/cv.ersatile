from classes.profile import Profile # type: ignore
from datetime import date

contentDict = {
    "profile": Profile(
        VAR_name = {"" : "John Doe"},
        VAR_title = {"" : "MSc"},
        VAR_birthDay = {"" : 1},
        VAR_birthMonth = {"" : 1},
        VAR_birthYear = {"" : 1993},
        VAR_street = {"" : "1 Downing Street"},
        VAR_city = {"" : "London"},
        VAR_country = {"": "UK"},
        VAR_email = {"":"john.doe@gmail.com"},
        VAR_linkedIn = {"":"john-doe"},
        VAR_phone = {"":"1234567890"},
        VAR_site = {"":"johndoe.com"},
        VAR_picture = {"":"images/johnDoe_portrait.png"},
        VAR_signature = {"":"images/signatures/signature.png"},
        VAR_pictureCropTop = {"":"10mm"},
        VAR_pictureCropRight = {"":"10mm"},
        VAR_pictureCropBottom = {"":"20mm"},
        VAR_pictureCropLeft = {"":"10mm"},
        VAL_VAR_myPictureStyleExtras = {"": ""}
        )
    }