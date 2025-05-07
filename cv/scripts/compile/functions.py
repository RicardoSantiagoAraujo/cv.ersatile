
import os
import argparse
from datetime import datetime
from scripts.utils.helpers import list_existing_profiles, list_existing_versions
from scripts.utils.style_console_text import red, green, blue, bold, reset
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

def list_as_string(list: list[any], sep:str=", ") -> str:
    """create a string out of a python list.

    Args:
        list (list[any]): list from which to create a string
        sep (str, optional): Separator between list items. Defaults to ", ".

    Returns:
        str: A string made out of the list items.
    """
    return sep.join([f"{blue}{e}{reset}" for e in list])


def enum_list_as_string(enumName: enum.Enum, sep:str=", ") -> str:
    """create a string out of a python Enum.

    Args:
        enumName (enum.Enum): Enum from which to create a string
        sep (str, optional): Separator between Enum items. Defaults to ", ".

    Returns:
        str: A sring made out of the Enum options.
    """
    return sep.join([f"{blue}{e.value}{reset}" for e in enumName])


profiles_list_as_string = list_as_string(profiles_names)


def deal_with_user_input(args__cmd_line: argparse.Namespace) -> argparse.Namespace:
    """Manage user arguments passed through the command line, and collect missing ones through the input() command.
    Additionally, perform tests for availability, quit commands and index inputs.

    Args:
        args__cmd_line (argparse.Namespace): user passed arguments through the command line

    Returns:
        argparse.Namespace: Validated and updated arguments
    """

    # If something has been provided in the command line as first argument but it is the build recipe:
    if args__cmd_line.thing_name in [e.value for e in Recipe]:
        # Pass it to the right arg and empty the thing_name arg
        args__cmd_line.recipe = args__cmd_line.thing_name
        args__cmd_line.thing_name = None


    # get and test user input thing (target document) as passed through the command line; may be empty in which case input is collected with the input() command
    thing_name_from_cmd_line = args__cmd_line.thing_name

    keep_asking = True
    while keep_asking == True:
        # If no thing name has been provided in the command line directly, request it from the user
        if thing_name_from_cmd_line == None:
            profile_names = list_existing_profiles(
                profiles_dir_path,
                header_message="Yout Profiles:",
            )
            example_names = list_existing_profiles(
                profiles_dir_path+examples_folder,
                header_message="Examples:",
                cnt_start=len(profile_names),
            )
            all_names = profile_names + example_names
            indexes = list(range(1, len(all_names) + 1))
            choice = input(
                f"Which profile ? ({blue}choose from options above{reset}): "
            )
            #  if user passed an instruction to quit the program:
            if choice in ["q", "quit"]:
                print(f"\n💀💀💀 {red}Program quit without compiling anything.{reset}")
                exit()
            # if user picked a valid index (number):
            elif choice.isdigit() and int(choice) in indexes:
                thing_name = all_names[int(choice) - 1]
            # if user wrote the article name directly and it is valid:
            elif choice in all_names:
                thing_name = choice
            # if invalid choice (non existing name or index):
            else:
                print(f"\n\n\n{red}Invalid choice{reset}, pick from options:\n")
                continue

            args__cmd_line.thing_name = thing_name
            print_choice_mesg(args__cmd_line)
            keep_asking = False

        # If thing name has been provided...
        # ...but it does not actually exist:
        elif thing_name_from_cmd_line not in all_names:
            print(f"\n\n\n{red}thing_name{reset} does not exist, pick from options:\n")
            # Restart proccess
            thing_name = None
        # ...and it exists:
        else:
            # Exit loop
            args__cmd_line.thing_name = thing_name_from_cmd_line
            print_choice_mesg(args__cmd_line)
            keep_asking = False

    return args__cmd_line


def ask_which_version_to_compile(build_dir: "str") -> str:
    keep_asking = True
    while keep_asking == True:
        v_names = list_existing_versions(
            build_dir,
            header_message="Available versions:",
        )
        indexes = list(range(1, len(v_names) + 1))
        choice = input(
            f"Which version do you want to compile? ({blue}choose from options above{reset}): "
        )
        #  if user passed an instruction to quit the program:
        if choice in ["q", "quit"]:
            print(f"\n💀💀💀 {red}Program quit without compiling anything.{reset}")
            exit()
        # if user picked a valid index (number):
        elif choice.isdigit() and int(choice) in indexes:
            return v_names[int(choice) - 1]
        # if user wrote the article name directly and it is valid:
        elif choice in v_names or choice+".tex" in v_names:
            return choice
        # if invalid choice (non existing name or index):
        else:
            print(f"\n\n\n{red}Invalid choice{reset}, pick from options:\n")
            continue



def print_choice_mesg(args:argparse.Namespace) -> None:
    """print a string announcing the document chosen by the user.

    Args:
        args (argparse.Namespace): an argument namespace.
    """
    print(f"You have chosen to compile {blue}{args.thing_name}{reset} in {blue}{args.recipe}{reset} recipe\n...")



def get_build_directory(args: argparse.Namespace) -> str:
    """ determine directory where to perform build

    Args:
        args (argparse.Namespace): arguments passed by the user

    Returns:
        str: path to build directory
    """
    if args.thing_name in profiles_names:
        dir_path = profiles_dir_path
    elif args.thing_name in examples_names:
        dir_path = profiles_dir_path + examples_folder
    build_directory = os.path.join(dir_path, args.thing_name)
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
    print(f"{blue}{msg}{reset} (step {counter})")
    if isTimer:
        time_now = datetime.now()
        delta_start = time_now - time_start
        print(f"\t⏲ {"Elapsed time since beginning:":<30} {green}{round(delta_start.total_seconds(), 2)}{reset} seconds")
        if time_prev != None:
            delta_prev = time_now - time_prev
            print(f"\t⏲ {"Elapsed time since prev. step:":<30} {green}{round(delta_prev.total_seconds(), 2)}{reset} seconds")
        return (time_now, counter)
    return (None, counter)