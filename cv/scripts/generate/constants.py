from datetime import date
import sys
import os
from scripts.utils.style_console_text import blue, green, reset

# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
os.chdir(script_directory)
# print(script_directory)
from scripts.utils.content_generation import *

### Enums
from scripts.enums.OutputTypes import OutputType
from scripts.enums.ConstantTypes import ConstantType
from scripts.enums.Languages import Language
from scripts.enums.Profiles import Profile
from scripts.enums.Versions import Version


#### Python script to generate a file
def main() -> None:
    """Python script to generate a file for constants.
    This script generates a file for constants based on the provided profile, constant type, version, language, and file type.
    """
    # check if correct number of arguments is passed:
    if len(sys.argv) == 6:
        profile = Profile(sys.argv[1]).value
        constant_type = ConstantType(sys.argv[2]).value
        version: str = Version(sys.argv[3]).value  # not actually useful here
        lang = Language(sys.argv[4]).value  # not actually useful here
        filetype = OutputType(sys.argv[5]).value

        contentDict, settings = import_contents_and_settings(
            f"../../profiles/{profile}/constants", constant_type, version, lang
        )
        generate_json(contentDict, profile, constant_type, version, lang)

        # Choose input template and outfile file paths depending on the desired filetype
        global auto_warning  # tell the interpreter to find variable a in the global scope

        template = getTemplateFolder(settings, filetype)

        template_path = f"./../templates/constants/{constant_type}/{template}/template.{filetype}"

        if filetype == "tex":
            output_path = f"../../profiles/{profile}/constants/{constant_type}.tex"
            auto_warning = f"%{auto_warning}\n"
        elif filetype == "ts":
            output_path = f"../../profiles/{profile}/webpage/scripts/constants/{constant_type}.ts"
            auto_warning = f"//{auto_warning}\n"
        elif filetype == "scss":
            output_path = f"../../profiles/{profile}/webpage/styles/constants/_{constant_type}.scss"
            auto_warning = f"//{auto_warning}\n"
            # add "_" if template is scss
            template_path = f"./../templates/constants/{constant_type}/{template}/_template.{filetype}"
        else:
            return print(f"/!\\ {filetype} generation not available for {Path(__file__).name}")

        output_content = generate_contents(
            source_dict=contentDict,
            template_path=template_path,
            pre_content=auto_warning,
            post_content="",
            inbetween_content="",
            output_type=OutputType(filetype),
        )

        generate_output_file(
            output_content,
            output_path,
        )
    else:
        print_instructions(
            __name__,
            (
                "profile id",
                f"id of the person whose CV is to be generated",
                Profile,
            ),
            (
                "constant type",
                f"Constant type to be generated",
                ConstantType,
            ),
            (
                "version",
                f"CV version to be generated",
                Version,
            ),
            (
                "languade id",
                f"language version of the CV content",
                Language,
            ),
            (
                "file type",
                f"type of file to be generated",
                OutputType,
            ),
        )


if __name__ == "__main__":
    main()
