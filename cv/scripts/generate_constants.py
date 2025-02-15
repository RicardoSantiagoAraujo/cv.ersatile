from datetime import date
import sys
import os

# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
os.chdir(script_directory)
# print(script_directory)
from content_generation import *

### Enums
from enums.output_types import OutputType
from enums.constant_types import ConstantType
from enums.languages import Language
from enums.profiles import Profile
from enums.versions import Version


#### Python script to generate a file
def generate_constants():
    # check if correct number of arguments is passed:
    if len(sys.argv) == 6:
        profile = Profile(sys.argv[1]).value
        constant_type = ConstantType(sys.argv[2]).value
        version: str = Version(sys.argv[3]).value  # not actually useful here
        lang = Language(sys.argv[4]).value  # not actually useful here
        filetype = OutputType(sys.argv[5]).value

        contentDict = import_contents_dict(
            f"../profiles/{profile}/constants", constant_type, version, lang
        )

        generate_json(contentDict, profile, constant_type, version, lang)

        # Choose input template and outfile file paths depending on the desired filetype
        global auto_warning  # tell the interpreter to find variable a in the global scope
        template_path = f"./templates/constants/{constant_type}/template.{filetype}"

        if filetype == "tex":
            output_path = f"../profiles/{profile}/constants/{constant_type}.tex"
            auto_warning = f"%{auto_warning}\n"
        elif filetype == "ts":
            output_path = (
                f"../profiles/{profile}/webpage/scripts/constants/{constant_type}.ts"
            )
            auto_warning = f"//{auto_warning}\n"
        elif filetype == "scss":
            output_path = (
                f"../profiles/{profile}/webpage/style/constants/_{constant_type}.scss"
            )
            auto_warning = f"//{auto_warning}\n"
            # add "_" if template is scss
            template_path = (
                f"./templates/constants/{constant_type}/_template.{filetype}"
            )
        else:
            return print(
                f"/!\\ {filetype} generation not available for {Path(__file__).name}"
            )

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
            (
                "profile id",
                f"id of the person whose CV is to be generated {[e.value for e in Profile]}",
                Profile,
            ),
            (
                "constant type",
                f"Constant type to be generated {[e.value for e in ConstantType]}",
                ConstantType,
            ),
            (
                "version",
                f"CV version to be generated {[e.value for e in Version]}",
                Version,
            ),
            (
                "languade id",
                f"language version of the CV content {[e.value for e in Language]}",
                Language,
            ),
            (
                "file type",
                f"type of file to be generated {[e.value for e in OutputType]}",
                OutputType,
            ),
        )


if __name__ == "__main__":
    generate_constants()
