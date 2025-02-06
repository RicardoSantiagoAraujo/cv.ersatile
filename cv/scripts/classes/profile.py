class Profile:
    def __init__(self,
                VAR_name: dict[str, str],
                VAR_title: dict[str, str],
                VAR_birthDay:dict[str, int],
                VAR_birthMonth:dict[str, int],
                VAR_birthYear: dict[str, int],
                VAR_street:dict[str, str],
                VAR_city: dict[str, str],
                VAR_country: dict[str, str],
                VAR_email: dict[str, str],
                VAR_linkedIn: dict[str, str],
                VAR_phone: dict[str, str],
                VAR_site: dict[str, str],
                VAR_picture: dict[str, str],
                VAR_signature: dict[str, str],
                VAR_pictureCropTop: dict[str, str],
                VAR_pictureCropRight: dict[str, str],
                VAR_pictureCropBottom: dict[str, str],
                VAR_pictureCropLeft: dict[str, str],
                VAR_myPictureStyleExtras : dict[str, str]
                 ):
        self.VAR_name = VAR_name
        self.VAR_title = VAR_title
        self.VAR_birthDay = VAR_birthDay
        self.VAR_birthMonth = VAR_birthMonth
        self.VAR_birthYear = VAR_birthYear
        self.VAR_street = VAR_street
        self.VAR_city = VAR_city
        self.VAR_country = VAR_country
        self.VAR_email = VAR_email
        self.VAR_linkedIn = VAR_linkedIn
        self.VAR_phone = VAR_phone
        self.VAR_site = VAR_site
        self.VAR_picture = VAR_picture
        self.VAR_signature = VAR_signature
        self.VAR_pictureCropTop = VAR_pictureCropTop
        self.VAR_pictureCropRight = VAR_pictureCropRight
        self.VAR_pictureCropBottom = VAR_pictureCropBottom
        self.VAR_pictureCropLeft = VAR_pictureCropLeft
        self.VAR_myPictureStyleExtras = VAR_myPictureStyleExtras