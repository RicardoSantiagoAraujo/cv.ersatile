class Profile:
    def __init__(self,
                CONST_name: dict[str, str],
                CONST_title: dict[str, str],
                CONST_birthDay:dict[str, int],
                CONST_birthMonth:dict[str, int],
                CONST_birthYear: dict[str, int],
                CONST_street:dict[str, str],
                CONST_city: dict[str, str],
                CONST_country: dict[str, str],
                CONST_email: dict[str, str],
                CONST_linkedIn: dict[str, str],
                CONST_phone: dict[str, str],
                CONST_site: dict[str, str],
                CONST_picture: dict[str, str],
                CONST_signature: dict[str, str],
                CONST_picCropTop: dict[str, str], # "pic" instead of "picture" to avoid being replaced by CONST_picture
                CONST_picCropRight: dict[str, str],
                CONST_picCropBottom: dict[str, str],
                CONST_picCropLeft: dict[str, str],
                CONST_myPictureStyleExtras : dict[str, str]
                 ):
        self.CONST_name = CONST_name
        self.CONST_title = CONST_title
        self.CONST_birthDay = CONST_birthDay
        self.CONST_birthMonth = CONST_birthMonth
        self.CONST_birthYear = CONST_birthYear
        self.CONST_street = CONST_street
        self.CONST_city = CONST_city
        self.CONST_country = CONST_country
        self.CONST_email = CONST_email
        self.CONST_linkedIn = CONST_linkedIn
        self.CONST_phone = CONST_phone
        self.CONST_site = CONST_site
        self.CONST_picture = CONST_picture
        self.CONST_signature = CONST_signature
        self.CONST_picCropTop = CONST_picCropTop
        self.CONST_picCropRight = CONST_picCropRight
        self.CONST_picCropBottom = CONST_picCropBottom
        self.CONST_picCropLeft = CONST_picCropLeft
        self.CONST_myPictureStyleExtras = CONST_myPictureStyleExtras