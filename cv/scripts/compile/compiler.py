import subprocess
import os 
import scripts.utils.style_console_text as sty
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

        print(f"\n🏗️ RECIPE FOR BUILD: {sty.magenta+sty.bold}{args.recipe}{sty.reset}\n")
        # use a dispatch to mimick the switch case that python versions below < 3.10 do not have
        recipe_dispatch = {
            Recipe.full.value: recipe__full,
            Recipe.lualatex.value: recipe__lualatex,
            Recipe.biber.value: recipe__biber,
        }

        if args.recipe in recipe_dispatch:
            recipe_dispatch[args.recipe](args, latex_doc_name)
        else:
            print(f"{sty.red}CHOSEN COMPILATION RECIPE ({args.recipe}) DOES NOT EXIST{sty.reset}")
            exit()

        print(f"\n✅ {sty.green}Compilation in {sty.bold}{args.recipe}{sty.reset}{sty.green} recipe finished for {sty.bold}{args.profile_name}{sty.reset} \n")

    except subprocess.CalledProcessError as e:
        print("Compilation log:")
        print(e.stdout)
        print(e.stderr)
        print(f"{sty.red}Compilation failed{sty.reset}")
