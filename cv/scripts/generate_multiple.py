import subprocess
import os
import sys
from content_generation import *

### Enums
from enums.generated_types import GeneratedTypes

# Get directory where the script is located
script_directory = os.path.dirname(os.path.realpath(__file__))
# Set it as working directory
os.chdir(script_directory)


def main():
    if len(sys.argv) == 2:
        group = GeneratedTypes(sys.argv[1]).value
    else:
        print_instructions(
            (
                "Type of content",
                f"Type of content to be generated {[e.value for e in GeneratedTypes]}",
                GeneratedTypes,
            ),
        )
        return 1

    profiles = ["examples/johnDoe"]
    sections = ["awards", "certificates", "description", "education", "experience", "other", "popScience", "programming", "publications", "research", "teaching", "works"]
    constants = ["fonts", "colors", "general"]
    versions =  ["full"]
    languages = ["en"]
    output_types_sections = ["tex", "html"]
    output_types_constants  = ["tex", "scss", "ts"]

    if group == "sections":
        script= "generate_section.py"
        chosen_content = sections
        output_types = output_types_sections
    if group == "constants":
        script= "generate_constants.py"
        chosen_content = constants
        output_types = output_types_constants


    # Total number of loops that will be run
    total_loops  = len(profiles)*len(chosen_content)*len(versions)*len(languages)*len(output_types)
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
                        result =  subprocess.run(
                            [
                            "python3",
                            script,
                            profile,
                            element,
                            version,
                            language,
                            output_type
                            ])
                        loop_counter += 1
                        error_counter += result.returncode
                        current_command = " ".join(result.args)
                        if result.returncode == 1:
                            failed_commands.append(current_command)
                        print("COMMAND: " + current_command)
                        print("--------------------------------------------------")
                        print(f"✓✓ Loop {loop_counter}/{total_loops} completed ✓")
                        print(f"✓✓ {total_loops - error_counter}/{total_loops} were successful ✓✓")
                        print("--------------------------------------------------\n")

    if len(failed_commands)>0:
        print(f"FAILED CALLS ({error_counter}):")
        for command in failed_commands:
            print("❌" + command)
    else:
        print("✅✅✅ All loops were successful ✅✅✅")



if __name__ == "__main__":
    main()
