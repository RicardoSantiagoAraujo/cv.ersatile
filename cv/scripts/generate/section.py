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
from scripts.enums.SectionTypes import SectionType
from scripts.enums.Languages import Language
from scripts.enums.Profiles import Profile
from scripts.enums.Versions import Version


#### Python script to generate a file
def generate_section():
    # check if correct number of arguments is passed:
    if len(sys.argv) == 6:
        profile = Profile(sys.argv[1]).value
        section = SectionType(sys.argv[2]).value
        version: str = Version(sys.argv[3]).value
        lang = Language(sys.argv[4]).value
        filetype = OutputType(sys.argv[5]).value

        contentDict, settings = import_contents_and_settings(
            f"../../profiles/{profile}/elements/{section}", section, version, lang
        )

        generate_json(contentDict, profile, section, version, lang)

        # Choose input template and outfile file paths depending on the desired filetype
        separator = ""
        global auto_warning  # tell the interpreter to find variable a in the global scope

        template = getTemplateFolder(settings, filetype)

        template_path = f"./../templates/sections/{section}/{template}/template.{filetype}"

        if filetype == "tex":
            output_path = f"../../profiles/{profile}/elements/{section}/{section}_contents_{version}_{lang}.tex"
            auto_warning = f"%{auto_warning}\n"
            if section in [
                "experience",
                "education",
                "popScience",
                "research",
                "teaching",
            ]:
                separator = "\n\\myTablesSeparator%"
        elif filetype == "html":
            output_path = (
                f"../../profiles/{profile}/webpage/sections/{section}/{section}_contents_{version}_{lang}.html"
            )
            separator = "\n<!-- ====== Spacer ====== -->\n"
            auto_warning = f"<!-- {auto_warning} -->\n"
        else:
            return print(f"/!\\ {filetype} generation not available for f{Path(__file__).name}")

        output_content = generate_contents(
            source_dict=contentDict,
            template_path=template_path,
            pre_content=auto_warning,
            post_content="",
            inbetween_content=separator,
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
                f"id of the person whose CV is to be generated",
                Profile,
            ),
            (
                "section",
                f"CV section to be generated",
                SectionType,
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
    generate_section()
