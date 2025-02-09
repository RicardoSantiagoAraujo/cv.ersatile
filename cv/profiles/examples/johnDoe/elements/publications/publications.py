from classes.publications import Publication # type: ignore
from datetime import date

contentDict = {
    "example1": Publication(
        PUB_key={"": "mypublications:johnDoe"},
        PUB_fullText={"": "Entry contents"},
        PUB_include={"":"true"},
    ),
    "example2": Publication(
        PUB_key={"": ""},
        PUB_fullText={"": "John Doe (Feb. 2023). “The Joy of Fullstack Developing”"},
        PUB_include={"":"true"},
    ),
}
