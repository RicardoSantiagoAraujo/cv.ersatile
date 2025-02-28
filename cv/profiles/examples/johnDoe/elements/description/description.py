from classes.settings.generationSettings import GenerationSettings # type: ignore
from classes.sections.description import Description # type: ignore
from datetime import date

generation_settings = GenerationSettings(
    templates={
        "html":"",
        "tex":""
        },
    subtemplates={
        "html":"",
        "tex":""
        },
)

contentDict_full_en = {
    "descriptionExample": Description(
        content=("Content",
                 ( # Using parentheses to get implied line continuation
                "I am a \myAgeFloor-year-old software developer who loves building applications and learning about new technologies."
                "I am an independent and rigorous individual that thrives in diverse environments. As a proactive team player, I bring not only my technical skills but also a sense of humor and cohesion to every workplace."
                "I am always eager to embrace new challenges, continually learning and growing in both my professional and personal endeavors."
                # "COMMENT OUT TO NOT INCLUDE THIS LINE"
                 )
            ),
        comment=("", "COMMENT GOES HERE"),
    ),
}
