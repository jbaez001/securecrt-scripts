# $language = "python"
# $interface = "1.0"

import re

PATTERNS = [
    r"(?P<title>[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9_\-\.]+)", # *nix user@host
    r"(?P<title>^RP\/\d+\/(?:RP|RSP)[0-1]\/CPU[0-9]:[a-zA-Z0-9_\-\.]+)#", # ioxr
    r"(?P<title>^[a-zA-Z0-9_\-\.]+)#\s" # ios/nx-os
]


def main():
    scrn = crt.GetScriptTab()
    scrn.Screen.Synchronous = True
    current_row = scrn.Screen.CurrentRow
    current_column = scrn.Screen.CurrentColumn
    prompt = scrn.Screen.Get(current_row, 1, current_row, current_column)

    for p in PATTERNS:
        m = re.search(p, prompt)

        if m is not None:
            scrn.Caption = m.group('title')

main()
