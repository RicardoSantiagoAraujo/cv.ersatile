import subprocess
import os
import sys
from typing import Optional
from scripts.utils.content_generation import *
import scripts.utils.style_console_text as sty

### Enums
from scripts.enums.GeneratedTypes import GeneratedTypes

###############################################################################
###############################################################################

#  CHANGE THESE TO FIT YOUR PROFILE'S PARTICULAR STRUCTURE
profiles = ["examples/johnDoe"]
sections = [
    "awards",
    "certificates",
    "description",
    "education",
    "experience",
    "other",
    "popScience",
    "informatics",
    "publications",
    "research",
    "teaching",
    "works",
]
constants = ["fonts", "colors", "general"]
versions = ["full"]
languages = ["en"]
output_types_sections = ["tex", "html"]
output_types_constants = ["tex", "scss", "ts"]

###############################################################################
###############################################################################


# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
# os.chdir(script_directory)


def main() -> Optional[int]:
    """Python script to generate multiple files for sections or constants.
    This script generates files for sections or constants based on the provided profile, section type, version, language, and file type.
    It loops through all combinations of profiles, sections/constants, versions, languages, and output types.

    Returns:
        int | None: Either none or an integer indicating the exit status of the script.
    """

    if len(sys.argv) == 2:
        group = GeneratedTypes(sys.argv[1]).value
    else:
        print_instructions(
            __name__,
            (
                "Type of content",
                f"Type of content to be generated",
                GeneratedTypes,
            ),
        )
        return 1

    if group == "sections":
        script = "scripts.generate.section"
        chosen_content = sections
        output_types = output_types_sections
    if group == "constants":
        script = "scripts.generate.constants"
        chosen_content = constants
        output_types = output_types_constants

    # Total number of loops that will be run
    total_loops = len(profiles) * len(chosen_content) * len(versions) * len(languages) * len(output_types)
    # Counter for  loops
    loop_counter = 0
    # Counter for failed loops
    error_counter = 0
    # List to store failed commands
    failed_commands = []

    #### LOOP to trigger commands
    for profile in profiles:
        for element in chosen_content:
            for version in versions:
                for language in languages:
                    for output_type in output_types:
                        print(
                            "python[3] -m",
                            script,
                            profile,
                            element,
                            version,
                            language,
                            output_type,
                        )
                        # might need to change to "python3" to work
                        result = subprocess.run(
                            [
                                "python3",
                                "-m",
                                script,
                                profile,
                                element,
                                version,
                                language,
                                output_type,
                            ]
                        )
                        loop_counter += 1
                        wasError = 1 if result.returncode != 0 else 0
                        error_counter += wasError
                        current_command = " ".join(result.args)
                        print(f"COMMAND: {sty.bright_blue}{current_command}{sty.reset}")
                        if result.returncode == 1 or wasError == 1:
                            failed_commands.append(current_command)
                            print(f"{sty.bright_red}{sty.bold}❌ ERROR ❌{sty.reset}")
                        print("------------------------------------------------")
                        print(f"\t✓✓ Loop {sty.cyan}{loop_counter}/{total_loops}{sty.reset} completed ✓✓")
                        print(
                            f"\t✓✓ {sty.green}{loop_counter - error_counter}/{total_loops}{sty.reset} were successful ✓✓"
                        )
                        print("------------------------------------------------\n")

    if len(failed_commands) > 0:
        print(f"{sty.bright_red}{sty.bold}FAILED CALLS ({error_counter}):{sty.reset}")
        for command in failed_commands:
            print(f"❌❌❌ {sty.yellow}{command}{sty.reset}")
    else:
        print("✅✅✅ All loops were successful ✅✅✅")


if __name__ == "__main__":
    main()
