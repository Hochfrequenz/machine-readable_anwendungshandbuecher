"""
This module iterates over all the files in the repository and generates a list of pruefis that are found.
"""
import re
import sys
from pathlib import Path
from typing import Set

_pruefi_json_pattern = re.compile("^(?P<pruefi>\d{5})\.json$")

if __name__ == "__main__":
    if sys.version_info.major != 3 or sys.version_info.minor < 9:
        sys.exit("Python 3.9 is required to run this script")
    # script is thought to be called from repo root as CWD
    supported_pruefis: Set[str] = set()
    for json_file_path in sorted(Path(".").glob("**/*.json")):
        if not (match := _pruefi_json_pattern.match(json_file_path.name)):
            continue
        pruefi = match.groupdict()["pruefi"]
        supported_pruefis.add(pruefi)
    supported_pruefis_list = sorted(list(supported_pruefis))
    print(f'Currently we support: {", ".join(supported_pruefis_list)}')
