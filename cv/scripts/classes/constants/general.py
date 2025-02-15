class General:
    def __init__(
        self,
        name: tuple[str, str],
        title: tuple[str, str],
        birthDay: tuple[str, int],
        birthMonth: tuple[str, int],
        birthYear: tuple[str, int],
        street: tuple[str, str],
        city: tuple[str, str],
        country: tuple[str, str],
        email: tuple[str, str],
        linkedIn: tuple[str, str],
        phone: tuple[str, str],
        site: tuple[str, str],
        picture: tuple[str, str],
        signature: tuple[str, str],
        picCropTop: tuple[
            str, str
        ],  # "pic" instead of "picture" to avoid being replaced by picture
        picCropRight: tuple[str, str],
        picCropBottom: tuple[str, str],
        picCropLeft: tuple[str, str],
        myPictureStyleExtras: tuple[str, str],
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

        self.CONST_birthDate: tuple[str, str] = (
            "",
            f"{birthYear[0]}-{birthMonth[0]}-{birthDay[0]}",
        )
