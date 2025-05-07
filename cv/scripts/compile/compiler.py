import subprocess
import os
from scripts.utils.style_console_text import red, green, blue, bold, reset
from scripts.compile.functions import (
    create_build_directories, get_build_directory, ask_which_version_to_compile
)

from scripts.compile.recipes import recipe__biber, recipe__full, recipe__lualatex
from scripts.enums.Recipe import Recipe
import argparse
from datetime import datetime


def perform_build_steps(args: argparse.Namespace) -> None:
    """Compile a LaTeX document with lualaTeX.

    Args:
        args (argparse.Namespace): namespace with arguments parsed via command line.
    """

    build_directory = get_build_directory(args)
    if not vars(args).get("cv_document"):
        latex_doc_name = ask_which_version_to_compile(build_directory)
    else:
        latex_doc_name = args.cv_document


    try:
        # print( os.path.join(dir_path, thing_name + ".tex"))
        # CHANGE DIRECTORY TO THING'S
        os.chdir(build_directory)
        # CREATE BUILD FOLDERS IF IT DOES NOT EXIST
        create_build_directories()

        print(f"\n🏗️  RECIPE FOR BUILD: {blue}{args.recipe}{reset}\n")
        match args.recipe:
            case Recipe.full.value :
                recipe__full(args, latex_doc_name)
            case Recipe.lualatex.value:
                recipe__lualatex(args, latex_doc_name)
            case Recipe.biber.value :
                recipe__biber(args, latex_doc_name)
            case _:
                print(f"{red}CHOSEN COMPILATION RECIPE ({args.recipe}) DOES NOT EXIST {reset}")
                exit()

        print(f"\n✅ {green}Compilation in {bold}{args.recipe}{reset}{green} recipe finished for {bold}{args.profile_name}{reset} \n")

    except subprocess.CalledProcessError as e:
        print("Compilation log:")
        print(e.stdout)
        print(e.stderr)
        print(f"{red}Compilation failed{reset}")
