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
def generate_section():
    # check if correct number of arguments is passed:
    if len(sys.argv) == 6:
        profile = Profile(sys.argv[1]).value
        section = SectionType(sys.argv[2]).value
        version:str = Version(sys.argv[3]).value
        lang = Language(sys.argv[4]).value
        filetype = OutputType(sys.argv[5]).value

        contentDict = import_contents_dict(
            f"../profiles/{profile}/elements/{section}",
            section,
            version,
            lang
        )

        generate_json(contentDict, profile, section, version, lang)


        # Choose input template and outfile file paths depending on the desired filetype
        separator = ""
        auto_warning = " /!\ CONTENT GENERATED WITH PYTHON SCRIPT, CHANGES MADE DIRECTLY HERE MAY BE OVERWRITTEN /!\ "
        if filetype == "latex":
            template_path = f"./templates/sections/{section}/template.tex"
            output_path = f"../profiles/{profile}/elements/{section}/{section}_contents_{version}_{lang}.tex"
            auto_warning = f"%{auto_warning}"
            if section in ["experience", "education", "popScience", "research", "teaching"]:
                separator =  "\n\\myTablesSeparator%"
        elif filetype == "html":
            template_path = f"./templates/sections/{section}/template.html"
            output_path = f"../profiles/{profile}/webpage/sections/{section}/{section}_contents_{version}_{lang}.html"
            separator = "<!-- ====== Spacer ====== -->\n"
            auto_warning = f"<!-- {auto_warning} -->\n"
        else:
            return print(f"/!\\ {filetype} generation not available for f{Path(__file__).name}")

        output_content = generate_contents(
            source_dict = contentDict,
            template_path = template_path,
            pre_content=auto_warning,
            post_content="",
            inbetween_content = separator,
            output_type = OutputType(filetype)
        )
        generate_output_file(
            output_content,
            output_path,
        )
    else:
        print_instructions(
        ("profile id", f"id of the person whose CV is to be generated {[e.value for e in Profile]}", Profile),
        ("section" , f"CV section to be generated {[e.value for e in SectionType]}", SectionType),
        ("version" , f"CV version to be generated {[e.value for e in Version]}", Version),
        ("languade id" , f"language version of the CV content {[e.value for e in Language]}", Language),
        ("file type" , f"type of file to be generated {[e.value for e in OutputType]}", OutputType),
        )


if __name__ == "__main__":
    generate_section()
