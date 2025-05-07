import os
from scripts.utils.style_console_text import red, green, blue, bold, reset
import shutil

def first_prompt(custom_prompt: str = None) -> None:
    """Print first prompt when script is lauched.

    Args:
        custom_prompt (str, optional): Initial prompt. Defaults to None.
    """
    # clear terminal
    os.system("cls" if os.name == "nt" else "clear")
    # get width of console in characters
    console_w = shutil.get_terminal_size().columns
    print(
        f"\t{'*' * (console_w - 8*2)}"
    )
    print(f"\t{bold}{blue}{custom_prompt.center(console_w - 8*2)}{reset}")
    print(
        f"\t{'*' * (console_w - 8*2)}\n"
    )
    print(
        f"\t{f'Script works with shell languages: {blue+bold}zsh (MacOS){reset}, {blue+bold}Batch Scripting (windows){reset}'}"
    )

    print(
        (
            f"\tProfile name convention: use only {bold+green}cammelCase{reset} (script performs automatic correction DOES IT ???)."
        )
    )
    print((f'\tType {bold+red}"q"{reset} or {bold+red}"quit"{reset} to exit program'))
    print(
        f"\t{'_' * (console_w - 8*2)}\n"
    )
