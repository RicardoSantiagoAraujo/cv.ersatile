from classes.experience import Experience
from classes.education import Education
from datetime import date
import sys
import os
from content_generation import *
from enums.output_type import OutputType
from enums.section_type import SectionType

# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
os.chdir(script_directory)


#### Python script to generate a HTML file
def generate_html():
    # check if correct number of arguments is passed:
    if len(sys.argv) == 5:
        profile = sys.argv[1]
        section = SectionType(sys.argv[2]).value
        lang = sys.argv[3]
        filetype = OutputType(sys.argv[4]).value

        contentDict = import_contents_dict(
            f"../profiles/examples/{profile}/elements/{section}",
            section
        )

        # Choose input template and outfile file paths depending on the desired filetype
        if filetype == "latex":
            template_path = f"./templates/sections/{section}/template.html"
            output_path = f"../profiles/examples/{profile}/elements/{section}/{section}_contents_{lang}.tex"
        elif filetype == "html":
            template_path = f"./templates/sections/{section}/template.html"
            output_path = f"../profiles/examples/{profile}/webpage/{section}/{section}_contents_{lang}.html"

        output_content = generate_contents(
            contentDict,
            template_path,
            "<!-- ====== Spacer ====== -->\n",
            OutputType("html")
        )
        generate_output_file(
            output_content,
            output_path,
        )
    else:
        print(
            """
              =================================================================
              COMMAND USE:
              python <profile id> generate_section.py <section> <language id> <output file type>

              example: python generate_section.py johnDoe experience en html
              =================================================================
              """
        )


if __name__ == "__main__":
    generate_html()
