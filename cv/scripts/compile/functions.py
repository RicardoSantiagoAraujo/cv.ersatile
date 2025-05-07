
import os
import argparse
from datetime import datetime
from scripts.utils.helpers import list_existing_profiles, list_existing_versions
import scripts.utils.style_console_text as sty
import enum
from scripts.compile.parameters import (
    profiles_directory,
    examples_folder,
    build_folder__aux_files,
    build_folder__main_output,
)
from scripts.enums.Recipe import Recipe


# get the directory of the current script
base_dir = os.path.dirname(os.path.realpath(__file__))  # dir of current file
profiles_dir_path = os.path.join(base_dir, profiles_directory)

profiles_names = list_existing_profiles(profiles_dir_path, print_list=False)
examples_names = list_existing_profiles(profiles_dir_path+examples_folder, print_list=False)
all_names = profiles_names + examples_names

# create list of all cv versions that can be compiled from all profiles (each entry is a tupple of cv doc name and its profile)
all_cv_documents = []
for name in profiles_names:
    versions = list_existing_versions(os.path.join(profiles_dir_path, name))
    all_cv_documents += [{"doc":version, "profile":name} for version in versions]
for name in examples_names:
    versions = list_existing_versions(os.path.join(profiles_dir_path, examples_folder, name))
    all_cv_documents += [{"doc":version, "profile":name} for version in versions]
# remove extensions
all_cv_documents = [{"doc":os.path.splitext(x["doc"])[0], "profile":x["profile"]} for x in all_cv_documents]

def list_as_string(list: list[any], sep:str=", ") -> str:
    """create a string out of a python list.

    Args:
        list (list[any]): list from which to create a string
        sep (str, optional): Separator between list items. Defaults to ", ".

    Returns:
        str: A string made out of the list items.
    """
    return sep.join([f"{sty.blue}{e}{sty.reset}" for e in list])


def enum_list_as_string(enumName: enum.Enum, sep:str=", ") -> str:
    """create a string out of a python Enum.

    Args:
        enumName (enum.Enum): Enum from which to create a string
        sep (str, optional): Separator between Enum items. Defaults to ", ".

    Returns:
        str: A sring made out of the Enum options.
    """
    return sep.join([f"{sty.blue}{e.value}{sty.reset}" for e in enumName])


profiles_list_as_string = list_as_string(profiles_names) + list_as_string(examples_names)


def deal_with_user_input(args__cmd_line: argparse.Namespace) -> argparse.Namespace:
    """Manage user arguments passed through the command line, and collect missing ones through the input() command.
    Additionally, perform tests for availability, quit commands and index inputs.

    Args:
        args__cmd_line (argparse.Namespace): user passed arguments through the command line

    Returns:
        argparse.Namespace: Validated and updated arguments
    """
    # Make variable all_names accessible within function
    global all_names
    global all_cv_documents
    # If something has been provided in the command line as first argument but it is the build recipe:
    if args__cmd_line.cv_document in [e.value for e in Recipe]:
        # Pass it to the right arg and empty the thing_name arg
        args__cmd_line.recipe = args__cmd_line.cv_document
        args__cmd_line.cv_document = None


    # get and test user input thing (target document) as passed through the command line; may be empty in which case input is collected with the input() command
    cv_doc_from_cmd_line = args__cmd_line.cv_document

    keep_asking = True
    while keep_asking == True:
        # If no thing name has been provided in the command line directly, request it from the user
        if cv_doc_from_cmd_line == None:
            profile_names = list_existing_profiles(
                profiles_dir_path,
                header_message="Your CV Profiles:",
            )
            example_names = list_existing_profiles(
                profiles_dir_path+examples_folder,
                header_message="Examples:",
                cnt_start=len(profile_names),
            )
            all_names = profile_names + example_names
            indexes = list(range(1, len(all_names) + 1))
            choice = input(
                f"Which profile do you want to compile from ? ({sty.blue}choose from options above{sty.reset}): "
            )
            #  if user passed an instruction to quit the program:
            if choice in ["q", "quit"]:
                print(f"\n💀💀💀 {sty.red}Program quit without compiling anything.{sty.reset}")
                exit()
            # if user picked a valid index (number):
            elif choice.isdigit() and int(choice) in indexes:
                thing_name = all_names[int(choice) - 1]
            # if user wrote the article name directly and it is valid:
            elif choice in all_names:
                thing_name = choice
            # if invalid choice (non existing name or index):
            else:
                print(f"\n\n\n{sty.red}Invalid choice{sty.reset}, pick from options:\n")
                continue

            args__cmd_line.profile_name = thing_name
            keep_asking = False

        # If thing name has been provided...
        # ...but it does not actually exist:


        elif cv_doc_from_cmd_line not in [x["doc"] for x in all_cv_documents]:
            print(f"\n\n\n{sty.red}cv document{sty.reset} does not exist, pick from options:\n")
            # Restart proccess
            thing_name = None
        # ...and it exists:
        else:
            # Exit loop
            args__cmd_line.cv_document = cv_doc_from_cmd_line
            args__cmd_line.profile_name = [cv["profile"] for cv in all_cv_documents if cv.get("doc") == cv_doc_from_cmd_line][0] 
            keep_asking = False

    if not vars(args__cmd_line).get("cv_document"):
        print(f"Chosen profile: {sty.blue}{args__cmd_line.profile_name}{sty.reset}")
    else:
        print(f"Chosen cv document: {sty.blue}{args__cmd_line.cv_document}{sty.reset}")
    return args__cmd_line


def ask_which_version_to_compile(build_dir: "str") -> str:
    keep_asking = True
    while keep_asking == True:
        v_names = list_existing_versions(
            build_dir,
            header_message="\nAvailable versions:",
        )
        indexes = list(range(1, len(v_names) + 1))
        choice = input(
            f"Which version do you want to compile? ({sty.blue}choose from options above{sty.reset}): "
        )
        #  if user passed an instruction to quit the program:
        if choice in ["q", "quit"]:
            print(f"\n💀💀💀 {sty.red}Program quit without compiling anything.{sty.reset}")
            exit()
        # if user picked a valid index (number):
        elif choice.isdigit() and int(choice) in indexes:
            version_to_compile = v_names[int(choice) - 1]
        # if user wrote the article name directly and it is valid:
        elif choice in v_names or choice+".tex" in v_names:
            version_to_compile =  choice
        # if invalid choice (non existing name or index):
        else:
            print(f"\n\n\n{sty.red}Invalid choice{sty.reset}, pick from options:\n")
            continue
        print_choice_mesg(version_to_compile)
        return version_to_compile




def print_choice_mesg(choice:str) -> None:
    """print a string announcing the document chosen by the user.

    Args:
        args (argparse.Namespace): an argument namespace.
    """
    print(f"You have chosen to compile {sty.green}{choice}{sty.reset}\n...")



def get_build_directory(args: argparse.Namespace) -> str:
    """ determine directory where to perform build

    Args:
        args (argparse.Namespace): arguments passed by the user

    Returns:
        str: path to build directory
    """
    if args.profile_name in profiles_names:
        dir_path = profiles_dir_path
    elif args.profile_name in examples_names:
        dir_path = profiles_dir_path + examples_folder
    build_directory = os.path.join(dir_path, args.profile_name)
    return build_directory




def create_build_directories() -> None:
    """
    Create required build directories if they do not exist yet
    """
    if not os.path.exists(build_folder__main_output):
        os.makedirs(build_folder__main_output)
    if not os.path.exists(build_folder__aux_files):
        os.makedirs(build_folder__aux_files)


def build_message(msg: str, counter: int,time_start : datetime, time_prev: datetime | None = None, isTimer: bool = True) -> datetime:
    """Print message reporting the compilation progress.

    Args:
        msg (str): Message to be printed to console.
        counter (int): A counter to be incremented with each call of the function.
        time_start (datetime): Time corresponding to the beginning of the compilation process (T0)
        time_prev (datetime | None, optional): Time corresponding to the previous compilation step (Tn-1). Defaults to None.
        isTimer (bool, optional): Whether to print the messages or only increment the counter. Defaults to True.

    Returns:
        datetime: _description_
    """
    counter+=1
    print(f"{sty.blue}{msg}{sty.reset} (step {counter})")
    if isTimer:
        time_now = datetime.now()
        delta_start = time_now - time_start
        print(f"\t⏲ {"Elapsed time since beginning:":<30} {sty.green}{round(delta_start.total_seconds(), 2)}{sty.reset} seconds")
        if time_prev != None:
            delta_prev = time_now - time_prev
            print(f"\t⏲ {"Elapsed time since prev. step:":<30} {sty.green}{round(delta_prev.total_seconds(), 2)}{sty.reset} seconds")
        return (time_now, counter)
    return (None, counter)