from classes.experience import Experience
from classes.education import Education
from datetime import date
import sys
import os
from content_generation import *
from enums.output_type import OutputType
from enums.constant_type import ConstantType
from enums.languages import Language
from enums.profiles import Profile

# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
os.chdir(script_directory)

#### Python script to generate a LaTeX file
def generate_latex():
    # check if correct number of arguments is passed:
    if len(sys.argv) == 5:
        profile = Profile(sys.argv[1]).value
        constant_type = ConstantType(sys.argv[2]).value
        lang = Language(sys.argv[3]).value
        filetype = OutputType(sys.argv[4]).value

        contentDict = import_contents_dict(
            f"../profiles/examples/{profile}/constants",
            constant_type
        )

        # Choose input template and outfile file paths depending on the desired filetype
        if filetype == "latex":
            template_path = f"./templates/constants/{constant_type}/template.tex"
            output_path = f"../profiles/examples/{profile}/constants/{constant_type}.tex"
        elif filetype == "html":
            template_path = f"./templates/constants/{constant_type}/template.html"
            output_path = f"../profiles/examples/{profile}/webpage/{constant_type}.html"


        output_content = generate_contents(
            contentDict,
            template_path,
            "",
            OutputType(filetype)
        )


        generate_output_file(
            output_content,
            output_path,
        )
    else:
        print_instructions(
        ("profile id", f"id of the person whose CV is to be generated {[e.value for e in Profile]}", Profile),
        ("constant type" , f"Constant type to be generated {[e.value for e in ConstantType]}", ConstantType),
        ("languade id" , f"language version of the CV content {[e.value for e in Language]}", Language),
        ("file type" , f"type of file to be generated {[e.value for e in OutputType]}", OutputType),
        )

if __name__ == "__main__":
    generate_latex()
