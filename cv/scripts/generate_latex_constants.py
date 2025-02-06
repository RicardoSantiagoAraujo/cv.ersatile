from classes.experience import Experience
from classes.education import Education
from datetime import date
import sys
import os
from content_generation import *
from enums.output_type import OutputType
from enums.constant_type import ConstantType

# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
os.chdir(script_directory)


#### Python script to generate a LaTeX file
def generate_latex():
    # check if correct number of arguments is passed:
    if len(sys.argv) == 4:
        profile = sys.argv[1]
        constant_type = ConstantType(sys.argv[2]).value
        lang = sys.argv[3]

        contentDict = import_contents_dict(
            f"../profiles/examples/{profile}/constants",
            constant_type
        )
        output_content = generate_contents(
            contentDict,
            f"./templates/constants/{constant_type}/template.tex",
            "\n\\myTablesSeparator%",
            OutputType("latex")
        )
        generate_output_file(
            output_content,
            f"../profiles/examples/{profile}/constants/{constant_type}.tex",
        )
    else:
        print(
            """
              =================================================================
              COMMAND USE:
              python <profile id> generate_latex_constants.py <section> <language id>

              example: python generate_latex_constants.py johnDoe experience en
              =================================================================
              """
        )


if __name__ == "__main__":
    generate_latex()
