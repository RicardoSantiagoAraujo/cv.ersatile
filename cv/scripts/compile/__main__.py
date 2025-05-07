# LaTeX workshop is set up to used latexmk, which automates the proccess of generating a latex document. Under the hood, it calls a latex compiler, e.g., lualatex.
# However, it might be slow, so alternatively you can use this script which calls lualatex directly.

import argparse
import scripts.utils.prompts as prompts
from scripts.enums.Recipe import Recipe
from scripts.utils.style_console_text import blue,green, reset

from .functions import (
    all_cv_documents,
    deal_with_user_input,
    get_build_directory
)

from scripts.compile.compiler import perform_build_steps
from scripts.compile.watch import watcher
from scripts.compile.parameters import watch_frequency_seconds, file_types_to_watch, paths_to_ignore

def main() -> None:
    """Main function of script to compile an existing LaTeX document into a PDF."""

    prompts.first_prompt("Script for pdf compilation from existing document"
    )
    # Create command line argument parser
    parser = argparse.ArgumentParser(description="arTeX compilation with biblatex.")
    # Add arguments
    parser.add_argument(
        "cv_document",
        nargs="?",
        type=str,
        help=f"CV document to be compiled. Available options: {", ".join([f"{blue}{doc}{reset}" for doc in all_cv_documents])}",
        default=None,
    )
    parser.add_argument(
        "recipe",
        nargs="?",
        type=str,
        help=f"Compilation recipe. Available options: {", ".join([f"{blue}{e.value}{reset}" for e in Recipe])}.",
        default=Recipe.full.value,
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="prints compilation information to console"
    )
    parser.add_argument(
        "-t", "--timer", action="store_true", help="logs compilation duration to console"
    )
    parser.add_argument(
        "-w", "--watch", action="store_true", help="watch for changes and automatically recompile"
    )
    # Parse the arguments
    args = parser.parse_args()

    args = deal_with_user_input(args)

    if args.watch:
        # Continuous atch for changes:
        print(f"\n👀👀👀 {green}Watching for changes...{reset}\n")
        watcher(function_to_trigger=perform_build_steps,
                function_arguments=args,
                path_to_watch=get_build_directory(args),
                file_types= file_types_to_watch,
                paths_to_ignore=paths_to_ignore,
                frequency_sec= watch_frequency_seconds)
    else:
        # Single script run:
        perform_build_steps(args)


if __name__ == "__main__":
    main()
