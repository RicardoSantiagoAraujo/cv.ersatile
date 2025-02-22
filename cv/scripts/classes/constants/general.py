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


    # Loop through local variables to generate new variables
        for key, value in locals().items():
            if key != 'self' and key not in ["functionToIgnore"]:  # Don't assign 'self' or functions
                # Dynamically assign the variable to the object
                setattr(
                    self,
                    f"CONST_{key}",
                    value
                    )

        self.CONST_birthDate: tuple[str, str] = (
            "",
            f"{birthYear[1]}-{birthMonth[1]}-{birthDay[1]}",
        )
