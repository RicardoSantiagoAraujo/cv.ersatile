from datetime import date
import sys
import os
from pathlib import Path
import json
# Enums
from enum import EnumType
from enums.output_types import OutputType
from enums.section_types import SectionType
from enums.constant_types import ConstantType
from enums.languages import Language

# Function to import a dictionary from a different path by adding it to the recognized paths
def import_contents_dict(path:str, type:str, version:str, lang:str):
    sys.path.insert(0, path)
    # __import__ works like "from ... import ...", but import can be decided at runtime
    module = __import__(type, fromlist=[f"contentDict_{version}_{lang}"])
    contentDict=getattr(module, f"contentDict_{version}_{lang}")
    return contentDict


def generate_contents(source_dict:dict, template_path: str, inbetween_content:str="", output_type:OutputType=OutputType("latex")):
    # Define the generated content as a string
    generated_content = r""""""
    # Iterate over each entry in provided dictionary
    for i, (entry_key, entry_obj) in enumerate(source_dict.items()):
        # Get list of non-special attributes of entry class
        entry_obj_attributes = get_obj_attributes(entry_obj)
        # Read contents of template file:
        with open(template_path, "r") as template_file:
            template_content = template_file.read()
            # Replace placeholder strings in template to generate an entry
            new_content = replace_placeholders_in_template(
                template_content, entry_obj_attributes, entry_obj, output_type
            )
            # Add newly create entry into the output file
            generated_content += new_content

            ### add inbetween content as long as last entry is not reached
            if i != (len(source_dict) - 1):
                generated_content += inbetween_content
    # Return generated string
    return generated_content


def get_obj_attributes(obj):
    # Get list of non-special attributes of entry class
    obj_attributes = [a for a in dir(obj) if not a.startswith("__")]
    # Sort by descending order
    obj_attributes = sorted(obj_attributes, key=len,  reverse=True)
    return obj_attributes


def replace_placeholders_in_template(template:str, placeholder_strings:list, entry_object, output_type:OutputType):
    # Iterate over attributes and replace them into the template
    for attr in placeholder_strings:
        # print(attr)
        dict = getattr(entry_object, attr)
        key = list(dict.keys())[0]
        val = list(dict.values())[0]
        # if date, format properly
        val = formatDate(val)
        # if string, format properly
        val = formatString(val)
        # if list of strings, format properly
        val = formatListStrings(val,output_type)
        # Replace in template
        template = template.replace(f"KEY_{attr}", str(key))
        template = template.replace(f"VAL_{attr}", str(val))
    return template


def generate_output_file(output_content, output_file_path):
    # Open a new .tex file and write the LaTeX content into it
    # Check whether the specified path exists or not
    output_file_dir = os.path.dirname(output_file_path)
    isExist = os.path.exists(output_file_dir)
    if not isExist:
        # Create a new directory because it does not exist
        os.makedirs(output_file_dir)
        print("The new directory is created!")
    with open(output_file_path, "w") as output_file:
        output_file.write(output_content)
    print("\n")
    print("+++++++++++++++++++++++++++++++++++")
    print("Output file generated successfully!")
    print("+++++++++++++++++++++++++++++++++++")
    print(f"Output: {output_file_path}")
    print("\n")


def formatDate(x):
    if type(x) == date:
        x = x.strftime("%Y-%m-%d")
    return x

def formatString(x):
    # if type(x) == str:
    #     x = x
    return x


def formatListStrings(x, output_type:OutputType):
    if type(x) == list:
        # x = x.strftime("%Y-%m-%d")
        if (output_type==OutputType("html")):
            x = "<ul>\n" + "".join([f"\t\t<li>{i}</li>\n" for i in x]) + "\t</ul>"
        if (output_type==OutputType("latex")):
            x = "\\begin{customlist}\n" + "".join([f"\t\t\t\\item {i}\n" for i in x]) + "\t\t\\end{customlist}"
    return x


def print_instructions(*args:tuple):# kwargs is a dictionary
    print(
    f"""
    \t =================================================================
    \t HOW TO USE THIS COMMAND:
    \t python {Path(__file__).name} {" ".join(f"<{la}>" for la,de,ex in args)}
    """
    )
    # Print list of arguments and their definitions
    for (label, definition, example) in args:
        print(f"\t\t- {label} : {definition}")
    # Print use case example, if an enum has been passes, print first element of it
    print(f"""
    \t EXAMPLE: python {Path(__file__).name} {" ".join([(list(ex)[0].value if isinstance(ex, EnumType) else ex) for la,de,ex in args])}
    \t=================================================================
    """
    )



def generate_json(inputDict: dict, profile: str, name: str, version: str, lang: str):
    # Convert objects to dictionaries, place each one in a merged dictionary
    merged_data = {}
    for label, obj in inputDict.items():
        merged_data[label] =  obj.__dict__

    # save dictionary as json
    with open(f"../profiles/{profile}/webpage/data/{name}_{version}_{lang}.json", "w") as outfile:
        json.dump(merged_data, outfile,
                    indent = 4,
                    sort_keys = True,
                    default = str
                    )