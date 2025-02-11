class General:
    def __init__(self,
                name: dict[str, str],
                title: dict[str, str],
                birthDay:dict[str, int],
                birthMonth:dict[str, int],
                birthYear: dict[str, int],
                street:dict[str, str],
                city: dict[str, str],
                country: dict[str, str],
                email: dict[str, str],
                linkedIn: dict[str, str],
                phone: dict[str, str],
                site: dict[str, str],
                picture: dict[str, str],
                signature: dict[str, str],
                picCropTop: dict[str, str], # "pic" instead of "picture" to avoid being replaced by picture
                picCropRight: dict[str, str],
                picCropBottom: dict[str, str],
                picCropLeft: dict[str, str],
                myPictureStyleExtras : dict[str, str]
                 ):
        self.CONST_name = name
        self.CONST_title = title
        self.CONST_birthDay = birthDay
        self.CONST_birthMonth = birthMonth
        self.CONST_birthYear = birthYear
        self.CONST_street = street
        self.CONST_city = city
        self.CONST_country = country
        self.CONST_email = email
        self.CONST_linkedIn = linkedIn
        self.CONST_phone = phone
        self.CONST_site = site
        self.CONST_picture = picture
        self.CONST_signature = signature
        self.CONST_picCropTop = picCropTop
        self.CONST_picCropRight = picCropRight
        self.CONST_picCropBottom = picCropBottom
        self.CONST_picCropLeft = picCropLeft
        self.CONST_myPictureStyleExtras = myPictureStyleExtras

        self.CONST_birthDate:dict[str,str] = {"" : f"{list(birthYear.values())[0]}-{list(birthMonth.values())[0]}-{list(birthDay.values())[0]}"}