from datetime import date
import sys
import os
from pathlib import Path
import json 
import scripts.utils.style_console_text as sty
# Enums
from enum import EnumMeta  # an alias of EnumType in 3.11+, so can still use it
from scripts.enums.OutputTypes import OutputType


# Function to import a dictionary from a different path by adding it to the recognized paths
def import_contents_and_settings(path: str, type: str, version: str, lang: str):
    sys.path.insert(0, path)
    # __import__ works like "from ... import ...", but import can be decided at runtime
    module_content = __import__(type, fromlist=[f"contentDict_{version}_{lang}"])
    contentDict = getattr(module_content, f"contentDict_{version}_{lang}")
    # Settings
    module_settings = __import__(type, fromlist=[f"generation_settings"])
    settings = getattr(module_settings, f"generation_settings")
    # Return content and settings
    return contentDict, settings


def getTemplateFolder(settings, filetype):
    template = settings.templates[filetype]
    # template = template+"/" if template != "" else ""
    return template


def generate_contents(
    source_dict: dict,
    template_path: str,
    pre_content: str = "",
    post_content: str = "",
    inbetween_content: str = "",
    output_type: OutputType = OutputType("tex"),
):
    # Create subtemplate path from template path
    subtemplate_path = getSubtemplatePath(template_path, output_type)
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
                template_content,
                entry_obj_attributes,
                entry_obj,
                output_type,
                subtemplate_path,
            )
            # Add newly create entry into the output file
            generated_content += new_content

            ### add inbetween content as long as last entry is not reached
            if i != (len(source_dict) - 1):
                generated_content += inbetween_content
    ### add prefix and suffix
    generated_content = f"{pre_content}{generated_content}{post_content}"
    # Return generated string
    return generated_content


def get_obj_attributes(obj):
    # Get list of non-special attributes of entry class
    obj_attributes = [a for a in dir(obj) if not a.startswith("__")]
    # Sort by descending order
    obj_attributes = sorted(obj_attributes, key=len, reverse=True)
    # print(obj_attributes)
    return obj_attributes


def replace_placeholders_in_template(
    template: str,
    placeholder_strings: list,
    entry_object,
    output_type: OutputType,
    subtemplate_path: str = "",
):
    # Iterate over attributes and replace them into the template
    for attr in placeholder_strings:
        kv_pair = getattr(entry_object, attr)
        key = kv_pair[0]
        val = kv_pair[1]
        # if date, format properly
        val = formatDate(val)
        # if string, format properly
        val = formatString(val)
        # if list of subObjects, format properly
        val = formatSubObjects(val, output_type, subtemplate_path)
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
    print("+++++++++++++++++++++++++++++++++++++++++")
    print(f"✅ {sty.green}Output file generated successfully!{sty.reset} ✅")
    print("+++++++++++++++++++++++++++++++++++++++++")
    print(f"Output: {sty.blue}{output_file_path}{sty.reset}")
    print("\n")


def formatDate(x):
    if type(x) == date:
        x = x.strftime("%Y-%m-%d")
    return x


def formatString(x):
    # if type(x) == str:
    #     x = x
    return x


# check type of a variable, and if it is an item, of all contained intems
def checktype(obj, type):
    return bool(obj) and all(isinstance(elem, type) for elem in obj)


def formatSubObjects(list_subobjs, output_type: OutputType, subtemplate_path: str):
    # check if it is a list AND contains only subobjects
    if type(list_subobjs) == list and checktype(list_subobjs, object):
        # empty string to be filled
        generated_content = """"""
        # iterate over object
        for subobj in list_subobjs:
            # get attributes of sub-objects
            entry_obj_attributes = get_obj_attributes(subobj)
            # read subtemplate
            with open(subtemplate_path, "r") as template_file:
                templateItem_content = template_file.read()
                # replace placeholders in subtemplate (this should make the function recursive!)
                new_subcontent = replace_placeholders_in_template(
                    template=templateItem_content,
                    placeholder_strings=entry_obj_attributes,
                    entry_object=subobj,
                    output_type=output_type,
                )
            # keep adding to string
            generated_content += new_subcontent + "\n"
        return generated_content
    else:
        # Leave as is if not a list of subobjects
        return list_subobjs


def print_instructions(module_dotted_name: str, *args: dict) -> None: # kwargs is a dictionary
    print("--------------------------")
    print(sys.argv)
    module_name = sys.modules[module_dotted_name].__spec__.name

    print(
        f"""
    \t =================================================================
    \t HOW TO USE THIS COMMAND:
    \t {sty.blue} python[3] -m {sty.yellow} {module_name} {sty.cyan} {" ".join(f"<{la}>" for la,de,ex in args)}{sty.reset}
    """
    )
    # Print list of arguments and their definitions
    for label, definition, enum in args:
        availanle_options = ", ".join([f"{sty.blue}{e.value}{sty.reset}" for e in enum])
        print(f"\t\t► {sty.green}{label}{sty.reset} : {definition} ({availanle_options})")
    # Print use case example, if an enum has been passed, print first element of it
    print(
        f"""
    \tEXAMPLE:{sty.blue} python[3] -m {sty.yellow} {module_name} {sty.cyan} {" ".join([(list(ex)[0].value if isinstance(ex, EnumMeta) else ex) for la,de,ex in args])}{sty.reset}
    \t=================================================================
    """
    )


def generate_json(inputDict: dict, profile: str, name: str, version: str, lang: str):
    # Convert objects to dictionaries, place each one in a merged dictionary
    merged_data = {}
    for label, obj in inputDict.items():
        merged_data[label] = obj.__dict__

    # save dictionary as json
    with open(f"../../profiles/{profile}/webpage/data/{name}_{version}_{lang}.json", "w") as outfile:
        json.dump(merged_data, outfile, indent=4, sort_keys=True, default=str)


# default message for auto generated content
auto_warning = f" /!\\ CONTENT GENERATED WITH PYTHON SCRIPT, CHANGES MADE DIRECTLY HERE MAY BE OVERWRITTEN /!\\ "


# Create subtemplate path from template path
def getSubtemplatePath(template_path: str, output_type: OutputType):
    return template_path.replace(f"/template.{output_type.name}", f"/sub-template.{output_type.name}")
