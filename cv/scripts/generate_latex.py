from classes.experience import Experience
from datetime import date
import sys
import os
# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
os.chdir(script_directory)

#### Python script to generate a LaTeX file
def generate_latex():
    # check if correct number of arguments is passed:
    if len(sys.argv) == 4:
        profile=sys.argv[1]
        section=sys.argv[2]
        lang=sys.argv[3]

        contentDict = import_contents_dict(f"../profiles/examples/{profile}/elements/{section}")
        latex_content = generate_latex_contents(contentDict, f"./templates/{section}_template.tex")
        generate_latex_file(latex_content, f"../profiles/examples/{profile}/elements/{section}/{section}_contents_{lang}.tex")
    else:
        print('''
              =================================================================
              COMMAND USE:
              python <profile id> <section> <language id>

              example: python johnDoe experience en
              =================================================================
              ''')

# Function to import a dictionary from a different path by adding it to the recognized paths
def import_contents_dict(path):
    sys.path.insert(0, path)
    from experience import contentDict # type: ignore (ignore python warning)
    return contentDict


def generate_latex_contents(source_dict, tex_template_path:str):
    # Define the LaTeX content as a string
    latex_content = r""""""
    # Iterate over each entry in provided dictionary
    for entry_key, entry_obj in source_dict.items():
        # Get list of non-special attributes of entry clas
        entry_obj_attributes = get_obj_attributes(entry_obj)
        # Read contents of template file:
        with open(tex_template_path, "r") as tex_file:
            template_content = tex_file.read()
            # Replace placeholder strings in tex template to generate an entry
            new_content = replace_placeholders_in_template(template_content, entry_obj_attributes, entry_obj)
            # Add newly create entry into the output file
            latex_content += new_content
    # Return generated tex string
    return latex_content

def get_obj_attributes(obj):
    # Get list of non-special attributes of entry class
    obj_attributes= [a for a in dir(obj) if not a.startswith('__')]
    # print(entry_obj_attributes)
    return obj_attributes

def replace_placeholders_in_template(tex_template, placeholder_strings, entry_object):
    # Iterate over attributes and replace them into the template
    for attr in placeholder_strings:
        # print(attr)
        dict = getattr(entry_object, attr)
        key=list(dict.keys())[0]
        val=list(dict.values())[0]
        tex_template = tex_template.replace(f"KEY_{attr}", str(key))
        tex_template = tex_template.replace(f"VAL_{attr}", str(val))
    return tex_template

def generate_latex_file(latex_content, output_file_path):
    # Open a new .tex file and write the LaTeX content into it
    with open(output_file_path, "w") as tex_file:
        tex_file.write(latex_content)

    print("LaTeX file generated successfully!")


if __name__ == "__main__":
    generate_latex()