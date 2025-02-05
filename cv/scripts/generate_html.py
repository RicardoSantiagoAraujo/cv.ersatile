from classes.experience import Experience
from datetime import date
import sys
import os
from content_generation import *
from enums.output_type import OutputType

# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
os.chdir(script_directory)


#### Python script to generate a HTML file
def generate_html():
    # check if correct number of arguments is passed:
    if len(sys.argv) == 4:
        profile = sys.argv[1]
        section = sys.argv[2]
        lang = sys.argv[3]

        contentDict = import_contents_dict(
            f"../profiles/examples/{profile}/elements/{section}"
        )
        output_content = generate_contents(
            contentDict,
            f"./templates/{section}/template.html",
            "<!-- ====== Spacer ====== -->\n",
            OutputType("html")
        )
        generate_output_file(
            output_content,
            f"../profiles/examples/{profile}/webpage/{section}/{section}_contents_{lang}.html",
        )
    else:
        print(
            """
              =================================================================
              COMMAND USE:
              python <profile id> generate_html.py <section> <language id>

              example: python generate_html.py johnDoe experience en
              =================================================================
              """
        )


if __name__ == "__main__":
    generate_html()
